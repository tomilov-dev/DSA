package main

func peopleAwareOfSecret(n int, delay int, forget int) int {
	dp := make([]int, n+1)
	for i := range dp {
		dp[i] = 1
	}
	dp[0] = 0
	for i := 1; i < n+1; i++ {
		for j := delay; j < forget; j++ {
			if i-j < 0 {
				continue
			}
			dp[i] += dp[i-j]
		}
	}
	return (dp[n] - dp[n-forget]) % MOD
}
