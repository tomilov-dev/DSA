function arraysEqual(arr1: boolean[], arr2: boolean[]): boolean {
  if (arr1.length !== arr2.length) return false;
  for (let i = 0; i < arr1.length; i++) {
    if (arr1[i] !== arr2[i]) return false;
  }
  return true;
}

function similarPairs(words: string[]): number {
  let count = 0;
  let word_chars: boolean[][] = [];
  for (let i = 0; i < words.length; i++) {
    word_chars.push(new Array(26).fill(false));
    let word = words[i];
    for (let char of word) {
      word_chars[i][char.charCodeAt(0) - "a".charCodeAt(0)] = true;
    }
  }

  for (let i = 0; i < word_chars.length; i++) {
    for (let j = i + 1; j < word_chars.length; j++) {
      if (arraysEqual(word_chars[i], word_chars[j])) {
        count++;
      }
    }
  }

  return count;
}

function similarPairs2(words: string[]): number {
  let count = 0;
  const word_masks = new Map<number, number>();
  for (let word of words) {
    let mask = 0;
    for (let char of word) {
      mask |= 1 << (char.charCodeAt(0) - "a".charCodeAt(0));
    }
    word_masks.set(mask, (word_masks.get(mask) || 0) + 1);
  }
  word_masks.forEach((v, k) => {
    count += (v * (v - 1)) / 2;
  });
  return count;
}

console.log(similarPairs2(["aba", "aabb", "abcd", "bac", "aabc"]));
