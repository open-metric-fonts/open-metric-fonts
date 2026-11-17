# Known differences

Every font has the same letter widths, line heights and spacing rules as the Microsoft font it replaces, so a document breaks its lines and pages in the same places. A few things still differ. They are listed here with their cause and what they affect.

## Bold applied to a SemiBold or Demi font in Word

**Affects:** Aptos SemiBold, Avenir Next LT Pro Demi, Georgia Pro Semibold and Verdana Pro Semibold, only in text where **Bold is also switched on**.

**Cause:** these four are Microsoft 365 cloud fonts. When Bold is applied on top of them, Word draws a simulated (faked) bold version that is slightly wider, so the text takes more room and lines can break later. Word does not do this for fonts installed on the computer, including Microsoft's own Segoe UI Semibold, and no other program does it.

**What it means for you:**

- In LibreOffice, and anywhere else these fonts stand in for the Microsoft ones, the document lays out exactly as it does with the Microsoft fonts in the same program.
- Only a document that uses this combination and is moved between Word and another program can break lines differently, and it does so with the Microsoft fonts too.
- Regular, italic and normal bold text is not affected.

## Characters no open font has

**Affects:** private-use characters some Microsoft fonts carry, such as the Apple logo (U+F8FF) in Segoe UI.

**Cause:** these are not standard Unicode characters, and no openly licensed font has them.

**What it means for you:** they are shown from a fallback font. They keep their width, so the layout does not change.

## Letter shapes

**Affects:** all fonts.

**Cause:** every letter is drawn from an openly licensed font, so it looks like that font, not like the Microsoft one. Where the Microsoft font draws a letter much wider or narrower, the letter is stretched or squeezed to fit, with its strokes kept at the same weight. A few letters differ more visibly. For example, the J in the Gill Sans replacements (Rill and Rill Nova) sits on the baseline, while the Microsoft J drops below it.

**What it means for you:** documents look slightly different but lay out the same. If a letter looks wrong, please open an issue with a screenshot.
