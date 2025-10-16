package main

func digitLen(n int) int {
	dl := 0
	if n == 0 {
		return 1
	}
	if n < 0 {
		n *= -1
		dl++
	}
	for n > 0 {
		dl++
		n /= 10
	}
	return dl
}

func findColumnWidth(grid [][]int) []int {
	n := len(grid[0])
	res := make([]int, n)
	for i := range grid {
		for j := range grid[i] {
			dl := digitLen(grid[i][j])
			res[j] = max(res[j], dl)
		}
	}
	return res
}
