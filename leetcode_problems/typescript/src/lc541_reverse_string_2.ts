function reverseSubStr(s: string[], p1: number, p2: number) {
  while (p1 < p2) {
    let temp = s[p1];
    s[p1] = s[p2];
    s[p2] = temp;
    p1++;
    p2--;
  }
}

function reverseStr(s: string, k: number): string {
  let str = Array.from(s);
  for (let i = 0; i < str.length; i += 2 * k) {
    reverseSubStr(str, i, Math.min(i + k - 1, str.length - 1));
  }
  return str.join("");
}
