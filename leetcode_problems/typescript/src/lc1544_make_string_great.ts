function makeGood(s: string): string {
  let res: string[] = [];
  for (let char of s) {
    if (res.length === 0) {
      res.push(char);
      continue;
    }

    let prev = res[res.length - 1];
    if (prev !== char && prev.toLowerCase() === char.toLowerCase()) {
      res.pop();
    } else {
      res.push(char);
    }
  }
  return res.join("");
}
