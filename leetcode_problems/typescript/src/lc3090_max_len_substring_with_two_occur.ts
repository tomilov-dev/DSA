function maximumLengthSubstring(s: string): number {
  let map: Map<string, number> = new Map();
  map.set(s[0], 1);
  map.set(s[1], (map.get(s[1]) || 0) + 1);
  let max = 2;
  let p1 = 0;
  for (let p2 = 2; p2 < s.length; p2++) {
    map.set(s[p2], (map.get(s[p2]) || 0) + 1);
    while (p1 < s.length && (map.get(s[p2]) || 0) > 2) {
      map.set(s[p1], (map.get(s[p1]) || 0) - 1);
      p1++;
    }
    max = Math.max(max, p2 - p1 + 1);
  }
  return max;
}
