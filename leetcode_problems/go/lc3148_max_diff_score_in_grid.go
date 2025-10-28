package main

import "math"

func maxScoreRecursiveHelper(grid [][]int, i, j int) int {
	m := len(grid)
	n := len(grid[0])
	maxi := math.MinInt
	for ii := i; ii < m; ii++ {
		for jj := j; jj < n; jj++ {
			if i == ii && j == jj {
				continue
			}
			jump := grid[ii][jj] - grid[i][j] + maxScoreRecursiveHelper(grid, ii, jj)
			maxi = max(maxi, jump)
		}
	}
	if maxi == math.MinInt {
		return 0
	}
	return maxi
}

func maxScoreRecursive(grid [][]int) int {
	res := math.MinInt
	for i := range grid {
		for j := range grid[0] {
			res = max(res, maxScoreRecursiveHelper(grid, i, j))
		}
	}
	return res
}
