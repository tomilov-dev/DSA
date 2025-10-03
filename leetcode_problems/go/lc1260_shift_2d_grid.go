package main

func shiftGrid(grid [][]int, k int) [][]int {
	m := len(grid)
	n := len(grid[0])
	total := m * n
	k = k % total

	flat := make([]int, total)
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			flat[i*n+j] = grid[i][j]
		}
	}

	res := make([][]int, m)
	for i := range res {
		res[i] = make([]int, n)
	}
	for idx := 0; idx < total; idx++ {
		newIdx := (idx + k) % total
		res[newIdx/n][newIdx%n] = flat[idx]
	}
	return res
}
