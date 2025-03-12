function reverseVowels(str: string): string {
  let vow: Map<string, boolean> = new Map([
    ["A", true],
    ["a", true],
    ["E", true],
    ["e", true],
    ["I", true],
    ["i", true],
    ["O", true],
    ["o", true],
    ["U", true],
    ["u", true],
  ]);
  let s = Array.from(str);

  let p1 = 0;
  let p2 = s.length - 1;
  while (p1 < p2) {
    while (p1 < p2 && p1 < s.length && !(vow.get(s[p1]) || false)) {
      p1++;
    }
    while (p1 < p2 && p2 >= 0 && !(vow.get(s[p2]) || false)) {
      p2--;
    }
    if (p1 >= p2) {
      break;
    }
    let temp = s[p1];
    s[p1] = s[p2];
    s[p2] = temp;
    p1++;
    p2--;
  }
  return s.join("");
}
