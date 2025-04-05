function makesquare(matchsticks: number[]): boolean {
  function backtrack(i: number): boolean {
    if (i >= m.length) {
      for (let size of square) {
        if (size != t) {
          return false;
        }
      }
      return true;
    }
    for (let side = 0; side < 4; side++) {
      if (square[side] + m[i] <= t) {
        square[side] += m[i];
        if (backtrack(i + 1)) {
          return true;
        }
        square[side] -= m[i];
      }
      if (square[side] === 0) {
        break;
      }
    }
    return false;
  }

  let m = matchsticks;
  let msum = 0;
  for (let n of matchsticks) {
    msum += n;
  }

  if (msum <= 0 || msum % 4 !== 0) {
    return false;
  }

  let t = Math.floor(msum / 4);
  for (let n of matchsticks) {
    if (n > t) {
      return false;
    }
  }

  m.sort((a, b) => b - a);
  let square: number[] = [0, 0, 0, 0];
  return backtrack(0);
}
