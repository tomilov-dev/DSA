package main

import "math"

func maxSum3473(nums []int, k int, m int) int {
	n := len(nums)
	pref := make([]int, n+1)
	for i, num := range nums {
		pref[i+1] = pref[i] + num
	}
	dp := make([][]int, n+1)
	for i := range dp {
		dp[i] = make([]int, k+1)
		for j := range dp[i] {
			dp[i][j] = math.MinInt32
		}
	}
	dp[0][0] = 0
	for i := 1; i <= n; i++ {
		for j := 0; j <= k; j++ {
			// не берем новый отрезок
			dp[i][j] = max(dp[i][j], dp[i-1][j])
			// пробуем закончить новый отрезок на позиции i
			if j > 0 && i >= m {
				for l := m; l <= i; l++ {
					dp[i][j] = max(
						dp[i][j],
						dp[i-l][j-1]+pref[i]-pref[i-l],
					)
				}
			}
		}
	}
	return dp[n][k]
}
