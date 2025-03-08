function canMakeArithmeticProgression(arr: number[]): boolean {
  arr.sort((a, b) => a - b);
  let diff: number = arr[1] - arr[0];
  for (let i = 2; i < arr.length; i++) {
    if (arr[i] - arr[i - 1] != diff) {
      return false;
    }
  }
  return true;
}

console.log(canMakeArithmeticProgression([3, 5, 1]));
