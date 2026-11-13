"""Package fonts/ for release: npm packages (web fonts + CSS), zips, checksums.

For every folder fonts/<package>/ this writes

  dist/npm/<package>/          npm package @open-metric-fonts/<package>
      package.json, README.md, LICENSE (OFL), FONTLOG.txt
      files/<face>.woff2       one WOFF2 per style
      index.css                @font-face rules for every style in the package
      <family>.css             one family only (e.g. overlook-display.css)
      <family>-<weight>[-italic].css   one style only
  dist/zips/<package>-<version>.zip      ttf/, web/ (the npm files), licenses,
                                         fontconfig/ and libreoffice/ files
  dist/zips/open-metric-fonts-<version>.zip   every package in one zip
  dist/SHA256SUMS.txt          checksums of every zip
  dist/SRI.txt                 Subresource Integrity hash of every CSS file
  docs/web.md                  package list with CDN links and SRI hashes
  README.md                    the CDN example between <!-- cdn --> markers

Everything is deterministic (same fonts in -> same bytes out), so the SRI
hashes in docs/web.md match what CI publishes.

Usage: python scripts/package.py <version, e.g. 1.0.0> [--no-docs]
"""
from __future__ import annotations

import base64
import glob
import hashlib
import io
import json
import os
import re
import shutil
import sys
import zipfile
from xml.etree import ElementTree

from fontTools.ttLib import TTFont

def _root():
    """The repository root: the nearest parent folder with fonts/ and OFL.txt."""
    d = os.path.dirname(os.path.abspath(__file__))
    while not (os.path.isdir(os.path.join(d, "fonts")) and os.path.isfile(os.path.join(d, "OFL.txt"))):
        parent = os.path.dirname(d)
        if parent == d:
            raise SystemExit("cannot find the repository root (fonts/ and OFL.txt)")
        d = parent
    return d


ROOT = _root()
SCOPE = "@open-metric-fonts"
REPO = "https://github.com/open-metric-fonts/open-metric-fonts"
CDN = "https://cdn.jsdelivr.net/npm"
ZIP_DATE = (2026, 1, 1, 0, 0, 0)  # fixed timestamp inside zips, so they are reproducible
STYLE_WORDS = {"Thin", "Hairline", "ExtraLight", "UltraLight", "Light", "SemiLight", "Regular", "Normal",
               "Book", "Roman", "Medium", "SemiBold", "Semibold", "DemiBold", "Demi", "Bold", "ExtraBold",
               "UltraBold", "Heavy", "Black", "ExtraBlack", "Italic", "Oblique"}


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def aliases(pkg_dir):
    """{our family: original family} from the package's fontconfig file."""
    out = {}
    for conf in glob.glob(os.path.join(pkg_dir, "fontconfig", "*.conf")):
        for alias in ElementTree.parse(conf).getroot().iter("alias"):
            target = alias.find("family").text
            ours = alias.find("accept/family").text
            out[ours] = target
    return out


def faces(pkg_dir):
    out = []
    for path in sorted(glob.glob(os.path.join(pkg_dir, "*.ttf"))):
        font = TTFont(path)
        name = font["name"]
        # CSS family: typographic family plus any non-weight words of the
        # typographic style (Display, Condensed, Text, ...); weight and italic
        # become font-weight / font-style.
        words = (name.getDebugName(17) or name.getDebugName(2) or "").split()
        extra = [w for w in words if w not in STYLE_WORDS]
        family = " ".join([name.getDebugName(16) or name.getDebugName(1)] + extra)
        legacy = name.getDebugName(1)
        sub = name.getDebugName(2)
        weight = font["OS/2"].usWeightClass
        italic = bool(font["OS/2"].fsSelection & 1)
        stem = os.path.splitext(os.path.basename(path))[0]
        out.append(dict(path=path, font=font, family=family, legacy=legacy, sub=sub, weight=weight,
                        italic=italic, file=f"{slug(stem)}.woff2", version=name.getDebugName(5)))
    return out


def font_face(family, face, local=None):
    src = f"url(./files/{face['file']}) format('woff2')"
    if local:
        src = f"local('{local}'), " + src
    return ("@font-face {\n"
            f"  font-family: '{family}';\n"
            f"  font-style: {'italic' if face['italic'] else 'normal'};\n"
            f"  font-weight: {face['weight']};\n"
            "  font-display: swap;\n"
            f"  src: {src};\n"
            "}\n")


def target_face_name(target_legacy, face):
    """Full name of the original's matching face, for local()."""
    return target_legacy if face["sub"] == "Regular" else f"{target_legacy} {face['sub']}"


def build_package(pkg, version, out_root):
    pkg_dir = os.path.join(ROOT, "fonts", pkg)
    fs = faces(pkg_dir)
    want = f"Version {version.split('.')[0]}.{''.join(version.split('.')[1:]).ljust(3, '0')[:3]}"
    bad = sorted({f["version"] for f in fs if f["version"] != want})
    if bad:
        raise SystemExit(f"{pkg}: fonts say {bad}, release is {version} ({want})")
    # Faces that would clash (same family, weight and style, e.g. Regular and
    # Book both at 400) use their Windows family name instead, which is unique.
    from collections import Counter
    count = Counter((f["family"], f["weight"], f["italic"]) for f in fs)
    for f in fs:
        if count[(f["family"], f["weight"], f["italic"])] > 1:
            f["family"] = f["legacy"]
    seen = {}
    for f in fs:
        key = (f["family"], f["weight"], f["italic"])
        if key in seen:
            raise SystemExit(f"{pkg}: {os.path.basename(seen[key])} and {os.path.basename(f['path'])} "
                             f"would both be CSS {key}")
        seen[key] = f["path"]
    legacy_alias = aliases(pkg_dir)   # legacy family names: "Grandview Display" -> ours
    out = os.path.join(out_root, pkg)
    os.makedirs(os.path.join(out, "files"))
    css = {}
    for f in fs:
        f["font"].flavor = "woff2"
        f["font"].save(os.path.join(out, "files", f["file"]))
        rule = font_face(f["family"], f)
        css.setdefault("index.css", []).append(rule)
        css.setdefault(f"{slug(f['family'])}.css", []).append(rule)
        css.setdefault(f"{slug(f['family'])}-{f['weight']}{'-italic' if f['italic'] else ''}.css", []).append(rule)
    for name, rules in css.items():
        with open(os.path.join(out, name), "w", encoding="utf-8", newline="\n") as fh:
            fh.write("\n".join(rules))
    shutil.copy(os.path.join(pkg_dir, "OFL.txt"), os.path.join(out, "LICENSE"))
    shutil.copy(os.path.join(pkg_dir, "FONTLOG.txt"), os.path.join(out, "FONTLOG.txt"))
    families = sorted({f["family"] for f in fs})
    targets = sorted(set(legacy_alias.values()))
    desc = (f"Open-source (OFL) font{'s' if len(families) > 1 else ''} {', '.join(families)}: "
            f"metric-compatible with {', '.join(targets)}. Same character widths, line breaks and page breaks.")
    meta = {
        "name": f"{SCOPE}/{pkg}",
        "version": version,
        "description": desc[:300],
        "license": "OFL-1.1",
        "main": "index.css",
        "style": "index.css",
        "files": ["files/", "*.css", "LICENSE", "FONTLOG.txt", "README.md"],
        "keywords": ["font", "fonts", "webfont", "woff2", "metric-compatible", "ofl", "open-metric-fonts"]
                    + [slug(t) for t in targets],
        "homepage": f"{REPO}#readme",
        "repository": {"type": "git", "url": f"git+{REPO}.git", "directory": f"fonts/{pkg}"},
        "bugs": f"{REPO}/issues",
        "publishConfig": {"access": "public", "provenance": True},
    }
    with open(os.path.join(out, "package.json"), "w", encoding="utf-8", newline="\n") as fh:
        json.dump(meta, fh, indent=2)
        fh.write("\n")
    sri = {name: sri_hash(os.path.join(out, name)) for name in sorted(css)}
    with open(os.path.join(out, "README.md"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(package_readme(pkg, version, families, targets, fs, sri))
    return dict(pkg=pkg, families=families, targets=targets, styles=len(fs), sri=sri)


def sri_hash(path):
    with open(path, "rb") as fh:
        return "sha384-" + base64.b64encode(hashlib.sha384(fh.read()).digest()).decode()


def link_tag(pkg, version, name, sri):
    return (f'<link rel="stylesheet" href="{CDN}/{SCOPE}/{pkg}@{version}/{name}"\n'
            f'      integrity="{sri}" crossorigin="anonymous">')


def package_readme(pkg, version, families, targets, fs, sri):
    first = families[0]
    styles = "\n".join(f"| {f['family']} | {f['weight']} | {'italic' if f['italic'] else 'normal'} | "
                       f"`{slug(f['family'])}-{f['weight']}{'-italic' if f['italic'] else ''}.css` |" for f in fs)
    return f"""# {SCOPE}/{pkg}

{', '.join(families)}: open-source (SIL Open Font License 1.1) fonts that are **metric-compatible** with {', '.join(targets)}. Every character has the original's width and the line spacing is the same, so text breaks into the same lines and pages. The letter shapes are not copies: each font is a modified version of an openly licensed font.

Part of [open-metric-fonts]({REPO}). Desktop fonts (TTF), fontconfig and LibreOffice files are in the [GitHub releases]({REPO}/releases).

## Install

```bash
npm install {SCOPE}/{pkg}
```

```js
import "{SCOPE}/{pkg}";             // every style
import "{SCOPE}/{pkg}/{slug(first)}-400.css";  // or one style
```

```css
body {{ font-family: "{first}", sans-serif; }}
```

## CDN (pinned version, with Subresource Integrity)

```html
{link_tag(pkg, version, "index.css", sri["index.css"])}
```

npm versions cannot be changed once published, and the `integrity` hash makes the browser reject a stylesheet that differs from this release. Every CSS file's hash is listed in [web.md]({REPO}/blob/main/docs/web.md).

## Styles

| Family | Weight | Style | CSS file |
|---|---|---|---|
{styles}

## License

Fonts: SIL Open Font License 1.1 (see `LICENSE`); each font keeps its base font's copyright notice. Font names of the originals are trademarks of their owners and are used only to describe compatibility; this project is not affiliated with or endorsed by them.
"""


def add_tree(zf, src, arc):
    for dirpath, _, files in sorted(os.walk(src)):
        for name in sorted(files):
            full = os.path.join(dirpath, name)
            rel = os.path.relpath(full, src).replace(os.sep, "/")
            info = zipfile.ZipInfo(f"{arc}/{rel}", ZIP_DATE)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            with open(full, "rb") as fh:
                zf.writestr(info, fh.read())


def make_zip(path, entries):
    with zipfile.ZipFile(path, "w") as zf:
        for src, arc in entries:
            add_tree(zf, src, arc)


def stage_package(pkg, npm_dir, stage_root):
    """Layout inside a zip: <pkg>/ttf, <pkg>/web, licenses, fontconfig, libreoffice."""
    src = os.path.join(ROOT, "fonts", pkg)
    dest = os.path.join(stage_root, pkg)
    os.makedirs(os.path.join(dest, "ttf"))
    for ttf in sorted(glob.glob(os.path.join(src, "*.ttf"))):
        shutil.copy(ttf, os.path.join(dest, "ttf"))
    shutil.copytree(npm_dir, os.path.join(dest, "web"), ignore=shutil.ignore_patterns("package.json"))
    for extra in ("OFL.txt", "FONTLOG.txt"):
        shutil.copy(os.path.join(src, extra), dest)
    for sub in ("fontconfig", "libreoffice"):
        if os.path.isdir(os.path.join(src, sub)):
            shutil.copytree(os.path.join(src, sub), os.path.join(dest, sub))
    return dest


def write_web_doc(results, version):
    rows = []
    for r in results:
        rows.append(f"| {', '.join(r['targets'])} | `{SCOPE}/{r['pkg']}` | {', '.join(r['families'])} | {r['styles']} |")
    sri_rows = []
    for r in results:
        for name, h in r["sri"].items():
            sri_rows.append(f"| `{SCOPE}/{r['pkg']}@{version}/{name}` | `{h}` |")
    doc = f"""# Web fonts and npm packages

Every font folder is published to npm as `{SCOPE}/<name>` (WOFF2 files and CSS), which also makes it available from the jsDelivr and unpkg CDNs. The same files are in each release zip under `web/` for self-hosting. This page is generated for version {version}.

## Use

```bash
npm install {SCOPE}/overlook
```

```html
<!-- CDN: pinned version + Subresource Integrity (hashes below) -->
{link_tag("overlook", version, "index.css", next(r for r in results if r['pkg'] == 'overlook')['sri']['index.css'])}
```

- `index.css`: every style in the package. `<family>.css`: one family. `<family>-<weight>[-italic].css`: one style.

## Security

- **Pin a version.** npm versions are immutable, so `@{version}` always serves the same bytes. Avoid unpinned or `@latest` URLs in production.
- **Use the `integrity` attribute.** Browsers refuse a stylesheet whose hash differs. The CSS only references font files of the same pinned version.
- **Self-host if you can.** Download the release zip, check it against `SHA256SUMS.txt` and the build attestation (see the README), and serve `web/` from your own domain.
- npm packages are published from GitHub Actions with npm provenance, which links each package version to the commit and workflow that built it.

## Packages

| Compatible with | Package | Families | Styles |
|---|---|---|---|
{chr(10).join(rows)}

## Subresource Integrity hashes

| File | integrity |
|---|---|
{chr(10).join(sri_rows)}
"""
    with open(os.path.join(ROOT, "docs", "web.md"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(doc)


def write_readme_cdn(results, version):
    """Real CDN example (with its SRI hash) between the README's cdn markers."""
    path = os.path.join(ROOT, "README.md")
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    start, end = "<!-- cdn:start -->", "<!-- cdn:end -->"
    r = next(r for r in results if r["pkg"] == "overlook")
    tag = link_tag("overlook", version, "index.css", r["sri"]["index.css"])
    block = f"{start}\n```html\n{tag}\n```\n{end}"
    text = text[:text.index(start)] + block + text[text.index(end) + len(end):]
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def main(argv):
    args = argv[1:]
    if not args or not re.fullmatch(r"\d+\.\d+\.\d+", args[0]):
        raise SystemExit(__doc__)
    version = args[0]
    dist = os.path.join(ROOT, "dist")
    shutil.rmtree(dist, ignore_errors=True)
    npm_root, zip_root, stage = (os.path.join(dist, d) for d in ("npm", "zips", "stage"))
    os.makedirs(zip_root)
    pkgs = sorted(os.path.basename(p) for p in glob.glob(os.path.join(ROOT, "fonts", "*")) if os.path.isdir(p))
    results = []
    for pkg in pkgs:
        results.append(build_package(pkg, version, npm_root))
        dest = stage_package(pkg, os.path.join(npm_root, pkg), stage)
        make_zip(os.path.join(zip_root, f"{pkg}-{version}.zip"), [(dest, pkg)])
    shutil.copy(os.path.join(ROOT, "OFL.txt"), stage)
    with open(os.path.join(ROOT, "README.md"), "rb") as fh:
        readme = fh.read()
    with open(os.path.join(stage, "README.md"), "wb") as fh:
        fh.write(readme)
    allzip = os.path.join(zip_root, f"open-metric-fonts-{version}.zip")
    with zipfile.ZipFile(allzip, "w") as zf:
        for name in sorted(os.listdir(stage)):
            full = os.path.join(stage, name)
            if os.path.isdir(full):
                add_tree(zf, full, f"open-metric-fonts-{version}/{name}")
            else:
                info = zipfile.ZipInfo(f"open-metric-fonts-{version}/{name}", ZIP_DATE)
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o644 << 16
                with open(full, "rb") as fh:
                    zf.writestr(info, fh.read())
    shutil.rmtree(stage)
    with open(os.path.join(dist, "SHA256SUMS.txt"), "w", encoding="utf-8", newline="\n") as fh:
        for z in sorted(os.listdir(zip_root)):
            with open(os.path.join(zip_root, z), "rb") as zfh:
                fh.write(f"{hashlib.sha256(zfh.read()).hexdigest()}  {z}\n")
    with open(os.path.join(dist, "SRI.txt"), "w", encoding="utf-8", newline="\n") as fh:
        for r in results:
            for name, h in r["sri"].items():
                fh.write(f"{h}  {SCOPE}/{r['pkg']}@{version}/{name}\n")
    if "--no-docs" not in args:
        write_web_doc(results, version)
        write_readme_cdn(results, version)
    total = sum(r["styles"] for r in results)
    print(f"{len(results)} packages, {total} styles; zips, SHA256SUMS.txt and SRI.txt in dist/")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
