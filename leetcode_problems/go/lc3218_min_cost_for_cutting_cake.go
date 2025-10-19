package main

import (
	"math"
	"sort"
)

func minimumCostForCuttingCake(
	m int,
	n int,
	horizontalCut []int,
	verticalCut []int,
) int {
	sort.Slice(horizontalCut, func(i, j int) bool { return horizontalCut[i] > horizontalCut[j] })
	sort.Slice(verticalCut, func(i, j int) bool { return verticalCut[i] > verticalCut[j] })

	dp := make([][]int, m)
	for i := range dp {
		dp[i] = make([]int, n)
		for j := range dp[i] {
			dp[i][j] = math.MaxInt
		}
	}
	dp[0][0] = 0
	for i := range m {
		for j := range n {
			if i > 0 {
				dp[i][j] = min(
					dp[i][j],
					dp[i-1][j]+horizontalCut[i-1]*(j+1),
				)
			}
			if j > 0 {
				dp[i][j] = min(
					dp[i][j],
					dp[i][j-1]+verticalCut[j-1]*(i+1),
				)
			}
		}
	}
	return dp[m-1][n-1]
}
