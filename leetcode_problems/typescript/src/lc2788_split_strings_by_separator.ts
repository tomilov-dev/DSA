function splitWordsBySeparator(words: string[], separator: string): string[] {
  let result: string[] = [];
  for (let word of words) {
    for (let subword of word.split(separator)) {
      if (subword !== "") {
        result.push(subword);
      }
    }
  }
  return result;
}

let words = ["one.two.three", "four.five", "six"];
let separator = ".";
let lc2788 = splitWordsBySeparator(words, separator);
console.log(lc2788);
