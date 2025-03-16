function arrangeCoinsIsGood(mid: number, n: number): boolean {
  let sum = (mid * (mid + 1)) / 2;
  return sum <= n;
}

function arrangeCoins(n: number): number {
  let low = 0;
  let high = n + 1;
  while (high - low > 1) {
    let mid = low + Math.floor((high - low) / 2);
    if (arrangeCoinsIsGood(mid, n)) {
      low = mid;
    } else {
      high = mid;
    }
  }
  return low;
}
