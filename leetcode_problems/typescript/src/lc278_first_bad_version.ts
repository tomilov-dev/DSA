var solution = function (isBadVersion: any) {
  return function (n: number): number {
    let low = 0;
    let high = n;
    while (high - low > 1) {
      let mid = low + Math.floor((high - low) / 2);
      if (isBadVersion(mid)) {
        high = mid;
      } else {
        low = mid;
      }
    }
    return high;
  };
};
