function coinChange(coins: number[], amount: number): number {
  let n = amount + 1;
  let dp = new Array(n).fill(10 ** 5);
  dp[0] = 0;
  for (let coin of coins) {
    for (let i = coin; i < n; i++) {
      dp[i] = Math.min(dp[i], dp[i - coin] + 1);
    }
  }
  return dp[amount] === 10 ** 5 ? -1 : dp[amount];
}
