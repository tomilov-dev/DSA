function reverse_word(word: string): string {
  return word.split("").reverse().join("");
}

function maximumNumberOfStringPairs(words: string[]): number {
  let res: number = 0;
  let map: Map<string, number> = new Map();
  for (let word of words) {
    let rev = reverse_word(word);
    res += map.get(word) || 0;
    map.set(rev, (map.get(rev) || 0) + 1);
  }
  return res;
}

console.log(maximumNumberOfStringPairs(["cd", "ac", "dc", "ca", "zz"]));
