function circularPermutation(n: number, start: number): number[] {
  function is_valid(cur: number, prev: number): boolean {
    let xr = cur ^ prev;
    return xr > 0 && (xr & (xr - 1)) == 0;
  }

  function gen_neighbors(num: number, n: number): number[] {
    let nb = [];
    for (let i = 0; i < n; i++) {
      nb.push(num ^ (1 << i));
    }
    return nb;
  }

  function backtrack(
    i: number,
    k: number,
    stack: number[],
    used: boolean[],
    nb: Map<number, number[]>
  ): boolean {
    if (i >= k) {
      return stack[k - 1] !== -1 && is_valid(stack[0], stack[stack.length - 1]);
    }

    let prev = stack[i - 1];
    let cnb = nb.get(prev);
    if (!cnb) {
      return false;
    }

    for (let j of cnb) {
      if (used[j] || !is_valid(j, stack[i - 1])) {
        continue;
      }

      used[j] = true;
      stack[i] = j;
      if (backtrack(i + 1, k, stack, used, nb)) {
        return true;
      }
      stack[i] = -1;
      used[j] = false;
    }
    return false;
  }

  let k = 2 ** n;
  let used = new Array(k).fill(false);
  used[start] = true;

  let stack = new Array(k).fill(-1);
  stack[0] = start;

  let nb = new Map<number, number[]>();
  for (let i = 0; i < k; i++) {
    nb.set(i, gen_neighbors(i, n));
  }

  backtrack(1, k, stack, used, nb);
  return stack;
}
