package main

func minIncrementsBottomUp(n int, cost []int) int {
	res := 0
	for i := n/2 - 1; i >= 0; i-- {
		l := i*2 + 1
		r := i*2 + 2
		res += abs(cost[l] - cost[r])
		cost[i] += max(cost[l], cost[r])
	}
	return res
}
