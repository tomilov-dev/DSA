function arrayStringsAreEqual(word1: string[], word2: string[]): boolean {
  let ap1 = 0;
  let wp1 = 0;
  let ap2 = 0;
  let wp2 = 0;
  while (ap1 < word1.length && ap2 < word2.length) {
    let char1 = word1[ap1][wp1];
    let char2 = word2[ap2][wp2];
    if (char1 != char2) {
      return false;
    }

    wp1++;
    wp2++;

    if (wp1 >= word1[ap1].length) {
      wp1 = 0;
      ap1++;
    }
    if (wp2 >= word2[ap2].length) {
      wp2 = 0;
      ap2++;
    }
  }
  return ap1 == word1.length && ap2 == word2.length;
}

console.log(arrayStringsAreEqual(["ab", "c"], ["a", "bc"]));
