function maxNumberOfBalloons(text: string): number {
  let min_count = 10 ** 4 + 1;
  const char_count = new Map<string, number>();
  const word = new Map<string, number>([
    ["b", 1],
    ["a", 1],
    ["l", 2],
    ["o", 2],
    ["n", 1],
  ]);

  for (let char of text) {
    char_count.set(char, (char_count.get(char) || 0) + 1);
  }

  word.forEach((v, k) => {
    min_count = Math.min(min_count, Math.floor((char_count.get(k) || 0) / v));
  });

  return min_count;
}

console.log(maxNumberOfBalloons("nlaebolko"));
