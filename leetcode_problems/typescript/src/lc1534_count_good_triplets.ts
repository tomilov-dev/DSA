function countGoodTriplets(
  arr: number[],
  a: number,
  b: number,
  c: number
): number {
  let n = arr.length;
  let count = 0;
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      for (let k = j + 1; k < n; k++) {
        if (
          Math.abs(arr[i] - arr[j]) <= a &&
          Math.abs(arr[j] - arr[k]) <= b &&
          Math.abs(arr[i] - arr[k]) <= c
        ) {
          count++;
        }
      }
    }
  }
  return count;
}

let arr = [3, 0, 1, 1, 9, 7];
let a = 7;
let b = 2;
let c = 3;
let result = countGoodTriplets(arr, a, b, c);
console.log(result);
