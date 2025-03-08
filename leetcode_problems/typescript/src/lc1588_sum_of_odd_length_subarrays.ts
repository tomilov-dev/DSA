function sumOddLengthSubarrays(arr: number[]): number {
  let n = arr.length;
  let sum = 0;
  for (let i = 0; i < n; i++) {
    for (let len = 1; i + len <= n; len += 2) {
      for (let j = i; j < i + len; j++) {
        sum += arr[j];
      }
    }
  }
  return sum;
}

function sumOddLengthSubarraysPrefixSum(arr: number[]): number {
  let n = arr.length;
  let sum = 0;
  let prefix: number[] = new Array(n + 1).fill(0);
  for (let i = 1; i <= n; i++) {
    prefix[i] = prefix[i - 1] + arr[i - 1];
  }
  for (let i = 0; i < n; i++) {
    for (let len = 1; i + len <= n; len += 2) {
      sum += prefix[i + len] - prefix[i];
    }
  }
  return sum;
}

function sumOddLengthSubarraysSolutionN(arr: number[]): number {
  let n = arr.length;
  let sum = 0;
  for (let i = 0; i < n; i++) {
    let total = (n - i) * (i + 1);
    let odd = Math.floor((total + 1) / 2);
    sum += odd * arr[i];
  }
  return sum;
}

console.log(sumOddLengthSubarraysSolutionN([1, 4, 2, 5, 3]));
