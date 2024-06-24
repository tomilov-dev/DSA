function swapCase(char: string): string {
  if (char === char.toUpperCase()) {
    char = char.toLowerCase();
  } else {
    char = char.toLocaleUpperCase();
  }
  return char;
}

function longestNiceSubstring(s: string): string {
  if (s.length === 0) {
    return "";
  }

  let charset = new Set(s);
  for (let index = 0; index < s.length; index++) {
    if (!charset.has(swapCase(s[index]))) {
      let s0 = longestNiceSubstring(s.slice(0, index));
      let s1 = longestNiceSubstring(s.slice(index + 1, s.length));

      if (s0.length >= s1.length) {
        return s0;
      } else {
        return s1;
      }
    }
  }

  return s;
}
