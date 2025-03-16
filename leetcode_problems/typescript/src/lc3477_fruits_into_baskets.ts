function numOfUnplacedFruits(fruits: number[], baskets: number[]): number {
  let n = fruits.length;
  let res = 0;
  let placed: Array<boolean> = new Array(n).fill(false);
  for (let i = 0; i < n; i++) {
    let done = false;
    let fruit = fruits[i];
    for (let j = 0; j < n; j++) {
      if (placed[j]) {
        continue;
      }
      let backet = baskets[j];
      if (fruit <= backet) {
        placed[j] = true;
        done = true;
        break;
      }
    }
    if (!done) {
      res++;
    }
  }
  return res;
}
