function divisorSubstrings(num: number, k: number): number {
  let numStr = num.toString();
  let n = numStr.length;
  let count = 0;
  for (let i = 0; i <= n - k; i++) {
    let subStr = numStr.slice(i, i + k);
    let subNum = Number(subStr);
    if (subNum !== 0 && num % subNum === 0) {
      count++;
    }
  }
  return count;
}
