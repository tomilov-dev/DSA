package main

import "math"

func integerReplacementRecursiveHelper(n int) int {
	if n == 1 {
		return 0
	}
	if n%2 == 0 {
		return 1 + integerReplacementRecursiveHelper(n/2)
	} else {
		return 1 + min(
			integerReplacementRecursiveHelper(n-1),
			integerReplacementRecursiveHelper(n+1),
		)
	}
}

func integerReplacementRecursive(n int) int {
	return integerReplacementRecursiveHelper(n)
}

func integerReplacementTopDownHelper(n int, mem map[int]int) int {
	if n == 1 {
		return 0
	}
	if n%2 == 0 {
		return 1 + integerReplacementTopDownHelper(n/2, mem)
	} else {
		return 1 + min(
			integerReplacementTopDownHelper(n-1, mem),
			integerReplacementTopDownHelper(n+1, mem),
		)
	}
}

func integerReplacementTopDown(n int) int {
	mem := make(map[int]int, 0)
	return integerReplacementTopDownHelper(n, mem)
}

func integerReplacementBottomUp(n int) int {
	dp := make([]int, n+1)
	for i := range dp {
		dp[i] = math.MaxInt
	}
	dp[0] = 0
	dp[1] = 0
	for i := 2; i < n+1; i++ {
		if i%2 == 0 {
			dp[i] = min(dp[i], 1+dp[i/2])
		} else {
			dp[i] = min(
				dp[i],
				1+dp[i-1],
				2+dp[(i+1)/2],
			)
		}
	}
	return dp[n]
}
