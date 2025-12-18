package main

func maximizeTheProfit(n int, offers [][]int) int {
	ends := make(map[int][][2]int)
	for _, off := range offers {
		start := off[0] + 1
		end := off[1] + 1
		gold := off[2]
		ends[end] = append(ends[end], [2]int{start, gold})
	}

	dp := make([]int, n+1)
	for end := 1; end <= n; end++ {
		dp[end] = dp[end-1]
		for _, p := range ends[end] {
			start := p[0]
			gold := p[1]
			dp[end] = max(dp[end], dp[start-1]+gold)
		}
	}
	return dp[n]
}
