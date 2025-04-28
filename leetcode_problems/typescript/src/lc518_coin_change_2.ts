function change(amount: number, coins: number[]): number {
  let n = amount + 1;
  let dp = new Array(n).fill(0);
  dp[0] = 1;
  for (let coin of coins) {
    for (let i = coin; i < n; i++) {
      dp[i] += dp[i - coin];
    }
  }
  return dp[amount];
}
