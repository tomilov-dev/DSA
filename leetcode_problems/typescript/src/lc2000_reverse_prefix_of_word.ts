function reversePrefix(word: string, ch: string): string {
  let i = 0;
  let res: string = "";
  for (let char of word) {
    if (char == ch) {
      break;
    }
    i++;
  }
  if (i >= word.length) {
    return word;
  }

  for (let j = i; j >= 0; j--) {
    res += word[j];
  }
  for (let j = i + 1; j < word.length; j++) {
    res += word[j];
  }
  return res;
}
function reversePrefix2(word: string, ch: string): string {
  let index = word.indexOf(ch);
  if (index === -1) {
    return word;
  }
  let prefix = word
    .slice(0, index + 1)
    .split("")
    .reverse()
    .join("");
  let suffix = word.slice(index + 1);
  return prefix + suffix;
}
