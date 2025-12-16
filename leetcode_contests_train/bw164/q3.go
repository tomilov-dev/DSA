package bw164

func uniquePaths(grid [][]int) int {
	const MOD = 1_000_000_007
	m := len(grid)
	n := len(grid[0])
	dp := make([][][]int, m)
	for i := range dp {
		dp[i] = make([][]int, n)
		for j := range dp[i] {
			dp[i][j] = make([]int, 2)
		}
	}
	for j := range n {
		dp[0][j][0] = 1
		if grid[0][j] == 1 {
			break
		}
	}
	for i := range m {
		dp[i][0][1] = 1
		if grid[i][0] == 1 {
			break
		}
	}

	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			if grid[i-1][j] == 1 {
				dp[i][j][1] = dp[i-1][j][0] % MOD
			} else {
				dp[i][j][1] = (dp[i-1][j][0] + dp[i-1][j][1]) % MOD
			}
			if grid[i][j-1] == 1 {
				dp[i][j][0] = dp[i][j-1][1] % MOD
			} else {
				dp[i][j][0] = (dp[i][j-1][0] + dp[i][j-1][1]) % MOD
			}
		}
	}
	return (dp[m-1][n-1][0] + dp[m-1][n-1][1]) % MOD
}
