package main

func lastStoneWeightII(stones []int) int {
	sum := 0
	for _, num := range stones {
		sum += num
	}
	target := sum / 2
	dp := make([]bool, target+1)
	dp[0] = true
	for _, st := range stones {
		for i := target; i >= st; i-- {
			dp[i] = dp[i] || dp[i-st]
		}
	}
	best := 0
	for i := target; i >= 0; i-- {
		if dp[i] {
			best = i
			break
		}
	}
	return abs(sum - (2 * best))
}
