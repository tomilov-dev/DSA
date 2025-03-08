function mostVisited(n: number, rounds: number[]): number[] {
  let arr: number[] = new Array(n).fill(0);

  for (let i = 1; i < rounds.length; i++) {
    let start = rounds[i - 1];
    let end = rounds[i];
    if (start < end) {
      for (let j = start; j < end; j++) {
        arr[j - 1]++;
      }
    } else {
      for (let j = start; j <= n; j++) {
        arr[j - 1]++;
      }
      for (let j = 0; j < end; j++) {
        arr[j - 1]++;
      }
    }
  }
  arr[rounds[rounds.length - 1] - 1]++;

  let xmax: number = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > xmax) {
      xmax = arr[i];
    }
  }

  let res: number[] = [];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] == xmax) {
      res.push(i + 1);
    }
  }

  return res;
}

function mostVisited2(n: number, rounds: number[]): number[] {
  const start = rounds[0];
  const end = rounds[rounds.length - 1];
  const result: number[] = [];

  if (start <= end) {
    for (let i = start; i <= end; i++) {
      result.push(i);
    }
  } else {
    for (let i = 1; i <= end; i++) {
      result.push(i);
    }
    for (let i = start; i <= n; i++) {
      result.push(i);
    }
  }

  return result;
}

console.log(mostVisited(4, [1, 3, 1, 2]));
