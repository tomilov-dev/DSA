function guess(num: number) {
  return 0;
}

function guessNumber(n: number): number {
  let low = 0;
  let high = n;
  while (high - low > 1) {
    let mid = Math.floor(low + (high - low) / 2);
    let guessed = guess(mid);
    if (guessed == 0) {
      return mid;
    } else if (guessed == 1) {
      low = mid;
    } // means -1 => higher
    else {
      high = mid;
    }
  }
  return high;
}
