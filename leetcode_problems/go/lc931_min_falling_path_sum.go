package main

import (
	"math"
)

func minFallingPathSumRecursionHelper(matrix [][]int, i int, j int) int {
	if i >= len(matrix) {
		return 0
	}
	if j >= len(matrix[0]) || j < 0 {
		return math.MaxInt
	}
	return matrix[i][j] + min(
		minFallingPathSumRecursionHelper(matrix, i+1, j-1),
		minFallingPathSumRecursionHelper(matrix, i+1, j),
		minFallingPathSumRecursionHelper(matrix, i+1, j+1),
	)
}

func minFallingPathSumRecursion(matrix [][]int) int {
	mini := math.MaxInt
	for j := 0; j < len(matrix[0]); j++ {
		mini = min(mini, minFallingPathSumRecursionHelper(matrix, 0, j))
	}
	return mini
}

func minFallingPathSumTopDownHelper(matrix [][]int, i int, j int, mem map[[2]int]int) int {
	if i >= len(matrix) {
		return 0
	}
	if j >= len(matrix[0]) || j < 0 {
		return math.MaxInt
	}
	key := [2]int{i, j}
	if _, solved := mem[key]; !solved {
		mem[key] = matrix[i][j] + min(
			minFallingPathSumTopDownHelper(matrix, i+1, j-1, mem),
			minFallingPathSumTopDownHelper(matrix, i+1, j, mem),
			minFallingPathSumTopDownHelper(matrix, i+1, j+1, mem),
		)
	}
	return mem[key]
}

func minFallingPathSumTopDown(matrix [][]int) int {
	mini := math.MaxInt
	mem := make(map[[2]int]int)
	for j := 0; j < len(matrix[0]); j++ {
		mini = min(mini, minFallingPathSumTopDownHelper(matrix, 0, j, mem))
	}
	return mini
}

func minFallingPathSumBottomUp(matrix [][]int) int {
	m := len(matrix)
	n := len(matrix[0])
	dp := make([][]int, m)
	for i := range dp {
		dp[i] = make([]int, n)
	}
	for j := range dp[0] {
		dp[0][j] = matrix[0][j]
	}
	for i := 1; i < m; i++ {
		for j := range dp[i] {
			left := math.MaxInt
			right := math.MaxInt
			mid := dp[i-1][j]
			if j-1 >= 0 {
				left = dp[i-1][j-1]
			}
			if j+1 < n {
				right = dp[i-1][j+1]
			}
			dp[i][j] = matrix[i][j] + min(
				left,
				mid,
				right,
			)
		}
	}
	mini := math.MaxInt
	for i := range dp[n-1] {
		mini = min(mini, dp[n-1][i])
	}
	return mini
}

func minFallingPathSumBottomUpOptimal(matrix [][]int) int {
	m := len(matrix)
	n := len(matrix[0])

	dp1 := make([]int, n)
	dp2 := make([]int, n)
	for i := range dp1 {
		dp1[i] = matrix[0][i]
	}
	for i := 1; i < m; i++ {
		for j := 0; j < n; j++ {
			left := math.MaxInt
			right := math.MaxInt
			mid := dp1[j]
			if j-1 >= 0 {
				left = dp1[j-1]
			}
			if j+1 < n {
				right = dp1[j+1]
			}
			dp2[j] = matrix[i][j] + min(
				left,
				mid,
				right,
			)
		}
		dp1, dp2 = dp2, dp1
	}
	mini := math.MaxInt
	for i := range dp1 {
		mini = min(mini, dp1[i])
	}
	return mini
}
