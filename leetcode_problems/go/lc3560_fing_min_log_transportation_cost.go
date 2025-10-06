package main

import "math"

func minCuttingCost(n int, m int, k int) int64 {
	if n <= k && m <= k {
		return 0
	}
	if n > k && m > k {
		return -1
	}
	l := max(n, m)
	mini := math.MaxInt64
	for i := 1; i < l; i++ {
		j := l - i
		if i <= k && j <= k {
			mini = min(mini, i*j)
		}
	}
	if mini == math.MaxInt64 {
		return -1
	}
	return int64(mini)
}
