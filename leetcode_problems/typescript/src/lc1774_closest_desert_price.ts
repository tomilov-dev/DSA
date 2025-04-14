function closestCost(
  baseCosts: number[],
  toppingCosts: number[],
  target: number
): number {
  function get_min(total: number) {
    let sp1 = target - total;
    let sp2 = target - min;
    if (Math.abs(sp1) > Math.abs(sp2)) {
      return min;
    } else if (Math.abs(sp1) < Math.abs(sp2)) {
      return total;
    } else {
      return sp1 > sp2 ? total : min;
    }
  }

  function backtrack(i: number) {
    if (total >= target) {
      min = get_min(total);
      return;
    }
    if (i >= toppingCosts.length) {
      min = get_min(total);
      return;
    }

    backtrack(i + 1);
    total += toppingCosts[i];
    backtrack(i + 1);
    total += toppingCosts[i];
    backtrack(i + 1);
    total -= 2 * toppingCosts[i];
  }

  let min = 10 ** 6;
  let total = 0;
  for (let bc of baseCosts) {
    total += bc;
    backtrack(0);
    total -= bc;
  }
  return min;
}
