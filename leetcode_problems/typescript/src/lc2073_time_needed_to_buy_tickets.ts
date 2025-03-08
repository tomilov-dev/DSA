function timeRequiredToBuy(tickets: number[], k: number): number {
  let res: number = 0;
  let target: number = tickets[k];
  for (let i = 0; i < tickets.length; i++) {
    if (i <= k) {
      res += Math.min(target, tickets[i]);
    } else {
      res += Math.min(target - 1, tickets[i]);
    }
  }
  return res;
}

console.log(timeRequiredToBuy([5, 1, 1, 1], 0));
