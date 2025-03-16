function _mySqrtIsGood(value: number, target: number): boolean {
  return value * value <= target;
}

function mySqrt(x: number): number {
  let low = 0;
  let high = x + 1;
  while (high - low > 1) {
    let mid = low + Math.floor((high - low) / 2);
    if (_mySqrtIsGood(mid, x)) {
      low = mid;
    } else {
      high = mid;
    }
  }
  return low;
}
