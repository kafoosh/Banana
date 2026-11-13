// The last page of the booklet: one margin doodle per drawing, as a
// ten-year-old would do it. Plain pencil line, 160 x 120, no fills.
// The #pencil filter in index.html gives the line its wobble and grain.

const wrap = (d) => `<svg viewBox="0 0 160 120" aria-hidden="true"><g filter="url(#pencil)">${d}</g></svg>`;

export const DOODLES = {
  house: wrap(`
    <path d="M38 104 40 58l82-2-1 48z"/>
    <path d="M30 61 81 20l52 39"/>
    <path d="M72 104V79h17l1 25"/>
    <path d="M48 67h14v13H48zM101 67h13l1 13h-14z"/>`),

  sun: wrap(`
    <ellipse cx="80" cy="60" rx="24" ry="23"/>
    <path d="M80 30V12M80 90v18M110 60h20M50 60H30M101 39l13-13M59 81 46 94M101 81l13 13M59 39 46 26M92 33l6-15M68 87l-6 15"/>`),

  fish: wrap(`
    <path d="M28 60Q68 22 112 58 70 97 28 60z"/>
    <path d="M112 58l28-20-2 43z"/>
    <circle cx="47" cy="55" r="3"/>
    <path d="M63 46q7 13-1 27"/>`),

  tree: wrap(`
    <path d="M71 108l2-38M91 108l-3-38"/>
    <path d="M58 72Q34 68 42 48 36 26 62 26 72 8 92 22q26-4 24 20 16 16-8 28-24 10-50 2z"/>
    <path d="M48 108h66"/>`),

  flower: wrap(`
    <path d="M80 112q-3-24 1-44"/>
    <circle cx="81" cy="44" r="9"/>
    <path d="M81 35q-9-16 0-24 10 8 0 24M90 44q16-9 24 0-8 10-24 0M81 53q9 16 0 24-10-8 0-24M72 44q-16 9-24 0 8-10 24 0M88 38q6-17 18-16 0 13-18 16M88 50q17 6 16 18-13 0-16-18M74 50q-6 17-18 16 0-13 18-16M74 38q-17-6-16-18 13 0 16 18"/>
    <path d="M80 94q18-15 25-5-12 11-25 5"/>`),

  pencil: wrap(`
    <path d="M22 78 106 34l8 15-84 44z"/>
    <path d="M106 34l28-4-20 19"/>
    <path d="M126 31l8-1-6 6"/>
    <path d="M31 73l8 15"/>`),

  moon: wrap(`<path d="M92 16a45 45 0 1 0 28 76 35 35 0 1 1-28-76z"/>`),

  glass: wrap(`
    <ellipse cx="80" cy="26" rx="26" ry="6"/>
    <path d="M54 26l9 76q17 5 35 0l8-76"/>
    <path d="M58 58q22 6 45 0"/>`),

  ball: wrap(`
    <ellipse cx="80" cy="60" rx="35" ry="34"/>
    <path d="M50 43q30 15 60-1M49 78q31-16 62 1M80 26q9 34 0 68"/>`),

  car: wrap(`
    <path d="M20 84l2-20 26-3 12-20h40l14 20 24 4 1 19z"/>
    <path d="M64 60l5-13h27l8 13z"/>
    <circle cx="50" cy="86" r="11"/>
    <circle cx="112" cy="86" r="11"/>`),

  plane: wrap(`
    <path d="M20 62q2-10 22-10h80q20 2 22 10-4 8-22 8H42q-18 0-22-8z"/>
    <path d="M72 52 58 20h16l20 32M72 70l-14 32h16l20-32"/>
    <path d="M32 53l-8-20h12l10 19"/>
    <circle cx="106" cy="61" r="2.500"/><circle cx="118" cy="61" r="2.500"/><circle cx="130" cy="61" r="2.500"/>`),

  cat: wrap(`
    <path d="M51 66q-1-30 29-31 31 1 30 31 0 29-30 30-29-1-29-30z"/>
    <path d="M55 48 52 16l22 20M105 48l4-32-22 20"/>
    <circle cx="68" cy="60" r="3"/><circle cx="93" cy="60" r="3"/>
    <path d="M77 71h7l-4 5zM80 76q-1 8-9 7M80 76q1 8 9 7"/>
    <path d="M62 72 36 66M62 76l-27 2M62 80l-24 9M99 72l26-6M99 76l27 2M99 80l24 9"/>`),

  stickman: wrap(`
    <circle cx="80" cy="24" r="12"/>
    <path d="M80 36l1 42M55 54l25-6 26 7M81 78 62 110M81 78l19 32"/>`),

  table: wrap(`
    <path d="M24 46l112-2 1 10-113 2z"/>
    <path d="M36 56l-2 50M126 54l2 52M60 56l-1 36M106 55l1 37"/>`),

  boat: wrap(`
    <path d="M28 78l104-2-17 22H44z"/>
    <path d="M80 77V16"/>
    <path d="M85 22v48h37z"/>
    <path d="M12 108q9-9 17 0t17 0 17 0 17 0 17 0 17 0 17 0"/>`),

  heart: wrap(`<path d="M80 102C40 73 25 50 40 34c14-13 34-6 40 10 6-17 28-23 40-8 13 17-2 38-40 66z"/>`),

  star: wrap(`<path d="M80 12l23 88-76-55h106L57 100z"/>`),
};
