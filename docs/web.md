# Web fonts and npm packages

Every font folder is published to npm as `@open-metric-fonts/<name>` (WOFF2 files and CSS), which also makes it available from the jsDelivr and unpkg CDNs. The same files are in each release zip under `web/` for self-hosting. This page is generated for version 1.0.0.

## Use

```bash
npm install @open-metric-fonts/overlook
```

```html
<!-- CDN: pinned version + Subresource Integrity (hashes below) -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@open-metric-fonts/overlook@1.0.0/index.css"
      integrity="sha384-eJIsixtMs7+MdQK4W8SVFXqyFcAc18ikQ4hWerGRHbULWoKvk1qsaP3o12nYxBWy" crossorigin="anonymous">
```

- `index.css`: every style in the package. `<family>.css`: one family. `<family>-<weight>[-italic].css`: one style.

## Security

- **Pin a version.** npm versions are immutable, so `@1.0.0` always serves the same bytes. Avoid unpinned or `@latest` URLs in production.
- **Use the `integrity` attribute.** Browsers refuse a stylesheet whose hash differs. The CSS only references font files of the same pinned version.
- **Self-host if you can.** Download the release zip, check it against `SHA256SUMS.txt` and the build attestation (see the README), and serve `web/` from your own domain.
- npm packages are published from GitHub Actions with npm provenance, which links each package version to the commit and workflow that built it.

## Packages

| Compatible with | Package | Families | Styles |
|---|---|---|---|
| Arial Nova, Arial Nova Cond, Arial Nova Cond Light, Arial Nova Light | `@open-metric-fonts/aerie-nova` | Aerie Nova, Aerie Nova Condensed | 12 |
| Century | `@open-metric-fonts/almanac` | Almanac | 1 |
| Impact | `@open-metric-fonts/anvil` | Anvil | 1 |
| Californian FB | `@open-metric-fonts/bancroft` | Bancroft | 3 |
| Sitka, Sitka Banner, Sitka Banner Semibold, Sitka Display, Sitka Display Semibold, Sitka Heading, Sitka Heading Semibold, Sitka Small, Sitka Small Semibold, Sitka Subheading, Sitka Subheading Semibold, Sitka Text, Sitka Text Semibold | `@open-metric-fonts/baranof` | Baranof Banner, Baranof Display, Baranof Heading, Baranof Small, Baranof Subheading, Baranof Text | 36 |
| Bookman Old Style | `@open-metric-fonts/bindery` | Bindery | 4 |
| Sagona, Sagona Book, Sagona ExtraLight | `@open-metric-fonts/calvi` | Calvi, Calvi Book | 8 |
| Garamond | `@open-metric-fonts/colines` | Colines | 3 |
| Century Gothic | `@open-metric-fonts/compass` | Compass | 4 |
| Tenorite, Tenorite Display | `@open-metric-fonts/cuprite` | Cuprite, Cuprite Display | 8 |
| Perpetua, Perpetua Titling MT | `@open-metric-fonts/ditchling` | Ditchling, Ditchling Titling MT | 6 |
| Abadi | `@open-metric-fonts/dune` | Dune | 4 |
| Baskerville Old Face | `@open-metric-fonts/easyhill` | Easyhill | 1 |
| Amasis MT Pro, Amasis MT Pro Black, Amasis MT Pro Light | `@open-metric-fonts/faience` | Faience | 8 |
| Constantia | `@open-metric-fonts/fidela` | Fidela | 4 |
| Segoe Script | `@open-metric-fonts/flourish` | Flourish | 2 |
| Verdana | `@open-metric-fonts/glade` | Glade | 4 |
| Verdana Pro, Verdana Pro Black, Verdana Pro Cond, Verdana Pro Light, Verdana Pro Semibold | `@open-metric-fonts/glade-pro` | Glade Pro, Glade Pro Cond | 14 |
| Bahnschrift, Bahnschrift Condensed, Bahnschrift Light, Bahnschrift Light Condensed, Bahnschrift Light SemiCondensed, Bahnschrift SemiBold, Bahnschrift SemiBold Condensed, Bahnschrift SemiBold SemiCondensed, Bahnschrift SemiCondensed, Bahnschrift SemiLight, Bahnschrift SemiLight Condensed, Bahnschrift SemiLight SemiCondensed | `@open-metric-fonts/gleis` | Gleis, Gleis Condensed, Gleis SemiCondensed | 15 |
| Century Schoolbook | `@open-metric-fonts/hornbook` | Hornbook | 4 |
| MV Boli | `@open-metric-fonts/lagoon` | Lagoon | 1 |
| Franklin Gothic Book, Franklin Gothic Demi, Franklin Gothic Demi Cond, Franklin Gothic Heavy, Franklin Gothic Medium, Franklin Gothic Medium Cond | `@open-metric-fonts/leyden` | Leyden Book, Leyden Demi, Leyden Demi Cond, Leyden Heavy, Leyden Medium, Leyden Medium Cond | 10 |
| Corbel, Corbel Light | `@open-metric-fonts/lintel` | Lintel | 6 |
| Palatino Linotype | `@open-metric-fonts/loggia` | Loggia | 4 |
| Trebuchet MS | `@open-metric-fonts/mangonel` | Mangonel | 4 |
| Posterama | `@open-metric-fonts/marquee` | Marquee | 4 |
| Aptos Mono | `@open-metric-fonts/morrow-mono` | Morrow Mono | 4 |
| Aptos, Aptos Black, Aptos Display, Aptos ExtraBold, Aptos Light, Aptos Narrow, Aptos SemiBold | `@open-metric-fonts/morrow-sans` | Morrow Sans, Morrow Sans Display, Morrow Sans Narrow | 20 |
| Aptos Serif | `@open-metric-fonts/morrow-serif` | Morrow Serif | 4 |
| Goudy Old Style | `@open-metric-fonts/oakwood` | Oakwood | 3 |
| Avenir Next LT Pro, Avenir Next LT Pro Demi, Avenir Next LT Pro Light | `@open-metric-fonts/onward` | Onward | 8 |
| Univers, Univers Condensed, Univers Condensed Light, Univers Light | `@open-metric-fonts/orbis` | Orbis, Orbis Condensed | 6 |
| Microsoft Sans Serif | `@open-metric-fonts/ordinal` | Ordinal | 1 |
| Grandview, Grandview Display | `@open-metric-fonts/overlook` | Overlook, Overlook Display | 6 |
| Bodoni MT, Bodoni MT Black, Bodoni MT Condensed, Bodoni MT Poster Compressed | `@open-metric-fonts/parma` | Parma, Parma Condensed, Parma Poster Compressed | 11 |
| Georgia Pro, Georgia Pro Black, Georgia Pro Cond, Georgia Pro Light, Georgia Pro Semibold | `@open-metric-fonts/peachtree` | Peachtree, Peachtree Cond | 14 |
| Segoe Print | `@open-metric-fonts/penmark` | Penmark | 2 |
| Daytona, Daytona Condensed, Daytona Light | `@open-metric-fonts/pitlane` | Pitlane, Pitlane Condensed | 7 |
| Sylfaen | `@open-metric-fonts/plinth` | Plinth | 1 |
| Lucida Bright, Lucida Calligraphy, Lucida Console, Lucida Fax, Lucida Handwriting, Lucida Sans, Lucida Sans Typewriter, Lucida Sans Unicode | `@open-metric-fonts/prism` | Prism Bright, Prism Bright Demibold, Prism Calligraphy, Prism Console, Prism Fax, Prism Fax Demibold, Prism Handwriting, Prism Sans, Prism Sans Demibold, Prism Sans Typewriter, Prism Sans Unicode | 20 |
| Rockwell, Rockwell Condensed, Rockwell Extra Bold | `@open-metric-fonts/quarry` | Quarry, Quarry Condensed, Quarry Extra Bold | 7 |
| Rockwell Nova, Rockwell Nova Cond, Rockwell Nova Light | `@open-metric-fonts/quarry-nova` | Quarry Nova, Quarry Nova Condensed | 10 |
| Neue Haas Grotesk Text Pro | `@open-metric-fonts/rhine` | Rhine | 4 |
| Gill Sans MT, Gill Sans MT Condensed, Gill Sans MT Ext Condensed Bold, Gill Sans Ultra Bold, Gill Sans Ultra Bold Condensed | `@open-metric-fonts/rill` | Rill, Rill Condensed, Rill Ext Condensed Bold, Rill Ultra Bold, Rill Ultra Bold Condensed | 8 |
| Gill Sans Nova, Gill Sans Nova Cond, Gill Sans Nova Cond Lt, Gill Sans Nova Light | `@open-metric-fonts/rill-nova` | Rill Nova, Rill Nova Cond, Rill Nova Cond Lt | 12 |
| Bierstadt, Bierstadt Display | `@open-metric-fonts/sawtooth` | Sawtooth, Sawtooth Display | 6 |
| Ink Free | `@open-metric-fonts/scrawl` | Scrawl | 1 |
| Gabriola | `@open-metric-fonts/seraphine` | Seraphine | 1 |
| Skeena, Skeena Display | `@open-metric-fonts/stikine` | Stikine, Stikine Display | 8 |
| Tahoma | `@open-metric-fonts/tamarack` | Tamarack | 2 |
| Candara, Candara Light | `@open-metric-fonts/taper` | Taper, Taper Light | 6 |
| Seaford, Seaford Display | `@open-metric-fonts/tidewater` | Tidewater, Tidewater Display | 6 |
| Sabon Next LT | `@open-metric-fonts/tympan` | Tympan | 4 |
| Calisto MT | `@open-metric-fonts/ursa` | Ursa | 4 |
| Book Antiqua | `@open-metric-fonts/vellum` | Vellum | 4 |
| Walbaum, Walbaum Display, Walbaum Heading, Walbaum Text | `@open-metric-fonts/weimar` | Weimar Display, Weimar Heading, Weimar Text | 12 |
| Trade Gothic Next, Trade Gothic Next Cond, Trade Gothic Next HvyCd, Trade Gothic Next Light | `@open-metric-fonts/wharf` | Wharf, Wharf Condensed | 12 |
| Tw Cen MT, Tw Cen MT Condensed, Tw Cen MT Condensed Extra Bold | `@open-metric-fonts/zenith` | Zenith, Zenith Condensed, Zenith Condensed Extra Bold | 7 |

## Subresource Integrity hashes

| File | integrity |
|---|---|
| `@open-metric-fonts/aerie-nova@1.0.0/aerie-nova-300-italic.css` | `sha384-3dS3ppipAhzxsu2oN0rIMjYCpdTfolA4FQSQQ1dv8NpkLiZJPlhJntuFuhEcIVGP` |
| `@open-metric-fonts/aerie-nova@1.0.0/aerie-nova-300.css` | `sha384-ZkaPtK8XBb1Cs2j+RKlGkVvlOyELmtc/ygP5zRee9fKawO5OaXFheoY/4Kb663qz` |
| `@open-metric-fonts/aerie-nova@1.0.0/aerie-nova-400-italic.css` | `sha384-iNgitYOcCzgq8n/oOaCkspgnvMatBAMlgEoBUy3MM6tg/dbOXo83l/OzLQxfuzQf` |
| `@open-metric-fonts/aerie-nova@1.0.0/aerie-nova-400.css` | `sha384-VH11L+kJ8WOANff0ks9m70z3b2lgSKDYuvPq0aolcuCg5WA+mPwfV87rU2Yg245x` |
| `@open-metric-fonts/aerie-nova@1.0.0/aerie-nova-700-italic.css` | `sha384-d67n/3TxEYpBLQbjMwQUIHsuYJR3NYPBLguMWCY31SZxXB3/d9ofkZBrXYGz3W9n` |
| `@open-metric-fonts/aerie-nova@1.0.0/aerie-nova-700.css` | `sha384-tScCLg1ZsjkQhvI9wWQolcBfxKDI8XlYr9EBdyxLya+8wu+B0/CioobcV91eivs8` |
| `@open-metric-fonts/aerie-nova@1.0.0/aerie-nova-condensed-300-italic.css` | `sha384-GdLAR8+I7CcS1spryCbrVgwQhh2B77uY/D7g1FHJl2RSSOSLAJR072qE+WMX8MWJ` |
| `@open-metric-fonts/aerie-nova@1.0.0/aerie-nova-condensed-300.css` | `sha384-HMeqf6im5m+fU3NQInREKkVmB1VE7Ly5UYhhLfdE4PV8aF4HQPbfqbOZl0YC969H` |
| `@open-metric-fonts/aerie-nova@1.0.0/aerie-nova-condensed-400-italic.css` | `sha384-1qhSak1GMgDFAMllEap0tpcdCN/cVztJbAy1/Fb/nVxDSkbDOk4RuK1QrRALTsX3` |
| `@open-metric-fonts/aerie-nova@1.0.0/aerie-nova-condensed-400.css` | `sha384-EXEjtnYGIAkNC+QbN0xaaMKD+wklJRN4FVxjCDUNpwNnxaKjkB5MRZuwO6nqfy5U` |
| `@open-metric-fonts/aerie-nova@1.0.0/aerie-nova-condensed-700-italic.css` | `sha384-mfAUmfJgAn00SL/tmB0Qee4GXJbGB4qdDLZX/YWHQ5GrdpJ1nkZxwsvMkE2Ujs2E` |
| `@open-metric-fonts/aerie-nova@1.0.0/aerie-nova-condensed-700.css` | `sha384-HUw/Ym5i4ILLYXUOkBay7xLd7z3MhpdSpmuyrTiUe1EjOeW53JV9JKR4iEo69s2H` |
| `@open-metric-fonts/aerie-nova@1.0.0/aerie-nova-condensed.css` | `sha384-qJxV/VB+wsUM+CxVVuhljp/pn9BI75Wp/HGLil9jxMOgHpgfv/Ci9cEAXc9oSYKV` |
| `@open-metric-fonts/aerie-nova@1.0.0/aerie-nova.css` | `sha384-s6t6apsBf1ZH5KlLchLvny9pk3M3xAlkms7mtIYc8gpi6zjWrQoWLQJc8yvg/Ap+` |
| `@open-metric-fonts/aerie-nova@1.0.0/index.css` | `sha384-2X1KiygHW4HrsOiVuZ+44DtCxGRdDZjeZ+Z4lRmSIf72+GeS1z3xibsj6nVXoS/y` |
| `@open-metric-fonts/almanac@1.0.0/almanac-400.css` | `sha384-4GQ1+hlWQc7urx/TgdmuDCndACnI3a4pxfQD3Oo1aTRHeKxgFSP7xPHB94GMt9y2` |
| `@open-metric-fonts/almanac@1.0.0/almanac.css` | `sha384-4GQ1+hlWQc7urx/TgdmuDCndACnI3a4pxfQD3Oo1aTRHeKxgFSP7xPHB94GMt9y2` |
| `@open-metric-fonts/almanac@1.0.0/index.css` | `sha384-4GQ1+hlWQc7urx/TgdmuDCndACnI3a4pxfQD3Oo1aTRHeKxgFSP7xPHB94GMt9y2` |
| `@open-metric-fonts/anvil@1.0.0/anvil-400.css` | `sha384-r9jo/bn079wDIMPq34gprVRnXHZhfw791Es7mK7hccXhRVRjmE1jVtCu1swUhoh/` |
| `@open-metric-fonts/anvil@1.0.0/anvil.css` | `sha384-r9jo/bn079wDIMPq34gprVRnXHZhfw791Es7mK7hccXhRVRjmE1jVtCu1swUhoh/` |
| `@open-metric-fonts/anvil@1.0.0/index.css` | `sha384-r9jo/bn079wDIMPq34gprVRnXHZhfw791Es7mK7hccXhRVRjmE1jVtCu1swUhoh/` |
| `@open-metric-fonts/bancroft@1.0.0/bancroft-400-italic.css` | `sha384-3nbuFYVkBTunSNevNcnRGJAgZ+tzJrPMuJKhcF0Q7qv2h3FGX/UjxGd30qcCUsNh` |
| `@open-metric-fonts/bancroft@1.0.0/bancroft-400.css` | `sha384-r3W9lMa54kEBF+NG7PJsOA7JWJsn3J5hJ6It+RoSlursz/lOghLZhZbZELD8WUFw` |
| `@open-metric-fonts/bancroft@1.0.0/bancroft-700.css` | `sha384-m3Z5QEfPi5p2vB+1m5+Kcy4cM1Lb1njCQxpTP+43ohh9AYImluxqUhdPyzQSwDhq` |
| `@open-metric-fonts/bancroft@1.0.0/bancroft.css` | `sha384-a7vlHmKjx106JanUiEWztnAYbwBR/6naBpK2BMw7+GJndfytSwavTObzsSNeLBYC` |
| `@open-metric-fonts/bancroft@1.0.0/index.css` | `sha384-a7vlHmKjx106JanUiEWztnAYbwBR/6naBpK2BMw7+GJndfytSwavTObzsSNeLBYC` |
| `@open-metric-fonts/baranof@1.0.0/baranof-banner-400-italic.css` | `sha384-Yn7PoVFhzax1eGYceRjINeVHoJE577yuV/UemEOpaRtIzUCJMWWA77O94gDyusyE` |
| `@open-metric-fonts/baranof@1.0.0/baranof-banner-400.css` | `sha384-j4s4Z6Qgn3H5x1UctRVLOs7LzvGwygkyi/5Vq0mgiXGTwYHW5BnPNXdcxf8z/pPL` |
| `@open-metric-fonts/baranof@1.0.0/baranof-banner-600-italic.css` | `sha384-rX97ce5myCTIsjGZOHOh9/aZq3f1dtqmO14CbudpTWjTpkyWcN7VyieEaozfAlp7` |
| `@open-metric-fonts/baranof@1.0.0/baranof-banner-600.css` | `sha384-TD3jrQwcc/vITXysUmqId0kmE/xY2ZAeOKfSSiG0VRudHkeGckZecaSM8EXuRHdx` |
| `@open-metric-fonts/baranof@1.0.0/baranof-banner-700-italic.css` | `sha384-GzK5JAD1PO1wUzENLI92jKyCxEizDLY3FVLkSuDtmTRsw/6BEfRZVGXW7N4LCjBc` |
| `@open-metric-fonts/baranof@1.0.0/baranof-banner-700.css` | `sha384-7rxiPYYLWWZAqHdPEAOEjt8ZnDwJKU7jZdqBlxbmiz2wtib+nD2Xao1Nnm2gZZ1P` |
| `@open-metric-fonts/baranof@1.0.0/baranof-banner.css` | `sha384-VexBBHAhXvk42llAqGhcLqCaAHFs0+AAyBMp0bRWQ39r13P6S+ZW6n28Am4YooKq` |
| `@open-metric-fonts/baranof@1.0.0/baranof-display-400-italic.css` | `sha384-B6Vnc/H62NgztG1FsCClTruheiZtD25gMSRODzHikteIwyrqrkfUeWhostpcb+/I` |
| `@open-metric-fonts/baranof@1.0.0/baranof-display-400.css` | `sha384-ecW6Z7BLHndVtkNlmMDt4CFvWD65fgEF2vXlmtU5orDK6IWb3f4LUlZ1hBv18R57` |
| `@open-metric-fonts/baranof@1.0.0/baranof-display-600-italic.css` | `sha384-h2Hjlu9dw+OmDF/qonPGIuTysa/7OTWZLeqgEU6Dz04XFnrTFmwcVf1XsxkAwjSI` |
| `@open-metric-fonts/baranof@1.0.0/baranof-display-600.css` | `sha384-c8x77CqOPBBwv5oVQ7WnfexeNqKlb0h0LX3NcvLl0/R1dfCg5YEwBUcnSTmx0zlk` |
| `@open-metric-fonts/baranof@1.0.0/baranof-display-700-italic.css` | `sha384-ZEmUuIqnZzU6o2ZX2zj/l/8GVFpEMbO48u3h4nMMmFtkliVpVYKTRj16AhEfEEJY` |
| `@open-metric-fonts/baranof@1.0.0/baranof-display-700.css` | `sha384-5Ci4Or1txmka8hq9wa0aisL+wuGm3XHAkYp9xvqNirIEbKnbRwG6S8d7MKTIdPvo` |
| `@open-metric-fonts/baranof@1.0.0/baranof-display.css` | `sha384-q+EUkHOifbzwurOX9rrajdHeeh4LRkEoXjlWK73WUk6Hgz41nPsAUx2AU6ESqWwA` |
| `@open-metric-fonts/baranof@1.0.0/baranof-heading-400-italic.css` | `sha384-K3wi9+tN/kc5vhNdG1kMSZI/vTa45b7xvgy7lH/LA23+pVOLb0vK9NIc6tMUaEiK` |
| `@open-metric-fonts/baranof@1.0.0/baranof-heading-400.css` | `sha384-M8AwVl2yryTYo4BNl6CyFjokYDrTf8AqrZ6U9iV9d3iZegETPmlhRxWVdl6+QtHk` |
| `@open-metric-fonts/baranof@1.0.0/baranof-heading-600-italic.css` | `sha384-tNARyau5xx96oI3JvbFMNBN4UhN/aprGea9NZKy6Q528URbmHPVw10A6OtQHake7` |
| `@open-metric-fonts/baranof@1.0.0/baranof-heading-600.css` | `sha384-vkroBEg6uwyd0DVRtEvotDUR8HrpWUCCWLvWZBm5b2rUklhfBMx27yzdhytRY7xW` |
| `@open-metric-fonts/baranof@1.0.0/baranof-heading-700-italic.css` | `sha384-zkCycs7RKmC/RLjK4TfBQH3LngWlgaunjBwJfkN5V+3e6+QLQ39K6eDOBoVQk5bn` |
| `@open-metric-fonts/baranof@1.0.0/baranof-heading-700.css` | `sha384-Scid2rA5JbH4oxfs92A5KuycJAcvmkJbZS0lO7ajqINtnyjMqpurVkfW9qbFBOA2` |
| `@open-metric-fonts/baranof@1.0.0/baranof-heading.css` | `sha384-XSQUQR2WXI2AgwUasLv698OEaoej3Z9/0Xd+8qeo4DrrLNLttnx60yCF5/ZHoGYz` |
| `@open-metric-fonts/baranof@1.0.0/baranof-small-400-italic.css` | `sha384-mkSTjI8itQYP91iRQ5CTCqBhPvBpb7xYftdzcCUEvej4HhW9NifJappQNgPZjQ93` |
| `@open-metric-fonts/baranof@1.0.0/baranof-small-400.css` | `sha384-U+jQpOQn41EICpy5zup/2qBxPr9ihc4KD6LJmhCRSP4zXzcnW3U1jVt5RKlAzmav` |
| `@open-metric-fonts/baranof@1.0.0/baranof-small-600-italic.css` | `sha384-Opt+dNzCmJmRT3Ul0K+acV35s0rZEunUwDWoDKUWVfyUdkTtv/ye/SsXI05+v+O4` |
| `@open-metric-fonts/baranof@1.0.0/baranof-small-600.css` | `sha384-7GNe8kP1xSyNP+qMU6Lk1AYuSZ/iXOSXKJVfa3zdxr/1Bzp0KIugTeQJ4QQnZaf/` |
| `@open-metric-fonts/baranof@1.0.0/baranof-small-700-italic.css` | `sha384-LYYm5SOSdrLl6u0epHFk00mekLJmd6KOnD03OCHBz3SfIolaIt+X67jsw/TQ6Elm` |
| `@open-metric-fonts/baranof@1.0.0/baranof-small-700.css` | `sha384-NoDjzxtEbQY3YUTj4XPkwdWXGPSlxlkXxBf6lFVFEGiEPrqeD5ks0EBdZJPhqy7g` |
| `@open-metric-fonts/baranof@1.0.0/baranof-small.css` | `sha384-yd7D85nORV0Qg//I2YxX5Q+KiGZ0a1eLmf3xccUzKsqViV/lcizh8WYe+lque6Us` |
| `@open-metric-fonts/baranof@1.0.0/baranof-subheading-400-italic.css` | `sha384-sXpiHL2KX1A3ig7Ft7AgDov69qqi+pSkJrBv8nuA7J/k71I9K12vwNjFEYprdDRo` |
| `@open-metric-fonts/baranof@1.0.0/baranof-subheading-400.css` | `sha384-CQWTZZHdULLvijt1BCP4y6Xvqm7IeDdo1EXb2hRKZAIkOGm2oD6XgGWPfG1fqgmc` |
| `@open-metric-fonts/baranof@1.0.0/baranof-subheading-600-italic.css` | `sha384-Z5uCkQexpjB9NLTxFOquqCJ04yDMugiaOpbz+UA9sZl0puuzbScH++udHlkhaLp2` |
| `@open-metric-fonts/baranof@1.0.0/baranof-subheading-600.css` | `sha384-Xst07qh4dyGG647w4SWKTyMSZ13lEMTLQ55pGUXZFS4bdqsnGDxqDCA4RZo3L4Dj` |
| `@open-metric-fonts/baranof@1.0.0/baranof-subheading-700-italic.css` | `sha384-3xuP+XiWZfkz298v61b7V70H2IySzsd7OJypyhIJAci3ZmWnNKcY5TwCW/xDe+Ad` |
| `@open-metric-fonts/baranof@1.0.0/baranof-subheading-700.css` | `sha384-GYZoxzYOk1LrdTPM9Rx7Wo2JdatLMauiVJivLVv6wC9mNyLoRviRJ1pv2uzY1Iop` |
| `@open-metric-fonts/baranof@1.0.0/baranof-subheading.css` | `sha384-s6haLJoyDx9mbyeoKQgMKULyCyR5SbQ0X5grknc/ZuupC3BJ5ukV7/OhsxzHhVNS` |
| `@open-metric-fonts/baranof@1.0.0/baranof-text-400-italic.css` | `sha384-idqi8WKXCFQVcxQ+4Ec9FpQRTvxKytPc7GcoTUMrV3ph5HJor2Byq7J+tUuAQbUY` |
| `@open-metric-fonts/baranof@1.0.0/baranof-text-400.css` | `sha384-c4z1eXR3EjtfMsBnoSv4CdThG9OWaNcGO7hm9wwDHjN94cFBKcHrrYbvFRT7sS+W` |
| `@open-metric-fonts/baranof@1.0.0/baranof-text-600-italic.css` | `sha384-2FPs8ajLcp7SK5Q4/xueEDdybcISvYFbjl5P6Yl6avvAwEOqgcmO+M4adI3rF7+b` |
| `@open-metric-fonts/baranof@1.0.0/baranof-text-600.css` | `sha384-FlzqrL5+RRBQBB5abS+dRPg+tMR9hyOvVKMRlEit3h4wdZYrsTQnBtvcnWuF4doN` |
| `@open-metric-fonts/baranof@1.0.0/baranof-text-700-italic.css` | `sha384-TmJ1vd1cU4cNI3i1a1U9kiHrbet6rPIGeTzwD6TgRH4NllbWQS+wermMH+J/M3AT` |
| `@open-metric-fonts/baranof@1.0.0/baranof-text-700.css` | `sha384-ggJNbu6PBQT/aOBe3yo511wjSehWNnkwNttRyS8/7qNoZcPtM3k9hRLb9jZ3Kyjf` |
| `@open-metric-fonts/baranof@1.0.0/baranof-text.css` | `sha384-98smRVyWCo0KbYZNAaqErMaOsh3OWjOsUdxklJGTvspeg8urvTKx4hdvYGKGCivN` |
| `@open-metric-fonts/baranof@1.0.0/index.css` | `sha384-ssz6QOi1iGPxvzSmj7pLGjAq5s4l764rd61M4QVhpSUjpovnXNXXvvYT1SOCP3wO` |
| `@open-metric-fonts/bindery@1.0.0/bindery-300-italic.css` | `sha384-G8pcClB+7rplsPBfEyrtwm/kWnLYgyG0RWQUP/klT3ZB334MOoft/qr8wVqPGSJa` |
| `@open-metric-fonts/bindery@1.0.0/bindery-300.css` | `sha384-DtjMzD+i8lmvkNNLvOaT5T0EQIyTBAM41SGjIMyyRJLZ4gayHSCRcQJcd65GGWsC` |
| `@open-metric-fonts/bindery@1.0.0/bindery-600-italic.css` | `sha384-jDUz3DYYN4fYzdGlneBU1IYaBs0zBwqN69j/LmV5jRhExq4QGm6r6aQZURF6mdAF` |
| `@open-metric-fonts/bindery@1.0.0/bindery-600.css` | `sha384-ZJdgvmNVI7uvIaWFdygmiSZOMdf/XvsI6NeJjsvTvqZtNlQLBmxlc3JMDvxopvdt` |
| `@open-metric-fonts/bindery@1.0.0/bindery.css` | `sha384-HG2u1H3/9EQZ3PcGS0ojjWQ4os97H3cSmnS4qO8ytKEDX6KNX9uAEUEd/XlxKLP4` |
| `@open-metric-fonts/bindery@1.0.0/index.css` | `sha384-HG2u1H3/9EQZ3PcGS0ojjWQ4os97H3cSmnS4qO8ytKEDX6KNX9uAEUEd/XlxKLP4` |
| `@open-metric-fonts/calvi@1.0.0/calvi-300-italic.css` | `sha384-KQ5xTiVr2awVMKT2hrDxg3cusjy9+DlwIej2IHsyWp5oWFyazo4HJjjUUv6uk5iW` |
| `@open-metric-fonts/calvi@1.0.0/calvi-300.css` | `sha384-LrqgJkc53165ghibT0ykRgRXTlCEaK2zRQImTo7a8+tF3X0vxhQVW29l91I5fyRW` |
| `@open-metric-fonts/calvi@1.0.0/calvi-400-italic.css` | `sha384-IhHPrZV+y5Pvx1sXEXsb8q2GDcS4VASddvDyKD9Tx2zlsO4f1nQ7IlB4nxEs/DX0` |
| `@open-metric-fonts/calvi@1.0.0/calvi-400.css` | `sha384-59y7Xn9WgGikirx7yjxMkjC0bQlXX0ENDEietOUCiXlyBcY2kFYDKjuexDzeSyhK` |
| `@open-metric-fonts/calvi@1.0.0/calvi-700-italic.css` | `sha384-h+IEh+Nt0LdYue9IqTFyk1Jptf9HfsdrEU/bYoGem+u5GPoIqdUGHtE8nnXrVir0` |
| `@open-metric-fonts/calvi@1.0.0/calvi-700.css` | `sha384-nmOPJa6VzsWfs/4Cj6qQVhZD7Z+pH/u0gcL4vsoc6vSSIQFCApxhDOby8tkbofwX` |
| `@open-metric-fonts/calvi@1.0.0/calvi-book-400-italic.css` | `sha384-VOx7C7ffhstYlVRp500eqZ5LRB7W9OS2N2e2OloZ9zqmT1bbqYSMWQQL8FV8Nx2n` |
| `@open-metric-fonts/calvi@1.0.0/calvi-book-400.css` | `sha384-OOjaRfM277nSE0BA67xcXoUNYcbRA3DETo8mGq13oZTMUWBuN5+D6KLZJ/lEobzN` |
| `@open-metric-fonts/calvi@1.0.0/calvi-book.css` | `sha384-kwKZAuOru6EKQtgi8d5pyk9MgPu4nj4UbylVwq5fN/p3tM2Lc6vogWP2eFiuavu9` |
| `@open-metric-fonts/calvi@1.0.0/calvi.css` | `sha384-8ujfNsAm/kckHSKZovxAI8wIQ1vlEMaFRgr9QOomb33mZYsoJBA/A1jhPIb081we` |
| `@open-metric-fonts/calvi@1.0.0/index.css` | `sha384-0LuQKhy14QUHgpdAfi4WG5JApzyMXq0Xeuy/KzSHSigzvTKRDZVN/jwm834YI6jC` |
| `@open-metric-fonts/colines@1.0.0/colines-400-italic.css` | `sha384-Xn2DUiDX9GHhoIgC+LkbIsF78mDDwj+Lwvr9T/Lkklt1P/ANzTB2kTCyZMeXhlZL` |
| `@open-metric-fonts/colines@1.0.0/colines-400.css` | `sha384-mhSl/hXchObcE1jgo0GlnM+IddXHIKoox3tjpV5R0xHLl1XUQZ2Lz1zQk74hV+il` |
| `@open-metric-fonts/colines@1.0.0/colines-700.css` | `sha384-E/vaL9HqnLQIqiSX5waKgnZgt4NTf/yJ08z3aqpQqtG7hI1C3YvtNHBfgO3be2Vb` |
| `@open-metric-fonts/colines@1.0.0/colines.css` | `sha384-+HXGEIatOMtwlOgYOvGt38KepVffeLrHdInqINlWs+/mFc3ozudgTgsFYtvT6oYV` |
| `@open-metric-fonts/colines@1.0.0/index.css` | `sha384-+HXGEIatOMtwlOgYOvGt38KepVffeLrHdInqINlWs+/mFc3ozudgTgsFYtvT6oYV` |
| `@open-metric-fonts/compass@1.0.0/compass-400-italic.css` | `sha384-qtiuaS9+Z/DGBFpjQo/rbMERRbRrclbfvpkZka8do7LHZ/2SchgJlV9EyFfJhMd6` |
| `@open-metric-fonts/compass@1.0.0/compass-400.css` | `sha384-pc7M126u0ZDXl7f42iGEeAO7zQ+y7wCYPvIrFViC7gOqS9CtFkVfjgKtXRuobC5z` |
| `@open-metric-fonts/compass@1.0.0/compass-700-italic.css` | `sha384-gn2bc+ApnQ8zMJB38O5BlZq1LgQziCURSci99RZNQcLhbAg/yTtlkdfnChM5SfWy` |
| `@open-metric-fonts/compass@1.0.0/compass-700.css` | `sha384-z0k3ruU3irM/Oa7lJlbILZj2wvknLLEJXwWLiEP8nZPRDC/5349lyWNszd/msqOb` |
| `@open-metric-fonts/compass@1.0.0/compass.css` | `sha384-2G0TJTxCaeFy9+EixJUqCiLgheM4ngjyB5452sF8k2A25CUh+Ht93MJ+lsbg2xGd` |
| `@open-metric-fonts/compass@1.0.0/index.css` | `sha384-2G0TJTxCaeFy9+EixJUqCiLgheM4ngjyB5452sF8k2A25CUh+Ht93MJ+lsbg2xGd` |
| `@open-metric-fonts/cuprite@1.0.0/cuprite-400-italic.css` | `sha384-Lp+V0ZvIG4RLaD+6FTjrt/zNMWSoHZ1S441j8ODZZNb3WukL/h68djp2tv6yukeV` |
| `@open-metric-fonts/cuprite@1.0.0/cuprite-400.css` | `sha384-lfsmK3wUAmqNRO4DQgStWSfB5wbI8+W7gSOR0kOlEN1LpU9y3e6fVDdNMxgKvclU` |
| `@open-metric-fonts/cuprite@1.0.0/cuprite-700-italic.css` | `sha384-L070N4prsCfEfc2xk6/Dxcm+9bHHTes5QD7mBABgfBtKLCm+vB+hHrr/plNYJEgu` |
| `@open-metric-fonts/cuprite@1.0.0/cuprite-700.css` | `sha384-nYY9HnrHbuBMppKGAKye1vO0sn1sxs9f/U89ciVj4TsF73vsoPavKbOfI0nfRmgV` |
| `@open-metric-fonts/cuprite@1.0.0/cuprite-display-400-italic.css` | `sha384-Ym/v+AEHtXCKot8GY1Y07F/mBnXWYKjdrI+U4ekTJVHfLx0+A5sXLbAdC3e0KURt` |
| `@open-metric-fonts/cuprite@1.0.0/cuprite-display-400.css` | `sha384-fcVvFfDqYINHle4buIJkQjIS6Q9QPX8crGJDMsfoAN0s1sMuvL8Dzg81hw+XYv+7` |
| `@open-metric-fonts/cuprite@1.0.0/cuprite-display-700-italic.css` | `sha384-bGAzZAY9KKn6TFjOa8kvAS5tGtpjiOrr1Cik+5rJ6/z7l2ZchIFB/R27er6B+NCK` |
| `@open-metric-fonts/cuprite@1.0.0/cuprite-display-700.css` | `sha384-a2Jz9CGwrxVR6Aw3SMTp0kXESv1A+4NXAckuQmpIlpYrkMkiYav3Un15uKL0qoGA` |
| `@open-metric-fonts/cuprite@1.0.0/cuprite-display.css` | `sha384-75+Oetj4cG5fEMAjizORQjr6xHV9VdCbUZ+fB4N+Z9fJwejchGMglCHUPnZDFXeB` |
| `@open-metric-fonts/cuprite@1.0.0/cuprite.css` | `sha384-aBAcZdaKN0XZeN4Bd7WAk3sPe9kdIC4sWRNR6/MMVsV+NSHI7AosOI3a8c3QKOgt` |
| `@open-metric-fonts/cuprite@1.0.0/index.css` | `sha384-ffgWjYuZQ1p30TipWm9Bxn5bIGwUgtx2wwbinxaPW4jLpzL3tpWqaDY+oJDNWcJ8` |
| `@open-metric-fonts/ditchling@1.0.0/ditchling-400-italic.css` | `sha384-t1FQyuxmFKoIMPxeoIqWqAzRtw4i/NDRPPQ0yVRWngv/+hRbNLnpDrHboKK1pxmE` |
| `@open-metric-fonts/ditchling@1.0.0/ditchling-400.css` | `sha384-JBnBt315ew6G3ncIi5sWOZ6sClzW6OeFa/7027anOP9M0A6/hGIQJcVb0H0gNP2A` |
| `@open-metric-fonts/ditchling@1.0.0/ditchling-700-italic.css` | `sha384-TPDZ+I8/cu04Rsd9ADmQdNePeAZ5MO6fMY1qanWw+0kzjCrtF/GG1PIjKJQ4x5h5` |
| `@open-metric-fonts/ditchling@1.0.0/ditchling-700.css` | `sha384-GNpbOBAnhl9yGqmx0kfja6gTfgOFx/bcPVh6YSkEE+aBcSGU7OdOIu54tbRxFnNa` |
| `@open-metric-fonts/ditchling@1.0.0/ditchling-titling-mt-300.css` | `sha384-ITmMR8w1ubBbZRK9yndiKwjEX+MSa6NXg9aDxUJmLBR+d6Mfyf9/lUxMMyKuKuc3` |
| `@open-metric-fonts/ditchling@1.0.0/ditchling-titling-mt-700.css` | `sha384-JwLaxQhSwMVYfLfREB7mlpSiUNT3irBVS1BImy7EJk/p4ArWVWc0FEvJnY6tskaR` |
| `@open-metric-fonts/ditchling@1.0.0/ditchling-titling-mt.css` | `sha384-5LR3+gTQpC9LYn4M0UkhdlHWdrAkIT11bp6eI4xLr0D1biwAqffB52Fjdem59gE2` |
| `@open-metric-fonts/ditchling@1.0.0/ditchling.css` | `sha384-sAFxNGkvrGKthr4FE0GPiC/s7gqzJELMn/8vOLHY/8hQLioMjbuv1YRwNe18PLi+` |
| `@open-metric-fonts/ditchling@1.0.0/index.css` | `sha384-tS4YAhFid7yrWLJ++3xjioML+G9qx3arqZb2YbvOUk8c1Fngr4drSs/K4nWufQ7W` |
| `@open-metric-fonts/dune@1.0.0/dune-400-italic.css` | `sha384-2gqozE+oZRUdq85OYYn2uav8MaY21CeLsClcYZwJaLFDAYwxskJI9XWtoAQP1GQz` |
| `@open-metric-fonts/dune@1.0.0/dune-400.css` | `sha384-kWk346BaYoE0UIW6wK1KgohFEJWQ3ikGQeF5xqrPXirpH18PhNsyGiD8VeG363SI` |
| `@open-metric-fonts/dune@1.0.0/dune-700-italic.css` | `sha384-QDHaFBidYziKTNMpE+esygIvKEBR0cCDnqeuj7UbLvNgDE5rd+RBbUPFsV1FZ3HO` |
| `@open-metric-fonts/dune@1.0.0/dune-700.css` | `sha384-4bBy/3kt/V8HQrFPx+TCu0OyrFIIvdmM+hJKikZk67wrg7U5Zx392U7Fjn+8Gxfe` |
| `@open-metric-fonts/dune@1.0.0/dune.css` | `sha384-B6ms89CKXmbXJb0S9IAzRx10A/UeIAR/ss9IcXKmHo3c6rJfUs8Ox4tbIdXYgZTK` |
| `@open-metric-fonts/dune@1.0.0/index.css` | `sha384-B6ms89CKXmbXJb0S9IAzRx10A/UeIAR/ss9IcXKmHo3c6rJfUs8Ox4tbIdXYgZTK` |
| `@open-metric-fonts/easyhill@1.0.0/easyhill-400.css` | `sha384-l3nid4Y3NuJcpay/khnZoEcPX6eQEIEIu4h2TruS8vd3SwvLMgTM7QbJ9Msi+xqY` |
| `@open-metric-fonts/easyhill@1.0.0/easyhill.css` | `sha384-l3nid4Y3NuJcpay/khnZoEcPX6eQEIEIu4h2TruS8vd3SwvLMgTM7QbJ9Msi+xqY` |
| `@open-metric-fonts/easyhill@1.0.0/index.css` | `sha384-l3nid4Y3NuJcpay/khnZoEcPX6eQEIEIu4h2TruS8vd3SwvLMgTM7QbJ9Msi+xqY` |
| `@open-metric-fonts/faience@1.0.0/faience-300-italic.css` | `sha384-F6rPKJB/J9T5O4Ooz4tgnpEJz964swf5i2NX7UDmDfSRsoyiuXKOdVqMPdFkzDmN` |
| `@open-metric-fonts/faience@1.0.0/faience-300.css` | `sha384-36JJNOIUt9w13LOavMMdOhcRuaRw2+5Ym2L0/N4lA328sdaOQrc8kzq8SWRjaGLO` |
| `@open-metric-fonts/faience@1.0.0/faience-400-italic.css` | `sha384-26lMnuBdJSSXcqage372+DnO8t7iTpp4F2PXH/BFdLfPGrMmqUpPn2BEwMHbMGId` |
| `@open-metric-fonts/faience@1.0.0/faience-400.css` | `sha384-HvGOy3J5xw/w81v6tM+CR60p9na1nAeeUyCe3RFpToqnlsja7ArXr7M1187shjj9` |
| `@open-metric-fonts/faience@1.0.0/faience-700-italic.css` | `sha384-4kWFB/swKUwFZr2pfgnWqHG3RlmJEnLRuWRfterFGOu9vt8XMF8Z1knbLD7OHR5I` |
| `@open-metric-fonts/faience@1.0.0/faience-700.css` | `sha384-+KuNpGyvJMPBOUvzXN7z21PG8TfTTyufT/OU8D/UCUdn8j/qwinwuThGtlDeul3x` |
| `@open-metric-fonts/faience@1.0.0/faience-900-italic.css` | `sha384-WoyuLPY/qkdMdhjDCH1LZDTriUHiT0L8GtPJaz9lBHG7DrZkTDqcPbmnJhlONsDt` |
| `@open-metric-fonts/faience@1.0.0/faience-900.css` | `sha384-IhtWWsc8l5L4xrCAtk/qAt98XWfNE2rvP304Ku27iCvORbT9qVkFSY4ZcWiDtxT4` |
| `@open-metric-fonts/faience@1.0.0/faience.css` | `sha384-tou4PWv57rx1DG6ig8uVFxUclHLDA0ex+eG7C6NriI82BxatBSw1WUzYOMYvfA8G` |
| `@open-metric-fonts/faience@1.0.0/index.css` | `sha384-tou4PWv57rx1DG6ig8uVFxUclHLDA0ex+eG7C6NriI82BxatBSw1WUzYOMYvfA8G` |
| `@open-metric-fonts/fidela@1.0.0/fidela-400-italic.css` | `sha384-5/btjUCHJ3wH46VLi+xY9xJoz89xphGgpV9mmDguzr3OpLBzCC/6YsuuseYD7M9J` |
| `@open-metric-fonts/fidela@1.0.0/fidela-400.css` | `sha384-9rEFD1/HLKvCqY+riB/DgsbykOZ9/kdkl6ptEttjstuWbCp3G4i9k1OPREp60atw` |
| `@open-metric-fonts/fidela@1.0.0/fidela-700-italic.css` | `sha384-fl4J1NPZAoAm0R+0ysrhE+VDeRCGnFLnKQkX4G7EFo8RLqnFzP9IQyvFiQWl/vsJ` |
| `@open-metric-fonts/fidela@1.0.0/fidela-700.css` | `sha384-FoM0d6j22p4xgHo2H4fcSKDEsF/RIolLBVdJ9FxIDl0Sy52/YjCXqRwvoECLOtVe` |
| `@open-metric-fonts/fidela@1.0.0/fidela.css` | `sha384-uJ5Tbm6lWyWJgN5MZyPQCSNePw1aOyk/1JKhOz7ZdHo5zf+2FX+8kwGsB1aIwIV/` |
| `@open-metric-fonts/fidela@1.0.0/index.css` | `sha384-uJ5Tbm6lWyWJgN5MZyPQCSNePw1aOyk/1JKhOz7ZdHo5zf+2FX+8kwGsB1aIwIV/` |
| `@open-metric-fonts/flourish@1.0.0/flourish-400.css` | `sha384-YPjPpWEREkcGrSmLz3mehZ4AP27xUyeTuNAdv+CLs9gQAYcO7Qrg9OMPIRPKA6Xm` |
| `@open-metric-fonts/flourish@1.0.0/flourish-700.css` | `sha384-RuLqPWxCNkeymb+MKxM9oJJB7FzI0gQlgaHCWEski2EnVd35jZ2TDd67WiGdhNc6` |
| `@open-metric-fonts/flourish@1.0.0/flourish.css` | `sha384-rRgV8K6FKjIuh332drYTtWSRBlSzr33ye9AzXOtze+WpzOHozt5jAxMdMoZvN5I1` |
| `@open-metric-fonts/flourish@1.0.0/index.css` | `sha384-rRgV8K6FKjIuh332drYTtWSRBlSzr33ye9AzXOtze+WpzOHozt5jAxMdMoZvN5I1` |
| `@open-metric-fonts/glade@1.0.0/glade-400-italic.css` | `sha384-Puo2Kw/ynx3ZZWqrKSgUKdWKiQclpnkRgGVh58Y36kfV010pQ4fyMF/o8tRMC5q9` |
| `@open-metric-fonts/glade@1.0.0/glade-400.css` | `sha384-akjB8/P1meU+hdhxhw5yE7MW8PD3qXwWazIyzK9vimXFV9uIHa+AECCJwWGYMJj7` |
| `@open-metric-fonts/glade@1.0.0/glade-700-italic.css` | `sha384-mQVaJktzfITvLXyPruFOK93+8Z+JxuDM6kh7HzF+J+WWdYX+12PSjR3/F+GXYfo1` |
| `@open-metric-fonts/glade@1.0.0/glade-700.css` | `sha384-J2Mq/FGOo0THS1PNos/HAYG+jEN0IeHD7pnRZF3g95il6xvNxXvoggioQaut/cPH` |
| `@open-metric-fonts/glade@1.0.0/glade.css` | `sha384-2XUWx7pRbVrmTUM7vEZDpbbZEHynyH+uNRMTlCQHxTYi5jY4PTZCZM/Ax4IdrFOW` |
| `@open-metric-fonts/glade@1.0.0/index.css` | `sha384-2XUWx7pRbVrmTUM7vEZDpbbZEHynyH+uNRMTlCQHxTYi5jY4PTZCZM/Ax4IdrFOW` |
| `@open-metric-fonts/glade-pro@1.0.0/glade-pro-300-italic.css` | `sha384-PueeYJ3w2keI67hJb4v2oQC+8Z9Den6gVG//XhM/72bUS5VO6NJgLvFUtFdjdFsG` |
| `@open-metric-fonts/glade-pro@1.0.0/glade-pro-300.css` | `sha384-2PyGyBo9kNnnaRp963zwuwRynv6RAxKz2g90EaEv6v6TfpAz+2675h3G6xf5bpn+` |
| `@open-metric-fonts/glade-pro@1.0.0/glade-pro-400-italic.css` | `sha384-Pf/Z+zy0JbxeGjzyO/hL3CApPnRiQmZy4Hrb3tJIznqNJWeLyMgC8bss+2LW1n8X` |
| `@open-metric-fonts/glade-pro@1.0.0/glade-pro-400.css` | `sha384-6yDj5YlkAiODCpWBhAs2MDotZ1TexiCdkW3gQu02jB14eGGdPTYurGJUs2+FfnoQ` |
| `@open-metric-fonts/glade-pro@1.0.0/glade-pro-600-italic.css` | `sha384-AAhSorf04pvHsC2Zf7oE+ZnTfnaIfMgy7ODEzVsCja3DPoTQ4kqetUBuGzqtZ3lg` |
| `@open-metric-fonts/glade-pro@1.0.0/glade-pro-600.css` | `sha384-q6VaAK2ohxLp9DGHdPU+OIwp6oFeatK/5RT3GSiKCCRaEMrQxPvi9cs2uS+8Ckg+` |
| `@open-metric-fonts/glade-pro@1.0.0/glade-pro-700-italic.css` | `sha384-THq7VxezEPqP5fxKCcQtIFpLYAHbn2Aqd03gBzDrj0YCT82c6gycsb2Lw/HtWto+` |
| `@open-metric-fonts/glade-pro@1.0.0/glade-pro-700.css` | `sha384-Rxrg6n3A5ZwyPr10Q5jea5TinssCT8OJKxM9qWVKYosibKhR/zsL+EkgXGsa0LMW` |
| `@open-metric-fonts/glade-pro@1.0.0/glade-pro-900-italic.css` | `sha384-XkgAbMl6tAwAeX1YLqosYonkbCth/jWdsmGAbgXTx9rvqQQgEKPSOZFA69MaZDJU` |
| `@open-metric-fonts/glade-pro@1.0.0/glade-pro-900.css` | `sha384-t5os0Op+iVhSn3PICDBdomKdgvsGerE175CsjzRS8GGcRNP8+ri1pij8KB5LTbhm` |
| `@open-metric-fonts/glade-pro@1.0.0/glade-pro-cond-400-italic.css` | `sha384-qjDJ7HpYyUMy0mIsjAdZ1ZI6x25ByhZOwdCzva+xGZbe15zicDQIe7RCJP6THKj0` |
| `@open-metric-fonts/glade-pro@1.0.0/glade-pro-cond-400.css` | `sha384-FbB6gsJCWhbtQSBmJGbaLxq3sH2df9phUA+Qr6OAuQsXgDrDzHR2OL5KrxUcJTTo` |
| `@open-metric-fonts/glade-pro@1.0.0/glade-pro-cond-700-italic.css` | `sha384-kK0zETiXANYr3+cjbsHYDuEUBdTAHd7tF0cqbc17TYYGoRodDCDVN13Yn1906lj2` |
| `@open-metric-fonts/glade-pro@1.0.0/glade-pro-cond-700.css` | `sha384-T6B+gvGKJz8OMet2i8+S3JnLtmFLH2L4n3NJHFafGUlp3zOzEZtR5h3CwzuuVj5M` |
| `@open-metric-fonts/glade-pro@1.0.0/glade-pro-cond.css` | `sha384-7XIy1GplUk7cBwDpZ6EbTMY0lXT5aP4opGjz7xpWDwWGIrh8Q+CsL221bTGCj6wt` |
| `@open-metric-fonts/glade-pro@1.0.0/glade-pro.css` | `sha384-Wd7VCzwvYHXZ/vrKZb7FP9Joi8SvC3iuAttVpQPBxjxcS5C86eUw/rQCPfwMgSKy` |
| `@open-metric-fonts/glade-pro@1.0.0/index.css` | `sha384-LMIWyNA79F5FlwDstLbJDkFOICZ+GOY+xccU6qt5g0tipOqlSvXrnhW3l722xOJm` |
| `@open-metric-fonts/gleis@1.0.0/gleis-300.css` | `sha384-eSPD+pzAYyw6/OXb/5RDAudha2O8ZxZcsBCg2mcuoZmgEip7P+grMfDqfOe3BE7e` |
| `@open-metric-fonts/gleis@1.0.0/gleis-350.css` | `sha384-bWfA0EsObOeyo1AI2L2jmULuDT/BGcCJzgIeUvR83im1cy/5C6wCSQNMZdW0WejM` |
| `@open-metric-fonts/gleis@1.0.0/gleis-400.css` | `sha384-cZ5OCDCsoYKfIB4FljPN3OEvvDzVDXFeVHwt0s2pBFE6I/aLu3e6FVkPGpVW5bNa` |
| `@open-metric-fonts/gleis@1.0.0/gleis-600.css` | `sha384-gygMIRfbDfAHOvapkpYzVIMhbKQjIFxM4x9n/Ij+1CkPvlZb4fH19UzrgPiqwKgy` |
| `@open-metric-fonts/gleis@1.0.0/gleis-700.css` | `sha384-qv1wvtHcC1RfiBoaLVKieQNkEQEqcBMYR41sCCOxSXGT1+b/3XTle7ckJz6uJ+4e` |
| `@open-metric-fonts/gleis@1.0.0/gleis-condensed-300.css` | `sha384-0RlyIMJf8q6mNwGCCcFfZf+trFvOId+D4SQxXjlgeqeA87h9Lxy6yiyLGC7EgNZ4` |
| `@open-metric-fonts/gleis@1.0.0/gleis-condensed-350.css` | `sha384-ZATbKRi4druh9R+ahtizmNyTNgJb+vme2bRkmqPhtauR1/QkdMOMM6dpbEM1EGuu` |
| `@open-metric-fonts/gleis@1.0.0/gleis-condensed-400.css` | `sha384-s/2+Xgu5LLboi5ePe+zoiWmwUZEboHRsfCG0fKror20QHHflxLCdpuXUgWRY45LR` |
| `@open-metric-fonts/gleis@1.0.0/gleis-condensed-600.css` | `sha384-oWkzdmuxp+EQQWVLR2IKKtmocIi6H/+7hCABlZOpPmeCmd+ZQpofVRDc8McvsqQe` |
| `@open-metric-fonts/gleis@1.0.0/gleis-condensed-700.css` | `sha384-+TFiGyCKw8HeQUL+2ohwxnvCHKdJCjX0Dr2NMOclm/VpkiR8lAHDdPo8XL7ba6AI` |
| `@open-metric-fonts/gleis@1.0.0/gleis-condensed.css` | `sha384-bV5JV7hPGVsLtzhsXUqP/+FPZnxgjc5Ddj9/XIHQHnn38GMW8X4xLGt3Sdu6Zrvj` |
| `@open-metric-fonts/gleis@1.0.0/gleis-semicondensed-300.css` | `sha384-CyRctC2kjTT3g3I4M7A1jctZ6QVfN3+wAeQv4eikBi/+Ob8TFbBDT+ddKJQAfxKK` |
| `@open-metric-fonts/gleis@1.0.0/gleis-semicondensed-350.css` | `sha384-wsno+3i36RuwuWKTpTA5bD0Y7+wXJ1C5X3Y6zNKSMUAcd4vOvb9nw/eT99pbwxn9` |
| `@open-metric-fonts/gleis@1.0.0/gleis-semicondensed-400.css` | `sha384-HqobCngGLphUMItqQ0jofIXJ862C3qhtRcRfBm5mJuISFJxKZYZxTzTzm34jMhBo` |
| `@open-metric-fonts/gleis@1.0.0/gleis-semicondensed-600.css` | `sha384-hp34hX1C4eBGuw55CC7GLKSxLajNDW4YG/USHTvbnjojyR6CJCE3fB6FS84Ed4OQ` |
| `@open-metric-fonts/gleis@1.0.0/gleis-semicondensed-700.css` | `sha384-gPC6htyw6lA7mh4vO6DqpGfol2VOxoJfw+bGp6lJexaDjcTcwMu5nG056ees5VO2` |
| `@open-metric-fonts/gleis@1.0.0/gleis-semicondensed.css` | `sha384-HfZVJilHXaVwPubRxr4DIo5l3FYKPO871JuVQilGexH8LN01OU4buqUZO2+kS7Y+` |
| `@open-metric-fonts/gleis@1.0.0/gleis.css` | `sha384-sclOFB58qHhORVYIID0ZUMklDwc6tuMlqWU2Nmz/ikrZ4mkCprFvJm7iMtpsLNwQ` |
| `@open-metric-fonts/gleis@1.0.0/index.css` | `sha384-uqb0WT0c/mPnLP+uZOnR2QX4CMV+0PnxUCBe1c+eFGHGf/EYbnn+W280XTNkAXnk` |
| `@open-metric-fonts/hornbook@1.0.0/hornbook-400-italic.css` | `sha384-NfNKekAV383mhwbp9k6VzL4L91Z62mHSSRH5iC+RtZVfusSAhbxTd3HxWZZsBzA/` |
| `@open-metric-fonts/hornbook@1.0.0/hornbook-400.css` | `sha384-T3thS8/9Wy2MnIVG78lPW2/bN/koTHi+lQIt54tXv50ANrMUG1FLiRt7zhHbYQQh` |
| `@open-metric-fonts/hornbook@1.0.0/hornbook-700-italic.css` | `sha384-A7So3Ou7ILyy0dObaT1TIDDMfg+YHeBGJ2PwbcCmT5M5u5K69I0NC7AXMZ6iVkka` |
| `@open-metric-fonts/hornbook@1.0.0/hornbook-700.css` | `sha384-pq39H/nPKxHJGGdbO4AUIQrs8f0aX/ciCwnAPxXwWBTHvoa8SyFAV2h8zPvoPrBQ` |
| `@open-metric-fonts/hornbook@1.0.0/hornbook.css` | `sha384-DG6PNcBiilHSBTIstBN+wKz0+8+D/XSXkBsTi8CU9X9Bc4w6Y8JhTiONmW99gd94` |
| `@open-metric-fonts/hornbook@1.0.0/index.css` | `sha384-DG6PNcBiilHSBTIstBN+wKz0+8+D/XSXkBsTi8CU9X9Bc4w6Y8JhTiONmW99gd94` |
| `@open-metric-fonts/lagoon@1.0.0/index.css` | `sha384-atDW3q5kQGnVatpc+AY64xVFsLX7f/iaYsvQvfzzXMLX3Oy8a24ryZZMGQkDO7fI` |
| `@open-metric-fonts/lagoon@1.0.0/lagoon-400.css` | `sha384-atDW3q5kQGnVatpc+AY64xVFsLX7f/iaYsvQvfzzXMLX3Oy8a24ryZZMGQkDO7fI` |
| `@open-metric-fonts/lagoon@1.0.0/lagoon.css` | `sha384-atDW3q5kQGnVatpc+AY64xVFsLX7f/iaYsvQvfzzXMLX3Oy8a24ryZZMGQkDO7fI` |
| `@open-metric-fonts/leyden@1.0.0/index.css` | `sha384-ABEXi5yE6zcpFG21bzvVdCVFMKLi2cB30x6JlLHSCSrS5qw6AGDR+KXxadeoF1TQ` |
| `@open-metric-fonts/leyden@1.0.0/leyden-book-400-italic.css` | `sha384-FMgUUnqrf2pSNZGwU9x01Hx+iAlGzkCQtZDkj1UNFtedaWcfF39MmE9ou2MFePSn` |
| `@open-metric-fonts/leyden@1.0.0/leyden-book-400.css` | `sha384-5IDgXncD3r5wgEfkOgai6MT0L0zUGhU8cs2XdxYqvTkNfYV8ldjhYWiH8oZI+ADF` |
| `@open-metric-fonts/leyden@1.0.0/leyden-book.css` | `sha384-7THah++3/2UUYvYKKSaZtImrYY6nWAJk4MGs/0pppl479aQmdpB/JDXypa2A+g5G` |
| `@open-metric-fonts/leyden@1.0.0/leyden-demi-400-italic.css` | `sha384-hij+1buVp2vq1tZ7N7FFGaOK4cQkt+Zr5uDND6/JAXvDlsHWph2QyUbTv35hvIxC` |
| `@open-metric-fonts/leyden@1.0.0/leyden-demi-400.css` | `sha384-bWsu0VNCOc8GBBHrlWhh4/SbnJ8a6UcoI7kgFOnoDH4K3IgTurn6n372oFIiE+Ci` |
| `@open-metric-fonts/leyden@1.0.0/leyden-demi-cond-400.css` | `sha384-faC6upUaJSgrI59tKg8jH9SPAOCM4Lq48RICUyc+/Ha9VBFINfx4hyp0uONRDQd9` |
| `@open-metric-fonts/leyden@1.0.0/leyden-demi-cond.css` | `sha384-faC6upUaJSgrI59tKg8jH9SPAOCM4Lq48RICUyc+/Ha9VBFINfx4hyp0uONRDQd9` |
| `@open-metric-fonts/leyden@1.0.0/leyden-demi.css` | `sha384-0hPLOyGs3X9Yf1EK8TXtpOBPZN/JcZkr3XzjXcJSIpxrvnAblc27HFE4hh5OndLd` |
| `@open-metric-fonts/leyden@1.0.0/leyden-heavy-400-italic.css` | `sha384-w+UQOOQtItMzxhNWKY3YyBKvTYqkP74OZdRSvVHhKqQGqV29robJwacIWPL8hyMf` |
| `@open-metric-fonts/leyden@1.0.0/leyden-heavy-400.css` | `sha384-XluXtkIGtP+oGV5Nzqecp5lQP/RwYDRQ8ZBvag9TNt/tUfIzXL9JOkEmZpjq3mVl` |
| `@open-metric-fonts/leyden@1.0.0/leyden-heavy.css` | `sha384-zkcaUNgb7rP83gVcUBUAPnj9g42K+UhJ8CyQ37b0B2yoP9a3wWUZjcscg5egtFzD` |
| `@open-metric-fonts/leyden@1.0.0/leyden-medium-400-italic.css` | `sha384-mjOgfjLK4jqQRPoCmmur/mFvMeOLL00G3m94cGNTUdaTSJC7p10BNZJ6QllQ5a56` |
| `@open-metric-fonts/leyden@1.0.0/leyden-medium-400.css` | `sha384-+be/xW9NhLiKo7bI3mWOjNskCeLnpQC3ApVjQSsQUbcsEfZGl8oXYuLw77xui/BB` |
| `@open-metric-fonts/leyden@1.0.0/leyden-medium-cond-400.css` | `sha384-wc3D+hPS2k3+975QdZKjpxYns32SAiQ5wxBsI9BRKqisScMaV4Bcu6nMwQtie0MW` |
| `@open-metric-fonts/leyden@1.0.0/leyden-medium-cond.css` | `sha384-wc3D+hPS2k3+975QdZKjpxYns32SAiQ5wxBsI9BRKqisScMaV4Bcu6nMwQtie0MW` |
| `@open-metric-fonts/leyden@1.0.0/leyden-medium.css` | `sha384-TOYaKge9g5O2pXrXlCCJL/H7JjZJTRe9uemu9OOGVerFXrACR8DBB6mbQ7kCHqpo` |
| `@open-metric-fonts/lintel@1.0.0/index.css` | `sha384-fb2SmIDmL54mQ56Qi4qr0DZWu8yIUNBdNx0wG7OnRKLELiut8pF9SeYYa0N7CA7J` |
| `@open-metric-fonts/lintel@1.0.0/lintel-300-italic.css` | `sha384-6evgsOkV4AE8OKDni1M2+iUpe/l8svuHUAbN4fZzottdQ650uCgihNgiWaketSJN` |
| `@open-metric-fonts/lintel@1.0.0/lintel-300.css` | `sha384-NhuEwzbklNkvdBTvBpjTy02voiiyvxVQ7Jre5eZ72C2DAWQA+d3Ten0il4EJPaRa` |
| `@open-metric-fonts/lintel@1.0.0/lintel-400-italic.css` | `sha384-Eg1UyTRsWo/Io/Qw+bRTBG2vcHF7QB022erWi2HEwB9k1ztOWuHrFRu8agMt0OTa` |
| `@open-metric-fonts/lintel@1.0.0/lintel-400.css` | `sha384-VZlE5mak0E4rGUJFnfvTbNbxDAQuck9oqMTPfE9QHovFUE5z660o3a4unHcQzdBJ` |
| `@open-metric-fonts/lintel@1.0.0/lintel-700-italic.css` | `sha384-rEijet/CxdtvKYs3STSxO0ZIegHbzxJCHEPia0uy9Y4Eg/vhohfCcBOExMBXoEs9` |
| `@open-metric-fonts/lintel@1.0.0/lintel-700.css` | `sha384-PQ7yUmQEZ+9gWwDWnIYJFN44Ru8rHUdBA1hDLvEfHgUt88LRfu0TPHtkQCYvo2HQ` |
| `@open-metric-fonts/lintel@1.0.0/lintel.css` | `sha384-fb2SmIDmL54mQ56Qi4qr0DZWu8yIUNBdNx0wG7OnRKLELiut8pF9SeYYa0N7CA7J` |
| `@open-metric-fonts/loggia@1.0.0/index.css` | `sha384-sqB4DeRYQlrSj8nbqClzzQjiIf0PCOKpXDoqErxgzBvxi/TpTyeG4lpkXGeaZS6l` |
| `@open-metric-fonts/loggia@1.0.0/loggia-400-italic.css` | `sha384-UR1yLXEfCvHNZEfjxquNbRYd4/VEuZzym06v/GNpe8kX2cs5AqDCJ5OrgNCH8+fS` |
| `@open-metric-fonts/loggia@1.0.0/loggia-400.css` | `sha384-SuAxqLWjyWfZ5WK3QyqfnZYC/lsrHo8G876frpsnJNLXmSmdfEH7mY852lf7e/Pw` |
| `@open-metric-fonts/loggia@1.0.0/loggia-700-italic.css` | `sha384-wDhV/MiZoBHbB3sZwogwEG+blO9y9hZaq4vofMqswq8mr3Fya9xiXZ0JR0QyjfCK` |
| `@open-metric-fonts/loggia@1.0.0/loggia-700.css` | `sha384-R+vIzpqGoLy9qIa+oKCD5behp/lYhBrzQwZj6W7oKRGGMS93/un4lZIhfzM5Bfr9` |
| `@open-metric-fonts/loggia@1.0.0/loggia.css` | `sha384-sqB4DeRYQlrSj8nbqClzzQjiIf0PCOKpXDoqErxgzBvxi/TpTyeG4lpkXGeaZS6l` |
| `@open-metric-fonts/mangonel@1.0.0/index.css` | `sha384-ckWlZ8Errn+dazFN+9A/IoaN4SINEgUq8Wa/aFUiaeOnUHh/w0C/6y7p5128uJSl` |
| `@open-metric-fonts/mangonel@1.0.0/mangonel-400-italic.css` | `sha384-s9rnFz2dmfOHBZYbBEt3r95PJBv6j2CtQ9wsRqHPigqF92KQrq62bRHWVOvJYTYR` |
| `@open-metric-fonts/mangonel@1.0.0/mangonel-400.css` | `sha384-+lzcN31+8Gt1pQCqjzobDcg5xAKDPyn1qx09uS59ypg+PE3dZwumzqvog4/Dfavr` |
| `@open-metric-fonts/mangonel@1.0.0/mangonel-700-italic.css` | `sha384-UvCH/ysVnjtJMpDkFYDQCNtkA0McP4n5M5gq3HICxcrK8skDDHu8MaUOeB1mOn1G` |
| `@open-metric-fonts/mangonel@1.0.0/mangonel-700.css` | `sha384-qlimfx8ggGlagjj1ZYFABhuWROCOueO1wfA87Um/fooKeMzb5cdFOH/cHn+/+AvV` |
| `@open-metric-fonts/mangonel@1.0.0/mangonel.css` | `sha384-ckWlZ8Errn+dazFN+9A/IoaN4SINEgUq8Wa/aFUiaeOnUHh/w0C/6y7p5128uJSl` |
| `@open-metric-fonts/marquee@1.0.0/index.css` | `sha384-UdVcLn690W+DJY8VTFBw2RHdf39thRS6Qbv6uGsq8xicWi/KuH1ZphrDXPrG4AcV` |
| `@open-metric-fonts/marquee@1.0.0/marquee-400-italic.css` | `sha384-csO24emc66gyYIalR5SV3yxo6RsOSwT6vYy2txGSkPWXtvm2i88MB7TCj9uX9jgL` |
| `@open-metric-fonts/marquee@1.0.0/marquee-400.css` | `sha384-M3+z0mPO73We34+9HtXsWzwDYW1Tcveeu7Nxtnmb6WM/mgPg2A9yfwLiGqM7UfTL` |
| `@open-metric-fonts/marquee@1.0.0/marquee-700-italic.css` | `sha384-tuM2M+LjrVq/YXW7F0CuaUzMdQ8BNgWlJZoFzgbg9zgiwry4Exz1bTX/UBFl6qIL` |
| `@open-metric-fonts/marquee@1.0.0/marquee-700.css` | `sha384-SM18zN5aGzxIyunah8lDQb3S0j2JyUac0RU+LCl14LQnoiFhAmKi9eIfLddbCi3f` |
| `@open-metric-fonts/marquee@1.0.0/marquee.css` | `sha384-UdVcLn690W+DJY8VTFBw2RHdf39thRS6Qbv6uGsq8xicWi/KuH1ZphrDXPrG4AcV` |
| `@open-metric-fonts/morrow-mono@1.0.0/index.css` | `sha384-QAR/BLOZiyoyWfGIM1KM7kVFRK4K3dF199S+n9FqxB2n+MNzjeyKlvl/eoEcg4i7` |
| `@open-metric-fonts/morrow-mono@1.0.0/morrow-mono-400-italic.css` | `sha384-4+HIbswRn4JR75MxLDjN8dY12S0F5ZxecC6PyeGhcyOk93OZeSsO+Yfn1kMi931q` |
| `@open-metric-fonts/morrow-mono@1.0.0/morrow-mono-400.css` | `sha384-1slBcjQFnrFBPOdVFgVTw18+S87vBCwOfvHTW1p/gdkakchSD7A8vz+7iPOgyHGt` |
| `@open-metric-fonts/morrow-mono@1.0.0/morrow-mono-700-italic.css` | `sha384-zVcTOj6lEVc5bO7nPKNOwBIu1O7jNXI/Sqf+Y3OwYo4h2EZQS09t0fPfpec38Hi1` |
| `@open-metric-fonts/morrow-mono@1.0.0/morrow-mono-700.css` | `sha384-RCsziiJuDZqMeJSZUppci8KOnDSGmu/M8CM39To/sy4vUK2INnn+Z/tkwqV6A3US` |
| `@open-metric-fonts/morrow-mono@1.0.0/morrow-mono.css` | `sha384-QAR/BLOZiyoyWfGIM1KM7kVFRK4K3dF199S+n9FqxB2n+MNzjeyKlvl/eoEcg4i7` |
| `@open-metric-fonts/morrow-sans@1.0.0/index.css` | `sha384-uYLpKR3Q28poqIhVZj7UxoxYpHH+CIigGOUwopPbVr1tJkSskZ4wmU4pe1Yg0JoP` |
| `@open-metric-fonts/morrow-sans@1.0.0/morrow-sans-300-italic.css` | `sha384-agf+NBnOz+rvFWYipfyw5pGx1RJThxq06yZgJSM+Kl4W5/8WBVvCfxyCpSvB7QuH` |
| `@open-metric-fonts/morrow-sans@1.0.0/morrow-sans-300.css` | `sha384-wF0Y5iRGl+5eoUoMZcBS344eHCI7N5y4pWVSXBVka5E4Qi+REfnMesY+3jvVGPag` |
| `@open-metric-fonts/morrow-sans@1.0.0/morrow-sans-400-italic.css` | `sha384-IQc8IegrVQqDH2qQsiVJVY6fecQWS1gbSBRGuvFP4g3iWtaoMCXsnc62Nrzicl7z` |
| `@open-metric-fonts/morrow-sans@1.0.0/morrow-sans-400.css` | `sha384-roPoCLYHscV9nK/X90KGtsgsvM5XCKt4U2Lm7CNaV8QwMfTo9/vgBwpYW2xltCdq` |
| `@open-metric-fonts/morrow-sans@1.0.0/morrow-sans-600-italic.css` | `sha384-uqwZDsK9bfLAngHZkwrxf+d9oKj5JfGOOzEHMM9Xuotj8i9EQHADLffCjY7Ya1jg` |
| `@open-metric-fonts/morrow-sans@1.0.0/morrow-sans-600.css` | `sha384-Llpq4WmwjuLIeiJMy481TB4+Q3Yvp3ePh87UGgCwm+urlErR8vtsnIrCEniSI1j7` |
| `@open-metric-fonts/morrow-sans@1.0.0/morrow-sans-700-italic.css` | `sha384-/u556z1kGNlZkeA28moKr20oPjN5GCmdXiL9jaFMFDcd7KD6gpSEklfNax2IK36c` |
| `@open-metric-fonts/morrow-sans@1.0.0/morrow-sans-700.css` | `sha384-E6O15J2ffcE32LCNtmAhzvKmf8CqTU45uAyAMMbv5cmptKBGXFhT8QALEF0aW8Zs` |
| `@open-metric-fonts/morrow-sans@1.0.0/morrow-sans-800-italic.css` | `sha384-SAlWeLUfU465RUhZupE6TdS9iusULeq50N5o0OaRM2u+gcRyEtF9g0HWYlycWeeI` |
| `@open-metric-fonts/morrow-sans@1.0.0/morrow-sans-800.css` | `sha384-OWAl/qTcC1+Vb+4uqfzO4MM1unPFeWu3A/QkTLm/Qly4UYhRCsxszxW53ua5zu65` |
| `@open-metric-fonts/morrow-sans@1.0.0/morrow-sans-900-italic.css` | `sha384-mHn9J8yuC0SvbG/z+RK4ZPl/tn1Ocf2a2Ac/aAYWmC1iMeEoNvO7FqHqmfsqmU0o` |
| `@open-metric-fonts/morrow-sans@1.0.0/morrow-sans-900.css` | `sha384-w+nbbLgMiLSZq3pRZ9n5vUF9pxKRnJMnMs1KILmE8iXgOHbaKxyFVZinVwI5zB+2` |
| `@open-metric-fonts/morrow-sans@1.0.0/morrow-sans-display-400-italic.css` | `sha384-qLy0ACJdjhvhg6Q9A8+4ilYTAyjpIQvVHYj3zXlkOxxtUnW8rYG0PEj/cDjGOPJg` |
| `@open-metric-fonts/morrow-sans@1.0.0/morrow-sans-display-400.css` | `sha384-1qTMjsPUrSSdatRmDxjrUCJF7cnJS7vvEpSUfGn7Tb8iI1vn6jqsnGG3rqhsoN5J` |
| `@open-metric-fonts/morrow-sans@1.0.0/morrow-sans-display-700-italic.css` | `sha384-ujF0D1g1iyp1ynP+c2DrR/5i5sYO6OGzopqF5FonmvLrvX2ffvCsqa3CZqtPz5Gb` |
| `@open-metric-fonts/morrow-sans@1.0.0/morrow-sans-display-700.css` | `sha384-H2oF+CXfZM66rXmt2mPFZTNXjBylqR4Y8nUpkebdIl9dk/HEIDC+UsK2O/JGWoGa` |
| `@open-metric-fonts/morrow-sans@1.0.0/morrow-sans-display.css` | `sha384-EyD2hSTyw9jvMk4gTduUSJyYugbvj5nGyhuNXlxaYeMwYA22xnsGFYptA3FLAt2T` |
| `@open-metric-fonts/morrow-sans@1.0.0/morrow-sans-narrow-400-italic.css` | `sha384-hkQ3/BaKlRKmZ8gakPX7pOT3vuqbzg4IvV3kX++CfaZ7aWV+162x5891rAWQzIKv` |
| `@open-metric-fonts/morrow-sans@1.0.0/morrow-sans-narrow-400.css` | `sha384-SIBlkgwsozgYir6ljCOIhnNE0Bf+K7C/a8lnOiEBOlDA3UIX+3lILtxNOWXF3Oaf` |
| `@open-metric-fonts/morrow-sans@1.0.0/morrow-sans-narrow-700-italic.css` | `sha384-x4ICOnIANb0eFhDXx/FRoHNHPfROmthEx+FY37iyi8TYLTJftZOS6EKfNzYKJtzD` |
| `@open-metric-fonts/morrow-sans@1.0.0/morrow-sans-narrow-700.css` | `sha384-uges6XdKjqDIF7zvgCY52Gl0QvteqqhowL9g/BAPmP28+B9hCsaaN10LseE7rPJM` |
| `@open-metric-fonts/morrow-sans@1.0.0/morrow-sans-narrow.css` | `sha384-yEEeQIJc7g57q1q6/yU8lP6Wb+U4jvucNMy0xsZ9cC7q5C5GFBT3lqyQ9RG8syRF` |
| `@open-metric-fonts/morrow-sans@1.0.0/morrow-sans.css` | `sha384-pstRP714lv0zbxNFKLZDuqNaj0FhgZG1YxdvZr8g2VDy4Y4qFOjyJxWZpPQh4h+m` |
| `@open-metric-fonts/morrow-serif@1.0.0/index.css` | `sha384-/69rOPO7yMdWX14csm9l4u0MCPxQHMAFXliEiHuas7QOnb9fpfhCmVbBBWMXkAXS` |
| `@open-metric-fonts/morrow-serif@1.0.0/morrow-serif-400-italic.css` | `sha384-jAuDs9UqgXYCK11PKLja6f9zMK899KeV2e2HTl9rlSPcEBB7dE//9rKXs8YP4Il8` |
| `@open-metric-fonts/morrow-serif@1.0.0/morrow-serif-400.css` | `sha384-M6B3vgXrGXaZBj6Bt3WID84UE54wdS4tt5j4/I5DoYqQQRXY7njQ+9fdaCE9JKti` |
| `@open-metric-fonts/morrow-serif@1.0.0/morrow-serif-700-italic.css` | `sha384-8tNEvVxdWYUlz4arCIRRj9rCdDo5JIglSIBXePtjPF/TMXJG4+P1WFwRYWENMmt6` |
| `@open-metric-fonts/morrow-serif@1.0.0/morrow-serif-700.css` | `sha384-dgxy/3eJYYpn/oLtk8RZfJVlKHLomHhMuKbar6EO6ve1zhDrzd4YwXpk0jKn+igk` |
| `@open-metric-fonts/morrow-serif@1.0.0/morrow-serif.css` | `sha384-/69rOPO7yMdWX14csm9l4u0MCPxQHMAFXliEiHuas7QOnb9fpfhCmVbBBWMXkAXS` |
| `@open-metric-fonts/oakwood@1.0.0/index.css` | `sha384-qqwRSRCOjKU6+7ZQeFr4hT4ZCoBFYgzWHdcWLIRKLvtonCWNfz4UVnv/o56LwTIh` |
| `@open-metric-fonts/oakwood@1.0.0/oakwood-400-italic.css` | `sha384-Nem5QnlODXmtpxleDDO3y+cjDU40mtgk0PmlXvZeDPmkH/VhyFeCj/t1rFPFOmzl` |
| `@open-metric-fonts/oakwood@1.0.0/oakwood-400.css` | `sha384-UnDjh+wqe8MNlNzoAEOCTHkJ5hWJ16avyVPt28yTZFrq2RpcsQJ2dZ6PgmEuBKkC` |
| `@open-metric-fonts/oakwood@1.0.0/oakwood-700.css` | `sha384-dtO+7Ob3P95vXCXqb83Dkeiy8csslg8x7NB3psBosULmOeRjfRS2sqoQ7mQaTCb1` |
| `@open-metric-fonts/oakwood@1.0.0/oakwood.css` | `sha384-qqwRSRCOjKU6+7ZQeFr4hT4ZCoBFYgzWHdcWLIRKLvtonCWNfz4UVnv/o56LwTIh` |
| `@open-metric-fonts/onward@1.0.0/index.css` | `sha384-87KTAU21hxFeLPupRyzJcAWdDnCC0N6KRrBVGGMbPKVeHDtCE6uIT5jKklZzGC/E` |
| `@open-metric-fonts/onward@1.0.0/onward-300-italic.css` | `sha384-XzM5cRNqYIlfiwjFG6kKautueWP1XeaFmmpXrgu2dq4lWZzj+cvyMeU8Uhs2/Mkf` |
| `@open-metric-fonts/onward@1.0.0/onward-300.css` | `sha384-P8Da6h+VfKUixkmQVwJOzU4gPY9bxYGwIJkWd32g4npyUqT3h6xtwkYsINr5DVPl` |
| `@open-metric-fonts/onward@1.0.0/onward-400-italic.css` | `sha384-ZoP2hi3sxSqCfOi6bR5Uzef/WXndQkGgipG61gAS2ImTODBTR/T9VxHiVkE7dNoF` |
| `@open-metric-fonts/onward@1.0.0/onward-400.css` | `sha384-mUyOPOCvswAIorgFSS762x8Klkv6ZmaSSktW8Jx3g4spx5ZLzsX0yprOjbx4g63J` |
| `@open-metric-fonts/onward@1.0.0/onward-600-italic.css` | `sha384-NFxN3mLgb/tucaT+Fk685IOFb9qDD4SfiqJk6MyMKqKNWeYW+AOXbSXt0/0+Wh9P` |
| `@open-metric-fonts/onward@1.0.0/onward-600.css` | `sha384-5bJ/U3k8y/y6DhQE+LT1VpH9dHlMNbTybj5PQKd3GvQQ36aOsB1GkYpxeA01MwSz` |
| `@open-metric-fonts/onward@1.0.0/onward-700-italic.css` | `sha384-eaaPgM0vefXaBWHLxGvVFyuY7TXOIePeWTlh+uQu8u/+HRVQIsHSFnrHL/7gpr+z` |
| `@open-metric-fonts/onward@1.0.0/onward-700.css` | `sha384-189XvnAq+O0FAgs5/x8XLBxWbnHNhMESL7ht+RpwZPCgZAfxmJNY1zCS/F/5rx7l` |
| `@open-metric-fonts/onward@1.0.0/onward.css` | `sha384-87KTAU21hxFeLPupRyzJcAWdDnCC0N6KRrBVGGMbPKVeHDtCE6uIT5jKklZzGC/E` |
| `@open-metric-fonts/orbis@1.0.0/index.css` | `sha384-rsKafUFDRoRpRN2jLkz7AkI6D0hBM5ROeVWbjB7xNY+RC5Z0Y3U2fm9dcOeeeL/C` |
| `@open-metric-fonts/orbis@1.0.0/orbis-300.css` | `sha384-klCvEImcLm5p4tyKPEOs+ejkQ9zcs0HwmJByR/OHS2pe36XB08ZON7+pp0QZInzL` |
| `@open-metric-fonts/orbis@1.0.0/orbis-400.css` | `sha384-E5HrGqr7DNk9FGdzh/C6ALuUKw9/L2oLgbCuPfvB3snpToToJdCrCneJlPm+ECdp` |
| `@open-metric-fonts/orbis@1.0.0/orbis-700.css` | `sha384-QTzwQQYjv0zZIwhZAuzt0AjHSYRhbtqAwhW/FKfSZn5BsU7tSvIlNFJoxdmgsKMO` |
| `@open-metric-fonts/orbis@1.0.0/orbis-condensed-300.css` | `sha384-tG8l5FbTia5bCbNkJ2sL/OyNlyadi1lTwuuVPngJVDugIprOvECdQsbJbw7d44f+` |
| `@open-metric-fonts/orbis@1.0.0/orbis-condensed-400.css` | `sha384-fjuvLse4PBhpt9xz21vq7QbhxpNojm3Eu4i+ppAyyeZPcjbImt6GVpQXO9WQ2kC5` |
| `@open-metric-fonts/orbis@1.0.0/orbis-condensed-700.css` | `sha384-m0ubN6uI3/0PRhRb0+O3mdfPV1Lljljg1abH1ZDzTgmkZd/YszRlirlCFXs/YdBQ` |
| `@open-metric-fonts/orbis@1.0.0/orbis-condensed.css` | `sha384-pdfkit3kQ523Wd9coNPgXpIdlc8Jm1saqooNm0d0MKRvnWUpl88j/LuLfLb7aMSq` |
| `@open-metric-fonts/orbis@1.0.0/orbis.css` | `sha384-i/V/2r3fjY2L1dwX1MNnxilFl5qJ62xBzkmPu2KdVznFNhXltaxEEywuUL9wqQSM` |
| `@open-metric-fonts/ordinal@1.0.0/index.css` | `sha384-grivFtL1SikZqRBE78woFdOUiFROCnqyH7AXKgYzH6poWOdfHoKdBM/hS1k1b3i2` |
| `@open-metric-fonts/ordinal@1.0.0/ordinal-400.css` | `sha384-grivFtL1SikZqRBE78woFdOUiFROCnqyH7AXKgYzH6poWOdfHoKdBM/hS1k1b3i2` |
| `@open-metric-fonts/ordinal@1.0.0/ordinal.css` | `sha384-grivFtL1SikZqRBE78woFdOUiFROCnqyH7AXKgYzH6poWOdfHoKdBM/hS1k1b3i2` |
| `@open-metric-fonts/overlook@1.0.0/index.css` | `sha384-eJIsixtMs7+MdQK4W8SVFXqyFcAc18ikQ4hWerGRHbULWoKvk1qsaP3o12nYxBWy` |
| `@open-metric-fonts/overlook@1.0.0/overlook-400-italic.css` | `sha384-1IfZHMJ1QIqywiRX8/rmYPD2LzpxcDwTqOXqCGg7xUPBva1SsSNVGcvJQrsBw1SE` |
| `@open-metric-fonts/overlook@1.0.0/overlook-400.css` | `sha384-2z7t3HgYk4nwiu3shmr/YAae6KZzfbSOx0wl+t7S1vRXPzDry3qxp31ktx8JPOKO` |
| `@open-metric-fonts/overlook@1.0.0/overlook-700-italic.css` | `sha384-PC9lWZN0Q+K6WUJYy8wGZgCw/KsHKAQGs+6BiRNHv9ZW7oW8dJaOPGmbzbf1cJXl` |
| `@open-metric-fonts/overlook@1.0.0/overlook-700.css` | `sha384-Dxv0pT9jUQO8GDjUjYPH6Muua9FxQZZ6aD19eIUusNwuvqM0UeWmwV5qgIVdWXgk` |
| `@open-metric-fonts/overlook@1.0.0/overlook-display-400-italic.css` | `sha384-3+G0QB/7sggjFRP7rQ5WRJvAvxulJGUxs08HXrA1QI8IIbJLdpTeo/lZhcK5ybZp` |
| `@open-metric-fonts/overlook@1.0.0/overlook-display-400.css` | `sha384-/ypU8N5w53pZBzZ0QJKy146l/z/f+54Gh8KYVXMJsN4u8RkiZCX9MtPhzkn1LK9T` |
| `@open-metric-fonts/overlook@1.0.0/overlook-display.css` | `sha384-GeUrSYftrMrbmGmQqEjFMYmBA8inrMbgY1XtPQl5Hc1tjX7fdobDKsxxAnDnK3ug` |
| `@open-metric-fonts/overlook@1.0.0/overlook.css` | `sha384-wvZYTwIZduYEmy5JjJclGcyjLdLExmGO3Y5RQpx18ym9DHSzvFHVCgL93ERh7Z8p` |
| `@open-metric-fonts/parma@1.0.0/index.css` | `sha384-5pV4IXlsLtWOnv9Kb4s92woz6a+EgmsZsfPbX6GllHWo4xfkPd6l6YHiqT0BYfi9` |
| `@open-metric-fonts/parma@1.0.0/parma-400-italic.css` | `sha384-TdA/l8KQYbUiBBZ5/555nV6TH0aZ6fvRB1nhgTepCAUCMlbGuzuGX+PJCKcolhhk` |
| `@open-metric-fonts/parma@1.0.0/parma-400.css` | `sha384-VBXw8B2pcCGsHKclgTHkhWWkyBrYKLVU1kpL2WEGxvu6Ikhtu29uh//CnZbutJpy` |
| `@open-metric-fonts/parma@1.0.0/parma-700-italic.css` | `sha384-rT0nMBrkQud/COvyC3pDsNqmL539tIslHWizVU1sZvlGI6lvTEwWwDvVo3e3th2q` |
| `@open-metric-fonts/parma@1.0.0/parma-700.css` | `sha384-LTvncq8C3Kr554bk/KVmmGxmUFFiW6dH4SiZJ/d/hsDqBr06FgE7SiwWvnoG0/rA` |
| `@open-metric-fonts/parma@1.0.0/parma-900-italic.css` | `sha384-N+KKOj/h3jek4J4Ny1J+xziJwNccjGnqKHlwX2lx3IYj2e8HO49s4MptW/NuJGvr` |
| `@open-metric-fonts/parma@1.0.0/parma-900.css` | `sha384-JZof9/9UKtmpPtV0H6Ck5kCMmxWNGUQTkfmVOZq6KtO5ewCImsW8BYnciDls89++` |
| `@open-metric-fonts/parma@1.0.0/parma-condensed-400-italic.css` | `sha384-z7LaX1C5c9z+hTsYobkD9ZFCNYnHLZYvNe1netRqTvK951aHWq+9ynM6eQXuu6EJ` |
| `@open-metric-fonts/parma@1.0.0/parma-condensed-400.css` | `sha384-kFC0xZF/PMNJR2IYoGLLRxj9rwYr/zVTbnsxV5mujRIHeoFkfGPVrSwncfOHWGUt` |
| `@open-metric-fonts/parma@1.0.0/parma-condensed-700-italic.css` | `sha384-folSSU/pOCF6MYcqe7Zo0w2oV+xXU4MAEg2umyKkFv6wXdQXsxS0UgbdxaWXiptU` |
| `@open-metric-fonts/parma@1.0.0/parma-condensed-700.css` | `sha384-C7pLHcu6q2hRQGLLryJPWoC72S6PVekCtpC1JgJIfRPL7OSIbxAM7oSIHN51133J` |
| `@open-metric-fonts/parma@1.0.0/parma-condensed.css` | `sha384-A6O/xO/o0bOYr6RjEagOGUpr/b0ZZZyG49klEiEqPTYSQz/QV92kGW0I3cJAKQ7V` |
| `@open-metric-fonts/parma@1.0.0/parma-poster-compressed-300.css` | `sha384-lrkEbqvlN0nhqHnSinVFGajiP0Bhk/kxfpACG6sdec10UJlQJjkUjXgsjIKFkRAt` |
| `@open-metric-fonts/parma@1.0.0/parma-poster-compressed.css` | `sha384-lrkEbqvlN0nhqHnSinVFGajiP0Bhk/kxfpACG6sdec10UJlQJjkUjXgsjIKFkRAt` |
| `@open-metric-fonts/parma@1.0.0/parma.css` | `sha384-oFDC0FPtxjoRq5ibodVgm9BxxxWLwRb1TtGw6pNQPqq+GnmMCamrynrSsI4G9rV6` |
| `@open-metric-fonts/peachtree@1.0.0/index.css` | `sha384-4A4Iy44sHedFPYuEwYskZLIsO/LHFZIZzvl3CgyVi6Bn54uDbZXj0xsNb5cFjGkR` |
| `@open-metric-fonts/peachtree@1.0.0/peachtree-300-italic.css` | `sha384-4T+szd4flHrAQqg3T9dOBdrR2IJX2LpLMgwPd4JYooS4PtK6eCAL2ND84x4VItLS` |
| `@open-metric-fonts/peachtree@1.0.0/peachtree-300.css` | `sha384-DaQ/gIb8Jl/mRM5lxMaL0CHMx+K+Hh2Di+98Z0+QE75nxeA6Grfw4PbgCiytWSHw` |
| `@open-metric-fonts/peachtree@1.0.0/peachtree-400-italic.css` | `sha384-S+LL/hiT+nZJNzpoobVl8tXF9X17OdCTHbZiRZuQ7nK1gPP0DxlkSw8nidexQZuS` |
| `@open-metric-fonts/peachtree@1.0.0/peachtree-400.css` | `sha384-ysCvhz29QRt33lGAidKbe/Gvxorm7Ye/n7lof1lKOahqu3el5m3k/pxnLj5st940` |
| `@open-metric-fonts/peachtree@1.0.0/peachtree-600-italic.css` | `sha384-zFc84gsHaE0SCZAxjChae+hypbWyIUJqCeVmWZh6hFy5oDJF5Kfm7EKmGAOklRL8` |
| `@open-metric-fonts/peachtree@1.0.0/peachtree-600.css` | `sha384-Nphed4gK4HEVBfitb8pRD3G5Zuwng3uYaR57BsUNXgsdGSzaR9Ctio2ocq8a2BcJ` |
| `@open-metric-fonts/peachtree@1.0.0/peachtree-700-italic.css` | `sha384-poCbsXVS33Z2xkKhc73+slvTctVaF8ZKIfZe7Rk203HrLRWCt8Wm88G6YkIUtPam` |
| `@open-metric-fonts/peachtree@1.0.0/peachtree-700.css` | `sha384-dxsULWz0kLmP9kw6bJrYiAgAVdtDgGDGtuzl6s9p2HPw4lAz4RIoHQ8fMhqf+dh/` |
| `@open-metric-fonts/peachtree@1.0.0/peachtree-900-italic.css` | `sha384-LuYDeNWh76QRhy2SSlAzWMx3jXWHsseOvjauOAqa11FcsGjClLceMtoCJE+Qsov3` |
| `@open-metric-fonts/peachtree@1.0.0/peachtree-900.css` | `sha384-rlzU14XyHcCVMX27U8adA2MswIgT2fqNWyqTkUqCoFjxL+N1PfXn3Ff9GxuNdUF7` |
| `@open-metric-fonts/peachtree@1.0.0/peachtree-cond-400-italic.css` | `sha384-eQqnEr4C7QFlE+8ZdRlYl62gqMdPF3dZhsHRVhoJcJeTino2aQD+lr8joo89pqlP` |
| `@open-metric-fonts/peachtree@1.0.0/peachtree-cond-400.css` | `sha384-3wLFdM3bXwdsfijJFoAsj92I+sJH3mjPLYdMkFU/6lOKes5P/VAQhtFo05uBytZi` |
| `@open-metric-fonts/peachtree@1.0.0/peachtree-cond-700-italic.css` | `sha384-nclz7d2Xzb6Y1fbbb6iGHY+m1fYOV79fbV/FgpF8RpdBlbbwriC7h3LPY+6Z4eKQ` |
| `@open-metric-fonts/peachtree@1.0.0/peachtree-cond-700.css` | `sha384-U9U7QmcPVGVfuTaQKNmAs+ZgxiHCJaDRGSdjhpya0hFdVqYc6/An9TZ29ibzOkLK` |
| `@open-metric-fonts/peachtree@1.0.0/peachtree-cond.css` | `sha384-8wRXyAUyt9EEh6oNbt98kLiiVz+cFoz0k7aZYqdI1tvwlCFW1bLeORGn31ldGPUm` |
| `@open-metric-fonts/peachtree@1.0.0/peachtree.css` | `sha384-2elNorkaj5T+LUc5WVnPK3fmsezptdS0WjvowQ+pvIYUwGNHsAa1lvbPJETSL6qs` |
| `@open-metric-fonts/penmark@1.0.0/index.css` | `sha384-YFgM3j2LmZkplSDR6JRIOD/IejnDifPGuY+jaMbtcpBAbdAZhTmukyEfmYIWWq+3` |
| `@open-metric-fonts/penmark@1.0.0/penmark-400.css` | `sha384-u7EoDje8HjriV4/UtDu9p/EhTSZKXrGWy1sBrnHvcH+Ms+OxmXi7/Jl9uu21mt4S` |
| `@open-metric-fonts/penmark@1.0.0/penmark-700.css` | `sha384-C9Z4uy8NiAEt9bh7uPLkrzxaI1OuBN8xmU0pgCpdN1ZqgWdwhyBmEgaUhRDrrMyX` |
| `@open-metric-fonts/penmark@1.0.0/penmark.css` | `sha384-YFgM3j2LmZkplSDR6JRIOD/IejnDifPGuY+jaMbtcpBAbdAZhTmukyEfmYIWWq+3` |
| `@open-metric-fonts/pitlane@1.0.0/index.css` | `sha384-0GTAMVOzd6W8TyzZOMJRjGlNuHtazi9KxGRFzThbNFrR7bk4cIdhEpUeaHwhtb+e` |
| `@open-metric-fonts/pitlane@1.0.0/pitlane-300-italic.css` | `sha384-PIbLqdAxDNuvQ9Q2OwP6vlDbfbrqHO3vjd+C2pWWmGyjy3tU/1/aGcpPgZ0UkQMI` |
| `@open-metric-fonts/pitlane@1.0.0/pitlane-300.css` | `sha384-IknoWkWqZmwAk3JzvvqkO0WWn3+PrHzqbb97V4zatjcOsKV/HXcfJwefiW/46oLi` |
| `@open-metric-fonts/pitlane@1.0.0/pitlane-400-italic.css` | `sha384-pDXzSVA5EXJxvjga4gDi3m+lIYYzrHKRaMAO8SS1a6Q+Fr5oCXzf6L7fwrXSYlN1` |
| `@open-metric-fonts/pitlane@1.0.0/pitlane-400.css` | `sha384-AwbOQ+aOb9oZAViT9C5mWNkJormaGIThSAv5eONglamFf0jYFRGKY6nRDrDI7SRZ` |
| `@open-metric-fonts/pitlane@1.0.0/pitlane-700-italic.css` | `sha384-0NBa7kc8NVVFzS0btQiNus0kSPOHtgJR8EvGu+pK01fIeHFren3APCmBdybsprhE` |
| `@open-metric-fonts/pitlane@1.0.0/pitlane-700.css` | `sha384-Y6puvji9Kbn+etPKHlobnLNiHXSgS+uJanw1vTlJG4LfJDe8O6MuFzyb3gLQnWBe` |
| `@open-metric-fonts/pitlane@1.0.0/pitlane-condensed-400.css` | `sha384-cpTh9S/WIGChVOZef8sROW9v8mhbOQCea9pkFIcHgCkhL6mnsr1EFkwju4g5K4gb` |
| `@open-metric-fonts/pitlane@1.0.0/pitlane-condensed.css` | `sha384-cpTh9S/WIGChVOZef8sROW9v8mhbOQCea9pkFIcHgCkhL6mnsr1EFkwju4g5K4gb` |
| `@open-metric-fonts/pitlane@1.0.0/pitlane.css` | `sha384-zoLIPh01fkrxMHr1Xf19hpJZwSe+mWL7k9vFMe0bIl/ybQPIOT7BepIZ3ZNw6raQ` |
| `@open-metric-fonts/plinth@1.0.0/index.css` | `sha384-WdJpN86nvEqig4XfesZJUuuTT86m4nk9gt5nsRBqRNFSFY1LpvhGxtObkI9kA4Gb` |
| `@open-metric-fonts/plinth@1.0.0/plinth-400.css` | `sha384-WdJpN86nvEqig4XfesZJUuuTT86m4nk9gt5nsRBqRNFSFY1LpvhGxtObkI9kA4Gb` |
| `@open-metric-fonts/plinth@1.0.0/plinth.css` | `sha384-WdJpN86nvEqig4XfesZJUuuTT86m4nk9gt5nsRBqRNFSFY1LpvhGxtObkI9kA4Gb` |
| `@open-metric-fonts/prism@1.0.0/index.css` | `sha384-0YIUJzavlvLgg7pDJ70FpqdRFw9DmnqKmO9yNYNFRkFxgYPJ8o2iEKTW/vFytFw4` |
| `@open-metric-fonts/prism@1.0.0/prism-bright-400-italic.css` | `sha384-Xi6UcpgnoPM1ITs3IGKL2dIJFbLmYw48MTSWb6sMw0McSP98Fo+5+OY59PZgzlMG` |
| `@open-metric-fonts/prism@1.0.0/prism-bright-400.css` | `sha384-BQBoPXiO2opFwDAjOfe6AjQecO/GYDvC4DnpEQu16raWaW8oOXTPTehlJ6t8fS6X` |
| `@open-metric-fonts/prism@1.0.0/prism-bright-demibold-600-italic.css` | `sha384-B2OwpVH+o3obo2TULvLjZrj6YhIqgryZJMpoLbjvyUXdXCm2gma0Bk/hninzYaAC` |
| `@open-metric-fonts/prism@1.0.0/prism-bright-demibold-600.css` | `sha384-hBVBj+12YzCMB9k4/atNirgCB2CxCn1rxkPDtadFfPb4/r8gr5dqgmUfLXgwmJKH` |
| `@open-metric-fonts/prism@1.0.0/prism-bright-demibold.css` | `sha384-g66xhqlIDp5Wbb5tNUFnEZE34/Ypn/uqY2bL6J1hsYvwF6bfRiNLutM2RNqLy+ut` |
| `@open-metric-fonts/prism@1.0.0/prism-bright.css` | `sha384-1B99xKqKbMnhxq6N+4OecBHm9+qqJxFnHDoHg26TP5nvN/BCMrrUaSTf1wvfmOH+` |
| `@open-metric-fonts/prism@1.0.0/prism-calligraphy-400.css` | `sha384-RZsZmsKnMDiREylM1uBUIATw3FHT16TQatvRBy1480lXQPvwucw7ApKLUN3ojzYf` |
| `@open-metric-fonts/prism@1.0.0/prism-calligraphy.css` | `sha384-RZsZmsKnMDiREylM1uBUIATw3FHT16TQatvRBy1480lXQPvwucw7ApKLUN3ojzYf` |
| `@open-metric-fonts/prism@1.0.0/prism-console-400.css` | `sha384-FjJHzh7s8YyqDn/UjBq1g008ihfN1/VJypZN05A6S1h9XzhsEkl1RGcmuzvqAdCO` |
| `@open-metric-fonts/prism@1.0.0/prism-console.css` | `sha384-FjJHzh7s8YyqDn/UjBq1g008ihfN1/VJypZN05A6S1h9XzhsEkl1RGcmuzvqAdCO` |
| `@open-metric-fonts/prism@1.0.0/prism-fax-400-italic.css` | `sha384-ASf8T6nctW82u4UxWl2w4IsshYa7ZhPwrbOrpNDEr2nxRU01h69AXjFV3wzEsaEO` |
| `@open-metric-fonts/prism@1.0.0/prism-fax-400.css` | `sha384-zZJI9DzetZc1dUXrrTe+O4UB6/30jca7AX+jkKsD87J6GKzwtTm+M3iPGHGnvhac` |
| `@open-metric-fonts/prism@1.0.0/prism-fax-demibold-600-italic.css` | `sha384-ujsU6zg/AUUim0OBBZMIpolbs6LOzPw0dGantng97npzydttjojJZj/T68XsBGAi` |
| `@open-metric-fonts/prism@1.0.0/prism-fax-demibold-600.css` | `sha384-o61ta2a9/pJHnQxWeyBBqMX4xvywoRrMNMcbmdAdEnJanjy3Xyf9Etez/ObURRne` |
| `@open-metric-fonts/prism@1.0.0/prism-fax-demibold.css` | `sha384-9aRid+5f9XReWY9Zo32ozzlQjlsNh2xV11gM+EAVuzsO9gvyzuQrmF5mB5HPlFDL` |
| `@open-metric-fonts/prism@1.0.0/prism-fax.css` | `sha384-STlsgbrn1n3E6DWsLm6PzpOA/w1YPgnakzRXHUawxi5onMbHPoslwsQ2tZrCs1CH` |
| `@open-metric-fonts/prism@1.0.0/prism-handwriting-400.css` | `sha384-JRtK8/m/oVQtW3mAQ5Ys1yY7Q2f8vANbFf+v/OuMzFgD+hCtPFq1DYULg8dBxhKr` |
| `@open-metric-fonts/prism@1.0.0/prism-handwriting.css` | `sha384-JRtK8/m/oVQtW3mAQ5Ys1yY7Q2f8vANbFf+v/OuMzFgD+hCtPFq1DYULg8dBxhKr` |
| `@open-metric-fonts/prism@1.0.0/prism-sans-400-italic.css` | `sha384-qqI23RErxQzNhHErmosI9y8oqwE3Al6jIBF3zWy3mY00o00jT4LQf55fDtK6f03x` |
| `@open-metric-fonts/prism@1.0.0/prism-sans-400.css` | `sha384-IemSFfLsT+9vCETaEG5nGuJjfSEbFfgtYkHgVR9gBBufr1WiamlBzJ9L/G/+fH7m` |
| `@open-metric-fonts/prism@1.0.0/prism-sans-demibold-600-italic.css` | `sha384-bFPBlnENJPuTjxi0hdIeEeFg5m0aYFrvYFw/C/+cRI9UCQalV91Bt0u2L9f8Ev9j` |
| `@open-metric-fonts/prism@1.0.0/prism-sans-demibold-600.css` | `sha384-XqzBpys8Sj+2qJgGdFWViSoKZwxX8xIKcydD9UaWghBIKMO7YbwB8j9RFYasLosp` |
| `@open-metric-fonts/prism@1.0.0/prism-sans-demibold.css` | `sha384-kLY15BTsUa2iyy2tFphM9kESujuUUdJiRYfQbctbidD0u7O83F7enIaH5zyCxOXI` |
| `@open-metric-fonts/prism@1.0.0/prism-sans-typewriter-400-italic.css` | `sha384-C56Mfk2gsTb5kWOJ2vWfH+ou/bZQv30M4wTVmOpFbRa4T9Jg1OYLWcTO1W6qOQEk` |
| `@open-metric-fonts/prism@1.0.0/prism-sans-typewriter-400.css` | `sha384-j4lsvFXO2T5GYn3IT8EeWJze/pxyCisUL+Y9HukqXYzp9ElzZYoxOCHLcoH06q7w` |
| `@open-metric-fonts/prism@1.0.0/prism-sans-typewriter-600-italic.css` | `sha384-C+U3HSByLaTY3Z7hlxR7BzkcYYX/g/VMipT1M8c50u55hfE4JmUlVxAefV3vqUDO` |
| `@open-metric-fonts/prism@1.0.0/prism-sans-typewriter-600.css` | `sha384-sfzeMAPk5OiyhRIRZ3qb2P64Ir3OodY2v9MVNa73+BwRQIfXvZOu38Fj7ZzILYIj` |
| `@open-metric-fonts/prism@1.0.0/prism-sans-typewriter.css` | `sha384-TR/1RqMPsCy549gW0NoNPRopDelAVFQCAItT/ICMsbJCbTdAnZqoocAoolTh2Us6` |
| `@open-metric-fonts/prism@1.0.0/prism-sans-unicode-400.css` | `sha384-CrD4T9dv6yK95EeJaG7tuvkXmDA33QYVyWlBbLV1fkcpUSjx8A4Clqh/6HkMjn4u` |
| `@open-metric-fonts/prism@1.0.0/prism-sans-unicode.css` | `sha384-CrD4T9dv6yK95EeJaG7tuvkXmDA33QYVyWlBbLV1fkcpUSjx8A4Clqh/6HkMjn4u` |
| `@open-metric-fonts/prism@1.0.0/prism-sans.css` | `sha384-14Is1alAcuZBcJB5tDvIByNEjhuJZM71OUPu6nBsMsSEJtw3JFpxwCFes4Jx5MWy` |
| `@open-metric-fonts/quarry@1.0.0/index.css` | `sha384-sq5nzGaT7QhBb68CGiWrcQCg7RG44RwYyDZbi5yzPpvVjSbD6/9xgAOcQlUdDKKy` |
| `@open-metric-fonts/quarry@1.0.0/quarry-400-italic.css` | `sha384-dTChAJ3hgIfb09hXg225cRy/w4M5zrpzIU+QXyn25W9u0fKoP6sc6WLoBfbKwN5o` |
| `@open-metric-fonts/quarry@1.0.0/quarry-400.css` | `sha384-bqHcv5J677Gd1WWEUxjLJqWC5d835LonwYsaXaHaCvPPFKxXGQSU7DWe/TV2PSBm` |
| `@open-metric-fonts/quarry@1.0.0/quarry-700-italic.css` | `sha384-EvJcIY0vYhS+z+9xGP8Di9q2uNaxug6hJjO8QZMEJQD1zrq3VjieNnyLu3WHFjv+` |
| `@open-metric-fonts/quarry@1.0.0/quarry-700.css` | `sha384-a+wNEaynHbb3KI87HUDW5BzVR0XtPyFjwoEl49SQjymSq/5Ff6wDhSvoKJR/Ihi7` |
| `@open-metric-fonts/quarry@1.0.0/quarry-condensed-400.css` | `sha384-VPvmVlJRGAP85bxWzLc1FQhxqtgkdtlpjfZxLIbcp5FZlS2qKJKB40wz7hemii7p` |
| `@open-metric-fonts/quarry@1.0.0/quarry-condensed-700.css` | `sha384-Al8rrHa5gYqaYXJ8xfGRgNCMQ3iovfsMFvgXKqJM1LDyVh2Z5ougTtLUu04WoAw+` |
| `@open-metric-fonts/quarry@1.0.0/quarry-condensed.css` | `sha384-i3lAmKM2qjCpIG/ULYuzp1ldAhnp+gHQHaGcPKtZVhMFmuRHzs3lXCLmispg90mj` |
| `@open-metric-fonts/quarry@1.0.0/quarry-extra-bold-800.css` | `sha384-te/HaNKo5e5CS8bQ9VW9fk2QZFoAX/7Usg5plwJeOWtYqHczMFZoudOETC0nesZX` |
| `@open-metric-fonts/quarry@1.0.0/quarry-extra-bold.css` | `sha384-te/HaNKo5e5CS8bQ9VW9fk2QZFoAX/7Usg5plwJeOWtYqHczMFZoudOETC0nesZX` |
| `@open-metric-fonts/quarry@1.0.0/quarry.css` | `sha384-Aiu2dS+WyTs/kxx2MT9TvC8Y57n99cH1LAwdNj3bFGyTOmRBQ8kf7f76N2Fo7si7` |
| `@open-metric-fonts/quarry-nova@1.0.0/index.css` | `sha384-bSAFud4woHhdMRaQTnbi37iI1M4jXXw3IkL240C2gwUzuRoQFESFpyw2bHUHk1Rg` |
| `@open-metric-fonts/quarry-nova@1.0.0/quarry-nova-300-italic.css` | `sha384-PZlHFKnhiYZHlkcc0Z9FHCnk1yXqWOdqx94LfX5V2IQuHj2YmB0qyA21NTvY5jkp` |
| `@open-metric-fonts/quarry-nova@1.0.0/quarry-nova-300.css` | `sha384-5FtDt1QOntBkKK5PN//4PUYO1yu1NWQrtUtm1UvW70RmgkY9jdi0s0oFU0FJBVTW` |
| `@open-metric-fonts/quarry-nova@1.0.0/quarry-nova-400-italic.css` | `sha384-/azflh1SaJk5MVMf8yjEZXcMGlRXJ1ImEVN0JojzQmxwISEyh6Q+NJeIewGd+7Al` |
| `@open-metric-fonts/quarry-nova@1.0.0/quarry-nova-400.css` | `sha384-4X1BZBZVdifZRPeo29eMSnrk8KBIlLENEn54jfN0d5ooF5cPSsbB7YrinNmEHVky` |
| `@open-metric-fonts/quarry-nova@1.0.0/quarry-nova-700-italic.css` | `sha384-DetssUI/zfmJAGhVVui9d7ZVjujTK93P+67poOid8N8xI1cNW+Th1NokHJ04GQUe` |
| `@open-metric-fonts/quarry-nova@1.0.0/quarry-nova-700.css` | `sha384-IeVpy9f4+anhDDMTFDn/Ij8MPBtTDRsllTzgBWjsdfNZm7bZ/DyDDyehOE7P4NZM` |
| `@open-metric-fonts/quarry-nova@1.0.0/quarry-nova-condensed-400-italic.css` | `sha384-fgWhXyEqb6npwKoXxmN36IgvqgdtQE0zS1fu8uB4Is28QIXRBACHVTJvzeVoJk58` |
| `@open-metric-fonts/quarry-nova@1.0.0/quarry-nova-condensed-400.css` | `sha384-rS9gAqEAw0PMe2tN7G91cFw7rgfCkUJ69DJP7mElEH1/P4Vw/P49ok9CfGXwdEtX` |
| `@open-metric-fonts/quarry-nova@1.0.0/quarry-nova-condensed-700-italic.css` | `sha384-KvkEpKAIK1VVA/T1gf1FzhWDicLZ0nOvCjd7TtrOA4NDaVA/RU506qju6v3XfKdh` |
| `@open-metric-fonts/quarry-nova@1.0.0/quarry-nova-condensed-700.css` | `sha384-AZ2azhz5JvNhKi9ejgbrrcy1JSO3ForOmladTVsI+kJHAYWyKAJWwQPPbhfAtu13` |
| `@open-metric-fonts/quarry-nova@1.0.0/quarry-nova-condensed.css` | `sha384-Bgy9J2xGIO6GOkrNt1+aDmKcw9SJhgxRFsoDOXTvcCozJid5Cve7e3ucbXqLeUdu` |
| `@open-metric-fonts/quarry-nova@1.0.0/quarry-nova.css` | `sha384-PCcChjHpPJcPRYXpo6NQD1HeKwDHx37MZS88z2uQhcsT16Xw+K2qA9GXiZQq86w9` |
| `@open-metric-fonts/rhine@1.0.0/index.css` | `sha384-r2P3u2Q4mVgq7tP8B6RSoRsVk42lqbCgKKnCIe6xWwKyJ0Yw4GiWP6y9jG4hPwOY` |
| `@open-metric-fonts/rhine@1.0.0/rhine-400-italic.css` | `sha384-+S2I2CrWxhA4p0i2XtE9wstb181wzSv40BJOUsY0zGh5WS9o9fxk81klzYFOyQk4` |
| `@open-metric-fonts/rhine@1.0.0/rhine-400.css` | `sha384-KuzV9JGIu1RW3mC3o5ImKtI0fGqq7+un9rTRED6x5smJK6AKf0GETFbAAY481fDv` |
| `@open-metric-fonts/rhine@1.0.0/rhine-700-italic.css` | `sha384-SHLRuUWXoE7L28mfs+xGeDOpMCev1wVW5Q+3ZqpzUnj4zW/4ltwSMFYR4EhmpSpa` |
| `@open-metric-fonts/rhine@1.0.0/rhine-700.css` | `sha384-ZDFZWK1QGwJCZ9iAQ6D0WYvkaq7FlLikGpbGdXY4TiDXt2M+eQY7S1VKEvm+Wsiv` |
| `@open-metric-fonts/rhine@1.0.0/rhine.css` | `sha384-r2P3u2Q4mVgq7tP8B6RSoRsVk42lqbCgKKnCIe6xWwKyJ0Yw4GiWP6y9jG4hPwOY` |
| `@open-metric-fonts/rill@1.0.0/index.css` | `sha384-ExoOqmXJkGu7b/v8DpAB9VftPIeJA/r5lnbpUHQLdGSH4UKmVmhtHxJ+saKg/R/V` |
| `@open-metric-fonts/rill@1.0.0/rill-400-italic.css` | `sha384-PvHYPqN8YIkeWw/A9WVDaZWnCBC0Ct14qY/6JbEyJfc469xwAYx5PqCh+6eGUeYA` |
| `@open-metric-fonts/rill@1.0.0/rill-400.css` | `sha384-Okd+sKidzqS2enQiQbSjLhiqNTHRaG9LCzjBCrMPv9/46A+LZqDuPRxyP2vYH26K` |
| `@open-metric-fonts/rill@1.0.0/rill-700-italic.css` | `sha384-uRJD4zKgj9dFT+TXVVeIUFM7hMtWKHM1CvbWcXZU43y96fOa+PSYxXBjL+kkCpoW` |
| `@open-metric-fonts/rill@1.0.0/rill-700.css` | `sha384-IVm259jow8lroWBGFWZxC6Gy0iSif0WGxH2UzAfZDF7U/M4BI2VRHPQKPocapD5k` |
| `@open-metric-fonts/rill@1.0.0/rill-condensed-400.css` | `sha384-EcOZpzNuzJjKuVi22Y1GYHTyI8WztyaoZdmLq+IjjOFDUwpovTIBAlLwW9WjRIAP` |
| `@open-metric-fonts/rill@1.0.0/rill-condensed.css` | `sha384-EcOZpzNuzJjKuVi22Y1GYHTyI8WztyaoZdmLq+IjjOFDUwpovTIBAlLwW9WjRIAP` |
| `@open-metric-fonts/rill@1.0.0/rill-ext-condensed-bold-400.css` | `sha384-tzXTnE3KowLtg/upzogOsCFNC3A4wPwENwCtIhkTaDMJNDQP5R7z9wtzZMd+p8XR` |
| `@open-metric-fonts/rill@1.0.0/rill-ext-condensed-bold.css` | `sha384-tzXTnE3KowLtg/upzogOsCFNC3A4wPwENwCtIhkTaDMJNDQP5R7z9wtzZMd+p8XR` |
| `@open-metric-fonts/rill@1.0.0/rill-ultra-bold-400.css` | `sha384-3VzwxVio3ZMNall6l8LplJcdsRR9XpoCgBgdeGy8pTVHplxg2fy2TjulBBVWnIJu` |
| `@open-metric-fonts/rill@1.0.0/rill-ultra-bold-condensed-400.css` | `sha384-KLvcijzDNae2kAglKf9VKvxpb/AjHc17F95O5NrpaI8X/dn/J4e+7/3+2J8P+n+f` |
| `@open-metric-fonts/rill@1.0.0/rill-ultra-bold-condensed.css` | `sha384-KLvcijzDNae2kAglKf9VKvxpb/AjHc17F95O5NrpaI8X/dn/J4e+7/3+2J8P+n+f` |
| `@open-metric-fonts/rill@1.0.0/rill-ultra-bold.css` | `sha384-3VzwxVio3ZMNall6l8LplJcdsRR9XpoCgBgdeGy8pTVHplxg2fy2TjulBBVWnIJu` |
| `@open-metric-fonts/rill@1.0.0/rill.css` | `sha384-kNMV0PBObPy4KuEOqwnISb2NpyowBgxwy9QqNsg0ooMgkyDU0/D9yo50ooBKf3+Y` |
| `@open-metric-fonts/rill-nova@1.0.0/index.css` | `sha384-Gt0FmJ7gSHYj2C+9aPwZyESO078aLnKL48ee6ThUW2iepd+v6Cu9tAkuBFDMl3Al` |
| `@open-metric-fonts/rill-nova@1.0.0/rill-nova-300-italic.css` | `sha384-dPxQm9pv5SSFdyhBMIuxbCgZ7ajlcsL5TSy7vs5tg7HeKbdV9DM5EeFt5+23Wglc` |
| `@open-metric-fonts/rill-nova@1.0.0/rill-nova-300.css` | `sha384-KVwEiNWEQUXkKHmZra7LLiUBUeKEjw4XWGsqsSofF+hiUYmDR+rGQ6/28awsBZP2` |
| `@open-metric-fonts/rill-nova@1.0.0/rill-nova-500-italic.css` | `sha384-GxJiLB2kYG6f6YF9QWdw1r8YvA3wHcOeLCxqtG13uNh9dXJGniWvyOzth0xywg9L` |
| `@open-metric-fonts/rill-nova@1.0.0/rill-nova-500.css` | `sha384-3ObWg+rzpdVtN7PH5l6I0GLPJ/ZO3NfvqC00t+UeODlvFxkHTX7NzvAL1KRv4RTN` |
| `@open-metric-fonts/rill-nova@1.0.0/rill-nova-700-italic.css` | `sha384-bTCpnX7fpDRTEQK2kaiZ6PpLP2p8FkkhkLrtlHbKThMB9fTBb9bcVqX+izlJnHlD` |
| `@open-metric-fonts/rill-nova@1.0.0/rill-nova-700.css` | `sha384-jU81viYJtdeMuk48sjgVIsky3/ZO+H3NsPiFFiNgMfnivMn/Vnzw9HD74/txb+8+` |
| `@open-metric-fonts/rill-nova@1.0.0/rill-nova-cond-500-italic.css` | `sha384-S00R/xFQAiI2A9vD3MbUhlvlcG2Uwysfnj1Y8mBwN+xCS9g9cXgxT+7Xek55uh1r` |
| `@open-metric-fonts/rill-nova@1.0.0/rill-nova-cond-500.css` | `sha384-0OT12bRfZUQRQaj8l1DWGSXDyq+xU+VFMj90LJ5zo7LiUPtSIeQTsfIS2RP8Jy4T` |
| `@open-metric-fonts/rill-nova@1.0.0/rill-nova-cond-700-italic.css` | `sha384-R32S9GWrXfkiv5c0+NNxlNX+jeVfsec8yEnF4tpIIFMN2J5TEJ1PPcfnf6Xx+mYk` |
| `@open-metric-fonts/rill-nova@1.0.0/rill-nova-cond-700.css` | `sha384-p/HM67sICV0llQoj4IBHy3Aw++rsiK5TS6JJQlfA13HgRaO55QstkrU++0Dwzf+8` |
| `@open-metric-fonts/rill-nova@1.0.0/rill-nova-cond-lt-300-italic.css` | `sha384-bXMB3qpAWOZBY24YQPAUKTchCktrorh1AEztj02QtL6Q+JEpc0KJQDJxmfncBw37` |
| `@open-metric-fonts/rill-nova@1.0.0/rill-nova-cond-lt-300.css` | `sha384-sJAnHaxS+BLWbwxcUaNe8Ag6+v/9gEgvx359pL1bQMBQJjiuX2YQz1ULdg2kZFG6` |
| `@open-metric-fonts/rill-nova@1.0.0/rill-nova-cond-lt.css` | `sha384-g91TtOnI1dUMo55ojq5sbeabOGbyB4UQCB1MDwisNs7rN4v7rIX87JLxJ3gXHOEX` |
| `@open-metric-fonts/rill-nova@1.0.0/rill-nova-cond.css` | `sha384-mqGdawEmzIsS2cr9AX8pDKZX1TujhHa9/bMMQyB8LYiMb1NF/vHOe1BmgJYddKW1` |
| `@open-metric-fonts/rill-nova@1.0.0/rill-nova.css` | `sha384-ompa5gK09K2HC+LJqFMp+Fx4tFDZvCj9IPJE6Vl1CjBF1qzMxucN7caoo2zQdAjD` |
| `@open-metric-fonts/sawtooth@1.0.0/index.css` | `sha384-I1P7nQVsm9sKL7bBmVuQZZpiQpg4L3xnzK9bMunGuYIEvLikCX05JDudDGp0Mx6e` |
| `@open-metric-fonts/sawtooth@1.0.0/sawtooth-400-italic.css` | `sha384-lmWfaZjXugVfpr8N99XMfz6M0f5Q4X2VIfW9+pnoeQVtZsu5VrJMUlP46ZhuZa75` |
| `@open-metric-fonts/sawtooth@1.0.0/sawtooth-400.css` | `sha384-RZ1+MKUFbVjPEsalCwLeaYm/epqhzBpXl9vYoPJMNR12TyakdSS7ctcUxicZZmRY` |
| `@open-metric-fonts/sawtooth@1.0.0/sawtooth-700-italic.css` | `sha384-IebQdcFTtpfF/7H7jIFU6y9IgDa8HHZ8HnUHiLfKvXfnhPu2/DIgPwJUy7aycWyh` |
| `@open-metric-fonts/sawtooth@1.0.0/sawtooth-700.css` | `sha384-wvs1dw/97MH7vj9Ywuz+k/E+Y0gPMto1GQrot8FenALZz6DBXlOpL/rReM67Z4kb` |
| `@open-metric-fonts/sawtooth@1.0.0/sawtooth-display-400.css` | `sha384-uNTnDhCoyZHCYXda0bkLogEByiTuM6HuX+o6IGfjXIintlSM/a46bJAz8UuuBoMI` |
| `@open-metric-fonts/sawtooth@1.0.0/sawtooth-display-700.css` | `sha384-42nwRFClmuSPCPCfC9vbJoBn39oRSQCK+98wI12L9BgQF55laJdQXauNhFXZMp9T` |
| `@open-metric-fonts/sawtooth@1.0.0/sawtooth-display.css` | `sha384-HFIwECdxj8Gj1ThSV/keHkYH3un8Wjm26udgzXX7QoOXvQOVZOuN0cZugHE6nc2A` |
| `@open-metric-fonts/sawtooth@1.0.0/sawtooth.css` | `sha384-y8z1tetC+2NYHAN7aLUBp7KAi4STzUESPDLEwppmb2X1vNXxmhZpzM3m+2DbYGE/` |
| `@open-metric-fonts/scrawl@1.0.0/index.css` | `sha384-WfLwL9mw6FaqnTKi2JCZB8IHf6ptDNuEjGv8V8x/9yoCHeRwRjm4zuq86rpKtX73` |
| `@open-metric-fonts/scrawl@1.0.0/scrawl-400.css` | `sha384-WfLwL9mw6FaqnTKi2JCZB8IHf6ptDNuEjGv8V8x/9yoCHeRwRjm4zuq86rpKtX73` |
| `@open-metric-fonts/scrawl@1.0.0/scrawl.css` | `sha384-WfLwL9mw6FaqnTKi2JCZB8IHf6ptDNuEjGv8V8x/9yoCHeRwRjm4zuq86rpKtX73` |
| `@open-metric-fonts/seraphine@1.0.0/index.css` | `sha384-95ROyS5SU3cV+PHOhL+mg64/3nwxLVka5yXyfSy6iic3M9HL2tt5tU+6sn9iYGDo` |
| `@open-metric-fonts/seraphine@1.0.0/seraphine-400.css` | `sha384-95ROyS5SU3cV+PHOhL+mg64/3nwxLVka5yXyfSy6iic3M9HL2tt5tU+6sn9iYGDo` |
| `@open-metric-fonts/seraphine@1.0.0/seraphine.css` | `sha384-95ROyS5SU3cV+PHOhL+mg64/3nwxLVka5yXyfSy6iic3M9HL2tt5tU+6sn9iYGDo` |
| `@open-metric-fonts/stikine@1.0.0/index.css` | `sha384-AFcB/DypiHqRzUnf7OltwxncCUGDmrFveL+kR73RWhM1Wnw1QVbAizQR/rNq5E4h` |
| `@open-metric-fonts/stikine@1.0.0/stikine-400-italic.css` | `sha384-LcA7Sj3KJ7e0BL+M9ukiaU3CGK+m6ra2YXZh6EumwOME/YRw0DcAoiyJuoNv5KWB` |
| `@open-metric-fonts/stikine@1.0.0/stikine-400.css` | `sha384-J2R+FVWzk8lp2yV0so4zteeSqmVGWDoSODi+6BCVhXxiHwZf79OZGSA970WcVmfJ` |
| `@open-metric-fonts/stikine@1.0.0/stikine-700-italic.css` | `sha384-pJCeRByjXQYJBZkx5uzqPmwLzpI2z8HlLFksHUTyw6SBwgxatPNFm5KW/vQKGMvy` |
| `@open-metric-fonts/stikine@1.0.0/stikine-700.css` | `sha384-7LIAPp5RRaIzu69VvWvofPuHK3HtX+ZW7O7vwWguGwGgqqBsfRX1nYbf3gg6kbS7` |
| `@open-metric-fonts/stikine@1.0.0/stikine-display-400-italic.css` | `sha384-uAWgmct3brnITxM/vfX+c5ieo14AeHK8P8rnD1QrXymnVc4IEOWByPMcNrFQMFJJ` |
| `@open-metric-fonts/stikine@1.0.0/stikine-display-400.css` | `sha384-N90ZA4k8a6daONGhFEa66F1nFmqisueZ3aZD+P6B+I/MBoKzKpyepYVbaLArfvlg` |
| `@open-metric-fonts/stikine@1.0.0/stikine-display-700-italic.css` | `sha384-wz4QZeGGoS2VyyTVf9wkLZtrLne7Tqk/aPMXtAOqMJUXKqtZVQuCxx8QBZEzvqVU` |
| `@open-metric-fonts/stikine@1.0.0/stikine-display-700.css` | `sha384-G4yHZQ+rvmT2jwuFPcSQ++yZ3/B66y65cvU9Nq/sE0ZXx4MoEhY63h/GSW/EsIOg` |
| `@open-metric-fonts/stikine@1.0.0/stikine-display.css` | `sha384-bnxVBY+OIsibzijTDX0xL94Fua16UxbgoT0ZMcF7MWBsUj+RVmQ9cUwvXo3YXhg7` |
| `@open-metric-fonts/stikine@1.0.0/stikine.css` | `sha384-o44vyuQLGH4aVZm8VkthgVYFBokHqQm6bJB5sUTCU5HqMxM2rObbrva+voKSIcgH` |
| `@open-metric-fonts/tamarack@1.0.0/index.css` | `sha384-VlZHVxlhT5pjjZ7NXs5bZbPh3GPVPmt+ceIhLV32yGXLXWo+cQs7NWx4qtU5kIa8` |
| `@open-metric-fonts/tamarack@1.0.0/tamarack-400.css` | `sha384-fSGF1AP2z9ju8YNoQokOqQq3JBAY3YJ79/thRlkUxdEFIm1aeP8Nm5XAIm0xCMtc` |
| `@open-metric-fonts/tamarack@1.0.0/tamarack-700.css` | `sha384-8ywkpuaigAwY07A/l5kFPC1thUXYcditzMpDV1X9epzPefjukliDL+oOoDlJPRxF` |
| `@open-metric-fonts/tamarack@1.0.0/tamarack.css` | `sha384-VlZHVxlhT5pjjZ7NXs5bZbPh3GPVPmt+ceIhLV32yGXLXWo+cQs7NWx4qtU5kIa8` |
| `@open-metric-fonts/taper@1.0.0/index.css` | `sha384-8KQ3h5rxNHCE3ku86BlOhqtUBMbGfSY2B2f7eHLQ+XmbQ1e9iMWcs5bQWZ5fhEe1` |
| `@open-metric-fonts/taper@1.0.0/taper-400-italic.css` | `sha384-q09JebO6NTkOgYzwgEF5fvxxVUiQSzqzgEFzjwB6tZ/pwcGKuQYQiPqQSkiklMs0` |
| `@open-metric-fonts/taper@1.0.0/taper-400.css` | `sha384-FRyPZxYyM2TR6+XYrLEBQmLiUEEB5vUgkVlHT06AHpnRM4ahuSEJbjqf5c4j7U+F` |
| `@open-metric-fonts/taper@1.0.0/taper-700-italic.css` | `sha384-STRWUmgICZWXjq5CVzhALjDC6axaIlRyoDFuH+aBOTz8HQBkz04QXbpiBvcUcIK0` |
| `@open-metric-fonts/taper@1.0.0/taper-700.css` | `sha384-WZrYdCZJ7GDf5ffOZwW7Fo+2lUN/np4ZfZ5XsfIrI0VSGs0Ri0O0Ot70LkcKHidc` |
| `@open-metric-fonts/taper@1.0.0/taper-light-400-italic.css` | `sha384-9NArygk6I1pLAFICYU4o4YdmQ0f4KVq/i/SB0xKDIEBh2xrm9NjalEUM+eTzNQel` |
| `@open-metric-fonts/taper@1.0.0/taper-light-400.css` | `sha384-B5x7ca+1n/SjXS/tErB6bNXT3CatWEnmUaX0KHvj/k+i9v2+SmoTy11J0ooxjVAb` |
| `@open-metric-fonts/taper@1.0.0/taper-light.css` | `sha384-KLnwQSvf5vcT0oMG8RttiIH1nzwyhYFMpf6POzfA18Db5uI9wP3wCvbzMV/v6fg2` |
| `@open-metric-fonts/taper@1.0.0/taper.css` | `sha384-3cE1k4YXv8eyXUj2jO5ywbunf22ELK3wJ5cMXVANFcBZNoBODo4lH4v7MELXlPrL` |
| `@open-metric-fonts/tidewater@1.0.0/index.css` | `sha384-UHA+/4KzqaQjxUJosrXpyaFec9/m2khwbFdCzESJUimJkikclbgh9ufKZegtL09V` |
| `@open-metric-fonts/tidewater@1.0.0/tidewater-400-italic.css` | `sha384-gSDDbNOtt+6POF2Wma68IjKSiV2i3K6tSLotNTw3SAr67lJRfjNF52MvpEmcMdoQ` |
| `@open-metric-fonts/tidewater@1.0.0/tidewater-400.css` | `sha384-QMbp7yCBmYfEWWKAAVdlnxMSB5TOmR/u2ohbvFfJS6frvn78tkTHUYsazJHxuDVE` |
| `@open-metric-fonts/tidewater@1.0.0/tidewater-700-italic.css` | `sha384-JyJbC+vzBvBcHtcntOPrP+zx9xl1DXK2BcNLCBLQzyhHJ2PT4N3xsIieJWndPqDu` |
| `@open-metric-fonts/tidewater@1.0.0/tidewater-700.css` | `sha384-3burdqv5PlM3ON4W3XI0q3Y5a3FvnOOAggk0a1MhGgI2v97dX6DF/vqnvkPDxtty` |
| `@open-metric-fonts/tidewater@1.0.0/tidewater-display-400-italic.css` | `sha384-HUEfvGUEcvSQkaRqmLkSumrLYgM01KwjKDCVpBzBFFgNlLC/jvRklcdiIi9bJ0pg` |
| `@open-metric-fonts/tidewater@1.0.0/tidewater-display-400.css` | `sha384-KVmUfn8wOMOeqBDoylYITeVM2b3Udm0Ge2/s+wd7svVsF8GIAYK3KH7R1naw3w33` |
| `@open-metric-fonts/tidewater@1.0.0/tidewater-display.css` | `sha384-mQgjNa+Hv+r24yhSiIBPnjX/AVjQI6jCbaMS3ogAl97JH2x4GCmongZ78VljoYYI` |
| `@open-metric-fonts/tidewater@1.0.0/tidewater.css` | `sha384-bH5wo+f3SAY0RaG3O3xIX0ZjxfwW9EfbWs9ynCA8Bqzb7GFgWKQNClzfO0qqGoUA` |
| `@open-metric-fonts/tympan@1.0.0/index.css` | `sha384-WuVwjhlcPjOWSJB69oPmA/633hoXrswqCT1AK/AuBYYNP9hXyUatX+2gT27bRv4A` |
| `@open-metric-fonts/tympan@1.0.0/tympan-400-italic.css` | `sha384-tQeo2zDFdEr6/HbsylEAWcnz5lcRK8psN0RH0CPRVAqQr+5phOL1HDp6kF/iwtmE` |
| `@open-metric-fonts/tympan@1.0.0/tympan-400.css` | `sha384-K2PsonLlsUThMe3AiYseKV6o3ohERjnz8szz6r3Z29ev9DoKu9Ln//k/UX/fJ1GP` |
| `@open-metric-fonts/tympan@1.0.0/tympan-700-italic.css` | `sha384-0sBPjv2p3iIszy0lUom4zUqf7eAgdkqI/kd6EUK08pd/rB6b98dn4lAuQ2VmLPPl` |
| `@open-metric-fonts/tympan@1.0.0/tympan-700.css` | `sha384-WGff7vJpZh/Ht85c3rr+vKfsZ4yz7GGm1uy3niRYfmuGBJtGpW8mVYLO7oFlXtnJ` |
| `@open-metric-fonts/tympan@1.0.0/tympan.css` | `sha384-WuVwjhlcPjOWSJB69oPmA/633hoXrswqCT1AK/AuBYYNP9hXyUatX+2gT27bRv4A` |
| `@open-metric-fonts/ursa@1.0.0/index.css` | `sha384-i05a5g+hxURLjW95+burk0W9Qg1PE+lVYCriQ/YxbHaKFqbpdksoqJ0eqVMLu5WD` |
| `@open-metric-fonts/ursa@1.0.0/ursa-400-italic.css` | `sha384-seHEc296DbdAkMhIkIVkPb2+ZA9VBiPtMGTj/IPDTXYGxIxFgcHXfG62zjrz4PmH` |
| `@open-metric-fonts/ursa@1.0.0/ursa-400.css` | `sha384-h8NIA3p/hxVnTVraJeQIiRUuGpIdRHDUVgsLI5ZLdr75vj8J58FOoOmLMOtfBKzx` |
| `@open-metric-fonts/ursa@1.0.0/ursa-700-italic.css` | `sha384-SyEVQ4dG9KWQT4lvRgyMirYtDJu4VBjq0sZQl1KLAkShhht38Axjk/q6d3fi5biq` |
| `@open-metric-fonts/ursa@1.0.0/ursa-700.css` | `sha384-X3mXx9EIhOiorJS54tuodU4EpLZrvVbPmYweMRSKRYKUY99NokO/A1tl9ERi+Npt` |
| `@open-metric-fonts/ursa@1.0.0/ursa.css` | `sha384-i05a5g+hxURLjW95+burk0W9Qg1PE+lVYCriQ/YxbHaKFqbpdksoqJ0eqVMLu5WD` |
| `@open-metric-fonts/vellum@1.0.0/index.css` | `sha384-FCyk0LGQLVAUJYHArHaK8iJWDYJGgpa1Nb0Ksv+8KK8qtwvlyut5J6oBTdXrY1ZZ` |
| `@open-metric-fonts/vellum@1.0.0/vellum-400-italic.css` | `sha384-TkiYKFLbO3qyxkJKKtagoU5tUeo2L5WoYwqpEWeKc0kpDrrPJTc6k9b+b8uijNIu` |
| `@open-metric-fonts/vellum@1.0.0/vellum-400.css` | `sha384-Bs6Yk+H6gyK88pLghB/dO8n+Rtn0F3jMfRz5UtxNU8U24hU5x2dJ5ww4QNUL6RnV` |
| `@open-metric-fonts/vellum@1.0.0/vellum-700-italic.css` | `sha384-hj5EhDBZgT3C0RwI5elrYpVd7MI7NPmF/hpD1ZueDGWFac+x3U7GW2G/E9hGk31U` |
| `@open-metric-fonts/vellum@1.0.0/vellum-700.css` | `sha384-64AOEkVulfZfqen4lmOS+vJ/lB+hi6ORJFfWNKM4F2Xm/47EjbZ/3VL0RBO84ff2` |
| `@open-metric-fonts/vellum@1.0.0/vellum.css` | `sha384-FCyk0LGQLVAUJYHArHaK8iJWDYJGgpa1Nb0Ksv+8KK8qtwvlyut5J6oBTdXrY1ZZ` |
| `@open-metric-fonts/weimar@1.0.0/index.css` | `sha384-j9JDzqJEhXX7Pq32KOANblsv6HEw+q797Hv2yGeJ7LRmbbLdtTyiWMNADljhIneO` |
| `@open-metric-fonts/weimar@1.0.0/weimar-display-400-italic.css` | `sha384-+3um2saTPGoqphv3ObeMa5cK+R5yxWRacKiaNz0ilnvbYqhgFr3337ShA+apzCQU` |
| `@open-metric-fonts/weimar@1.0.0/weimar-display-400.css` | `sha384-NuvRpNe6hL8YFsilKbe84zcGEzSoeL35H0aA3rfHR5BwWs9+UiJ+cBUgv/Z5DDeP` |
| `@open-metric-fonts/weimar@1.0.0/weimar-display-700-italic.css` | `sha384-+EMyfqFp2ozSc/ynlAXPtTErTokC64/nLEwNRvezWWdTafGp1Hu8yJt+JUhOWTIw` |
| `@open-metric-fonts/weimar@1.0.0/weimar-display-700.css` | `sha384-pIftDX4ngLYzGMpDi5QKdc42Mk436kmcRn94xuvkt9oRhYtKrSU4Kin2kMoDtq28` |
| `@open-metric-fonts/weimar@1.0.0/weimar-display.css` | `sha384-JMp1OwO0SNJ1DqTKpvrc88JrBn3O/sKQggg2xOMdV2r8d6xAkIcbkRWGLvFjvbCF` |
| `@open-metric-fonts/weimar@1.0.0/weimar-heading-400-italic.css` | `sha384-QRsp0voQB2xjn/HRwwIkn5a5VkDZz8dcTbw++rz58vSaxb/duBdtIkYYiuEi4SWb` |
| `@open-metric-fonts/weimar@1.0.0/weimar-heading-400.css` | `sha384-Yv93M1T3jJ3zXiYW5dBSTObgiN8ULAI3mYxF/LF92k+0xG9Cqs3MsYM0wJh4S5Ok` |
| `@open-metric-fonts/weimar@1.0.0/weimar-heading-700-italic.css` | `sha384-sH77IVfx8Ycsn2a0TSB4DYyh3HYCCQbP8yaimA0wSclcsycZ3f+uxWpYo+H1DdZC` |
| `@open-metric-fonts/weimar@1.0.0/weimar-heading-700.css` | `sha384-HEPoSBvgUx+NMJKcJ+GooE5nG6T4fEt/5KD25DaKDtBSA8J5DY7bsXWKVWG5cRlZ` |
| `@open-metric-fonts/weimar@1.0.0/weimar-heading.css` | `sha384-RddLUUwvYNZ68F2C/2RIPCqPtoKvFQwJli5wtQzWxC2EACKXw8Ue8TpusNS8/1kx` |
| `@open-metric-fonts/weimar@1.0.0/weimar-text-400-italic.css` | `sha384-0tNub3j1o1HT0Y6hFE2jXv7PNRoGHFeem4YeSBvQECD/gCpasbbYfvZPE6kk/JTN` |
| `@open-metric-fonts/weimar@1.0.0/weimar-text-400.css` | `sha384-1LYqrQbW2Hac42YYsxfb8E0qFeiuW+dFbz7J5sN/VCAbPbu9pHgkcUxbrTHkjoyP` |
| `@open-metric-fonts/weimar@1.0.0/weimar-text-700-italic.css` | `sha384-8/XOpm5yxwhieRuBpCR3/WnC4lKq/OMNbCWpss+DSchupq/1O9/hkV7lXs87L40E` |
| `@open-metric-fonts/weimar@1.0.0/weimar-text-700.css` | `sha384-vHqhy2Bpd7kzYIAfJ+02+LLisSfG0fHO3s+qMMVWYNYWR63WAKeMk4I1G0glVtoK` |
| `@open-metric-fonts/weimar@1.0.0/weimar-text.css` | `sha384-cHwqkeQfCTzuvXUji3UOm3NP+XFzOCIPhe9Sw10aSQFFnoomJL23+ZDk8kHU+QuT` |
| `@open-metric-fonts/wharf@1.0.0/index.css` | `sha384-hNxYxoDjKcmmmyATBNNjWg7JCL4Gm3ULCtcuEjI7Th9+l0cGXOBTstovqC0D71Lw` |
| `@open-metric-fonts/wharf@1.0.0/wharf-300-italic.css` | `sha384-Sd2KIxcnUfJXaI7iLrVuIhX5aUEZsKN7Stc7Lk0D2ikLYCxo5E3pVAFS9TalWCvp` |
| `@open-metric-fonts/wharf@1.0.0/wharf-300.css` | `sha384-p5rVgk5q/Qu99KoeEkwI0cRntagr94/awxpLdFTp/EJ1NFUhDOTY3ByS6OWznm4y` |
| `@open-metric-fonts/wharf@1.0.0/wharf-400-italic.css` | `sha384-+HnEhUys2FrLz/IBBwWyZx2GUhMEM6+7rh7phLrOyRhEivBdjRZR3A9BXhE3Zvgt` |
| `@open-metric-fonts/wharf@1.0.0/wharf-400.css` | `sha384-AWtf8BkEA9wi+IMKXBHNn9ZBPwmEmaZ9Bh+F0asZyqFhDMpYaIF+i/Fa37f5vIkX` |
| `@open-metric-fonts/wharf@1.0.0/wharf-700-italic.css` | `sha384-9+vnzU7PJQlBn8YyOSVS2CUIkF5Sjyzel8UOwybd+DQKLneZopnj862jrSwFxo0K` |
| `@open-metric-fonts/wharf@1.0.0/wharf-700.css` | `sha384-l1IyuGgrhBsVbzP3wV6kP/JzMJFLEGrTU4VvEEMbCZBu4vIlGdtnEh2HFHw97ilE` |
| `@open-metric-fonts/wharf@1.0.0/wharf-condensed-400-italic.css` | `sha384-oDLDh55IGKlMLKI/uybcHJ5fo5gSPFpqgdKxMygtIYa/lmjkFAtgslwPNJTNwGF6` |
| `@open-metric-fonts/wharf@1.0.0/wharf-condensed-400.css` | `sha384-f+rJ5vlLT6+c8fr7Z5aGnmUVJlBLldLtGvV3PLjWPkgSEm0J8a6AEN0astEzwBZa` |
| `@open-metric-fonts/wharf@1.0.0/wharf-condensed-700-italic.css` | `sha384-5I74hKbo5k10jLNMdx+SQu9wTipaIzbyScgMwMJI8AOsgsZUIWz9MH5mYxy+KQec` |
| `@open-metric-fonts/wharf@1.0.0/wharf-condensed-700.css` | `sha384-wDozmm4m5nbi/6VKatcvoQZ3STimTjL5iptjRulWs5LsKoG5MKyPpCkxRs8Rc1w9` |
| `@open-metric-fonts/wharf@1.0.0/wharf-condensed-800-italic.css` | `sha384-ePk00l2b7EDCthtVYokjc7x1SUqbUYIAQcH2oVzLwO0Ho1lhtJAHq0uHhQBLN4av` |
| `@open-metric-fonts/wharf@1.0.0/wharf-condensed-800.css` | `sha384-Oml2QobZ2If0YMeW5B2qPjDOM1TLLMkkSf2/7pAFg64IY2AuoCT0+qgd/Lh/6Yt5` |
| `@open-metric-fonts/wharf@1.0.0/wharf-condensed.css` | `sha384-RXBz1f9SmrC859zlg6J5B/eGW6OsDX5MCews4NwBee0W9sMZu8qnIQJuhgtSjBrC` |
| `@open-metric-fonts/wharf@1.0.0/wharf.css` | `sha384-IvQ8rthol189v0sd4NqZTLegw9R3romtvq96tSkvc8HVQTW/K/mwPhZGhnTxqTWV` |
| `@open-metric-fonts/zenith@1.0.0/index.css` | `sha384-gAfp2KuhvZS5l9R0BLM1vhzSFfPfn9/KP/JZpuTGtfvUUV3CosnVDgl6AJWuJ0mw` |
| `@open-metric-fonts/zenith@1.0.0/zenith-400-italic.css` | `sha384-5W9vnDyuMPT5bJAP/maiKl945mNs1NjQzjpvoVPkGhjXbE2h9lgeoYhU/4Xnt5BW` |
| `@open-metric-fonts/zenith@1.0.0/zenith-400.css` | `sha384-yF5qfrxXVmxoB0k/D1ps8oFj1Uldzq7Bw/6fXqd6WpsMewG2YLW4EA51K+YyoFvD` |
| `@open-metric-fonts/zenith@1.0.0/zenith-700-italic.css` | `sha384-6hxtu7lX7KN4a+WP9TEvHw+Q7c3LDnthkBgicv8najJhHZMuKichOyLqLEHXW/zA` |
| `@open-metric-fonts/zenith@1.0.0/zenith-700.css` | `sha384-O0R0KPXW0MDCvlXW93SZFG2YptPH0/bIIttRbkPpgshBxZP7m4GEuDsXTAQb96u2` |
| `@open-metric-fonts/zenith@1.0.0/zenith-condensed-400.css` | `sha384-PjsP5oagORh8Jul1awEQLG1iUxtWCFnzmr6VGmPMSNnFUZ6X1JEwrIUpdBtzCQwp` |
| `@open-metric-fonts/zenith@1.0.0/zenith-condensed-700.css` | `sha384-Vuackx4ij9s7qElmsaAhaxmqyoo+QFWhWvqw1zFkIK/KayWXc6r9K2yCvgw09Rbw` |
| `@open-metric-fonts/zenith@1.0.0/zenith-condensed-extra-bold-400.css` | `sha384-qT/7C/0dtQBmy8R4ykxq9VNneTA1i7aRMzhUHW0BUZaS3++g0KMuSaI5MXfgcGfn` |
| `@open-metric-fonts/zenith@1.0.0/zenith-condensed-extra-bold.css` | `sha384-qT/7C/0dtQBmy8R4ykxq9VNneTA1i7aRMzhUHW0BUZaS3++g0KMuSaI5MXfgcGfn` |
| `@open-metric-fonts/zenith@1.0.0/zenith-condensed.css` | `sha384-Yti/iXj5go18huqv4Pq71Ffpx2QmOaFchmb4NFQh7lJWLCrNYu4R8J3s4j/5u8cP` |
| `@open-metric-fonts/zenith@1.0.0/zenith.css` | `sha384-m+fvZJUlPCz8pyusul7rlvSZQOhe0HSkdo7ibJ7Oc6NtgOSuKwQ+DQFLMuDHhF2O` |
