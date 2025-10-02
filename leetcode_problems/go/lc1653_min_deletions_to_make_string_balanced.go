package main

func minimumDeletions(s string) int {
	n := len(s)
	dp := make([]int, n+1)
	b := 0
	for i := 1; i <= n; i++ {
		if s[i] == 'a' {
			dp[i] = min(dp[i-1]+1, b)
		} else {
			dp[i] = dp[i-1]
			b++
		}
	}
	return dp[n]
}
