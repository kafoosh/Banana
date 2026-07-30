// Reveal art: deliberately crude 90s clip-art, one SVG per out.
// Style contract: 120x110 viewBox, fat #1c1a16 outlines, garish flat fills.

const S = 'stroke="#1c1a16" stroke-linejoin="round" stroke-linecap="round"';

export const ART = {
  house: `<svg viewBox="0 0 120 110">
    <rect x="80" y="16" width="12" height="24" fill="#b0483a" ${S} stroke-width="5"/>
    <polygon points="60,6 12,48 108,48" fill="#c0392b" ${S} stroke-width="6"/>
    <rect x="22" y="48" width="76" height="50" fill="#e8b84b" ${S} stroke-width="6"/>
    <rect x="52" y="66" width="16" height="32" fill="#8a5a2b" ${S} stroke-width="5"/>
    <rect x="30" y="58" width="14" height="14" fill="#9ad1e8" ${S} stroke-width="5"/>
    <rect x="76" y="58" width="14" height="14" fill="#9ad1e8" ${S} stroke-width="5"/>
  </svg>`,

  sun: `<svg viewBox="0 0 120 110">
    <g ${S} stroke-width="6">
      <line x1="60" y1="4" x2="60" y2="20"/><line x1="60" y1="90" x2="60" y2="106"/>
      <line x1="9" y1="55" x2="25" y2="55"/><line x1="95" y1="55" x2="111" y2="55"/>
      <line x1="24" y1="19" x2="35" y2="30"/><line x1="85" y1="80" x2="96" y2="91"/>
      <line x1="96" y1="19" x2="85" y2="30"/><line x1="35" y1="80" x2="24" y2="91"/>
    </g>
    <circle cx="60" cy="55" r="30" fill="#f2d24b" ${S} stroke-width="6"/>
    <circle cx="50" cy="48" r="3.4" fill="#1c1a16"/><circle cx="70" cy="48" r="3.4" fill="#1c1a16"/>
    <path d="M48 63 Q60 73 72 63" fill="none" ${S} stroke-width="5"/>
  </svg>`,

  fish: `<svg viewBox="0 0 120 110">
    <circle cx="97" cy="26" r="5" fill="none" ${S} stroke-width="4"/>
    <circle cx="106" cy="14" r="3.4" fill="none" ${S} stroke-width="4"/>
    <polygon points="18,55 40,38 40,72" fill="#e07a9a" ${S} stroke-width="5"/>
    <ellipse cx="68" cy="55" rx="34" ry="22" fill="#9ad1e8" ${S} stroke-width="6"/>
    <path d="M62 37 Q72 55 62 73" fill="none" ${S} stroke-width="4"/>
    <circle cx="85" cy="50" r="3.6" fill="#1c1a16"/>
  </svg>`,

  tree: `<svg viewBox="0 0 120 110">
    <rect x="52" y="62" width="16" height="42" fill="#8a5a2b" ${S} stroke-width="6"/>
    <circle cx="40" cy="46" r="22" fill="#6aa84f" ${S} stroke-width="6"/>
    <circle cx="80" cy="46" r="22" fill="#6aa84f" ${S} stroke-width="6"/>
    <circle cx="60" cy="30" r="24" fill="#6aa84f" ${S} stroke-width="6"/>
  </svg>`,

  flower: `<svg viewBox="0 0 120 110">
    <line x1="60" y1="58" x2="60" y2="104" ${S} stroke-width="6"/>
    <ellipse cx="74" cy="88" rx="13" ry="7" fill="#6aa84f" ${S} stroke-width="5" transform="rotate(-24 74 88)"/>
    <g fill="#e07a9a" ${S} stroke-width="5">
      <ellipse cx="60" cy="16" rx="10" ry="14"/><ellipse cx="60" cy="60" rx="10" ry="14"/>
      <ellipse cx="38" cy="38" rx="14" ry="10"/><ellipse cx="82" cy="38" rx="14" ry="10"/>
      <ellipse cx="44" cy="22" rx="11" ry="11"/><ellipse cx="76" cy="22" rx="11" ry="11"/>
      <ellipse cx="44" cy="54" rx="11" ry="11"/><ellipse cx="76" cy="54" rx="11" ry="11"/>
    </g>
    <circle cx="60" cy="38" r="13" fill="#f2d24b" ${S} stroke-width="5"/>
  </svg>`,

  pencil: `<svg viewBox="0 0 120 110">
    <g transform="rotate(-38 60 55)">
      <rect x="20" y="44" width="66" height="22" fill="#f2d24b" ${S} stroke-width="5"/>
      <rect x="10" y="44" width="10" height="22" fill="#e07a9a" ${S} stroke-width="5"/>
      <polygon points="86,44 108,55 86,66" fill="#efe3c0" ${S} stroke-width="5"/>
      <polygon points="100,51 108,55 100,59" fill="#1c1a16" stroke="none"/>
      <line x1="86" y1="44" x2="86" y2="66" ${S} stroke-width="4"/>
    </g>
  </svg>`,

  moon: `<svg viewBox="0 0 120 110">
    <path d="M78 10 A46 46 0 1 0 78 100 A38 38 0 1 1 78 10 Z" fill="#f2d24b" ${S} stroke-width="6"/>
    <g fill="#f2d24b" ${S} stroke-width="3.5">
      <polygon points="88,22 91,29 98,29 92,34 94,41 88,37 82,41 84,34 78,29 85,29"/>
      <polygon points="100,52 103,59 110,59 104,64 106,71 100,67 94,71 96,64 90,59 97,59"/>
      <polygon points="86,78 89,85 96,85 90,90 92,97 86,93 80,97 82,90 76,85 83,85"/>
    </g>
  </svg>`,

  glass: `<svg viewBox="0 0 120 110">
    <polygon points="24,12 96,12 60,52" fill="#9ad1e8" ${S} stroke-width="6"/>
    <line x1="60" y1="52" x2="60" y2="92" ${S} stroke-width="6"/>
    <line x1="38" y1="98" x2="82" y2="98" ${S} stroke-width="6"/>
    <circle cx="47" cy="24" r="7" fill="#6aa84f" ${S} stroke-width="4"/>
    <line x1="47" y1="17" x2="47" y2="6" ${S} stroke-width="4"/>
  </svg>`,

  ball: `<svg viewBox="0 0 120 110">
    <circle cx="60" cy="55" r="42" fill="#e8853b" ${S} stroke-width="6"/>
    <line x1="60" y1="13" x2="60" y2="97" ${S} stroke-width="5"/>
    <line x1="18" y1="55" x2="102" y2="55" ${S} stroke-width="5"/>
    <path d="M32 25 Q60 48 88 25" fill="none" ${S} stroke-width="5"/>
    <path d="M32 85 Q60 62 88 85" fill="none" ${S} stroke-width="5"/>
  </svg>`,

  car: `<svg viewBox="0 0 120 110">
    <path d="M14 62 L22 44 Q26 36 36 36 L74 36 Q82 36 90 46 L104 62 Z" fill="#c0392b" ${S} stroke-width="6"/>
    <rect x="10" y="62" width="100" height="20" rx="6" fill="#c0392b" ${S} stroke-width="6"/>
    <rect x="40" y="42" width="22" height="20" fill="#9ad1e8" ${S} stroke-width="5"/>
    <circle cx="34" cy="86" r="12" fill="#4a4a4a" ${S} stroke-width="6"/>
    <circle cx="86" cy="86" r="12" fill="#4a4a4a" ${S} stroke-width="6"/>
  </svg>`,

  plane: `<svg viewBox="0 0 120 110">
    <ellipse cx="60" cy="58" rx="46" ry="13" fill="#cfd8e8" ${S} stroke-width="6"/>
    <polygon points="52,50 30,20 44,20 66,48" fill="#c0392b" ${S} stroke-width="5"/>
    <polygon points="52,66 34,92 48,92 66,68" fill="#c0392b" ${S} stroke-width="5"/>
    <polygon points="100,50 116,38 112,54" fill="#c0392b" ${S} stroke-width="5"/>
    <g fill="#1c1a16"><circle cx="34" cy="57" r="2.6"/><circle cx="46" cy="57" r="2.6"/><circle cx="58" cy="57" r="2.6"/><circle cx="70" cy="57" r="2.6"/></g>
  </svg>`,

  cat: `<svg viewBox="0 0 120 110">
    <polygon points="30,26 36,4 50,20" fill="#e8853b" ${S} stroke-width="5"/>
    <polygon points="90,26 84,4 70,20" fill="#e8853b" ${S} stroke-width="5"/>
    <circle cx="60" cy="42" r="30" fill="#e8853b" ${S} stroke-width="6"/>
    <circle cx="48" cy="36" r="3.6" fill="#1c1a16"/><circle cx="72" cy="36" r="3.6" fill="#1c1a16"/>
    <polygon points="56,46 64,46 60,52" fill="#1c1a16"/>
    <g ${S} stroke-width="3.5">
      <line x1="20" y1="42" x2="42" y2="46"/><line x1="20" y1="54" x2="42" y2="52"/>
      <line x1="100" y1="42" x2="78" y2="46"/><line x1="100" y1="54" x2="78" y2="52"/>
      <path d="M52 56 Q60 62 68 56"/>
    </g>
    <path d="M60 72 Q90 70 92 96 L28 96 Q30 70 60 72 Z" fill="#e8853b" ${S} stroke-width="6"/>
  </svg>`,

  stickman: `<svg viewBox="0 0 120 110">
    <circle cx="60" cy="24" r="16" fill="#efe3c0" ${S} stroke-width="6"/>
    <circle cx="54" cy="21" r="2.6" fill="#1c1a16"/><circle cx="66" cy="21" r="2.6" fill="#1c1a16"/>
    <path d="M53 30 Q60 35 67 30" fill="none" ${S} stroke-width="4"/>
    <g ${S} stroke-width="6" fill="none">
      <line x1="60" y1="40" x2="60" y2="74"/>
      <line x1="60" y1="48" x2="26" y2="42"/><line x1="60" y1="48" x2="94" y2="42"/>
      <line x1="60" y1="74" x2="40" y2="102"/><line x1="60" y1="74" x2="80" y2="102"/>
    </g>
  </svg>`,

  table: `<svg viewBox="0 0 120 110">
    <rect x="12" y="34" width="96" height="14" rx="3" fill="#8a5a2b" ${S} stroke-width="6"/>
    <g ${S} stroke-width="6">
      <line x1="24" y1="48" x2="20" y2="98"/><line x1="96" y1="48" x2="100" y2="98"/>
      <line x1="44" y1="48" x2="44" y2="88"/><line x1="76" y1="48" x2="76" y2="88"/>
    </g>
  </svg>`,

  boat: `<svg viewBox="0 0 120 110">
    <line x1="60" y1="10" x2="60" y2="66" ${S} stroke-width="5"/>
    <polygon points="60,12 60,56 24,56" fill="#f2d24b" ${S} stroke-width="5"/>
    <polygon points="66,20 66,50 98,50" fill="#c0392b" ${S} stroke-width="5"/>
    <polygon points="18,66 102,66 88,88 32,88" fill="#5b8bd0" ${S} stroke-width="6"/>
    <path d="M8 98 q6 -7 12 0 q6 7 12 0 q6 -7 12 0 q6 7 12 0 q6 -7 12 0 q6 7 12 0 q6 -7 12 0 q6 7 12 0" fill="none" ${S} stroke-width="4"/>
  </svg>`,

  heart: `<svg viewBox="0 0 120 110">
    <path d="M60 96 C20 68 10 40 24 24 C36 11 54 16 60 32 C66 16 84 11 96 24 C110 40 100 68 60 96 Z" fill="#c0392b" ${S} stroke-width="6"/>
    <path d="M34 32 Q28 38 30 46" fill="none" stroke="#efe3c0" stroke-width="5" stroke-linecap="round"/>
  </svg>`,

  star: `<svg viewBox="0 0 120 110">
    <polygon points="60,4 73,40 111,40 80,62 92,100 60,76 28,100 40,62 9,40 47,40" fill="#f2d24b" ${S} stroke-width="6"/>
  </svg>`,
};

// reveal segment id -> out name, used only by the ?debug=1 overlay
export const OUT_NAMES = {
  36: 'FISH', 37: 'HOUSE', 38: 'SUN', 39: 'TREE', 40: 'FLOWER', 41: 'PENCIL',
  42: 'MOON', 43: 'GLASS', 44: 'BALL', 45: 'CAR', 46: 'PLANE', 47: 'CAT',
  48: 'STICKMAN', rman: 'STICKMAN', 49: 'TABLE', 50: 'BOAT', 51: 'HEART', 52: 'STAR',
};
