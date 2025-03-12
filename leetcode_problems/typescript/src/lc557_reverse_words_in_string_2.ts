function reverseWord(s: string[], p1: number, p2: number) {
  while (p1 < p2) {
    let temp = s[p1];
    s[p1] = s[p2];
    s[p2] = temp;
    p1++;
    p2--;
  }
}

function reverseWords(s: string): string {
  let str = Array.from(s);
  let p1 = 0;
  let p2 = 0;
  while (p1 < str.length && p2 < str.length) {
    while (p2 < str.length && s[p2] != " ") {
      p2++;
    }
    reverseWord(str, p1, p2 - 1);
    p1 = p2 + 1;
    p2 = p1;
  }
  return str.join("");
}
