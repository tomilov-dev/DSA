function isPerfectSquareIsGood(value: number, target: number) {
  return value * value <= target;
}

function isPerfectSquare(num: number): boolean {
  let low = 0;
  let high = num + 1;
  while (high - low > 1) {
    let mid = low + Math.floor((high - low) / 2);
    if (isPerfectSquareIsGood(mid, num)) {
      low = mid;
    } else {
      high = mid;
    }
  }
  return low * low == num;
}
