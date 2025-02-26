function average(salary: number[]): number {
  let maxi = Number.MIN_SAFE_INTEGER;
  let mini = Number.MAX_SAFE_INTEGER;
  let sum = 0;
  for (let num of salary) {
    if (num > maxi) {
      maxi = num;
    }
    if (num < mini) {
      mini = num;
    }
    sum += num;
  }
  return (sum - mini - maxi) / (salary.length - 2);
}

let salary = [4000, 3000, 1000, 2000];
console.log(average(salary));
