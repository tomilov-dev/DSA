package main

import "math"

func maxScore(a []int, b []int) int64 {
	n := len(a)              // 4
	dp := make([]int64, n+1) // in other words make([]int, 5)
	for i := range dp {
		dp[i] = math.MinInt64
	}
	dp[0] = 0

	for _, num := range b {
		for i := n - 1; i >= 0; i-- {
			if dp[i] != math.MinInt64 { // проверяем что предыдущий не MinInt
				cur := dp[i] + int64(a[i]*num)
				dp[i+1] = max(dp[i+1], cur)
			}
		}
	}
	return dp[n]
}
