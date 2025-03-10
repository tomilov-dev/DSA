function gcd(a: number, b: number): number {
  while (b !== 0) {
    let temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}

function first_digit(num: number): number {
  while (num >= 10) {
    num = Math.floor(num / 10);
  }
  return num;
}

function last_digit(num: number): number {
  return num % 10;
}

function countBeautifulPairs(nums: number[]): number {
  let res = 0;
  let map: Map<number, number> = new Map();
  for (let num of nums) {
    let last_value = last_digit(num);
    map.forEach((first_count, first_value) => {
      if (gcd(first_value, last_value) == 1) {
        res += first_count;
      }
    });
    let first_value = first_digit(num);
    map.set(first_value, (map.get(first_value) || 0) + 1);
  }
  return res;
}
