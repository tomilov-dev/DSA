function constructDistancedSequence(n: number): number[] {
  function large(seqA: number[], seqB: number[]) {
    if (seqA.length > seqB.length) {
      return true;
    } else if (seqA.length < seqB.length) {
      return false;
    } else {
      for (let i = 0; i < seqA.length; i++) {
        if (seqA[i] === seqB[i]) {
          continue;
        }
      }
      return false;
    }
  }
  function backtrack(i: number) {
    if (found) {
      return;
    }

    if (i >= stack.length) {
      if (large(stack, res)) {
        res = stack.slice();
        found = true;
      }
    }

    if (stack[i] !== -1) {
      backtrack(i + 1);
      return;
    }

    for (let num = n; num > 0 && !found; num--) {
      if (!nums[num]) {
        continue;
      }

      let dist = num == 1 ? 0 : num;
      if (i + dist >= stack.length || stack[i + dist] !== -1) {
        continue;
      }

      stack[i] = num;
      stack[i + dist] = num;
      nums[num] = false;

      backtrack(i + 1);

      stack[i] = -1;
      stack[i + dist] = -1;
      nums[num] = true;
    }
  }

  let found = false;
  let nums = new Array(n + 1).fill(true);
  let stack = new Array(1 + (n - 1) * 2).fill(-1);
  let res: number[] = [];
  backtrack(0);
  return res;
}
