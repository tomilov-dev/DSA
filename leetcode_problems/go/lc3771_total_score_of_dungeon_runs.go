package main

import "sort"

func totalScore(hp int, damage []int, requirement []int) int64 {
	n := len(damage)
	prefix := make([]int, n+1)
	for i := 1; i <= n; i++ {
		prefix[i] = prefix[i-1] + damage[i-1]
	}

	total := 0
	for end := 1; end <= n; end++ {
		target := prefix[end] + requirement[end-1] - hp
		start := sort.SearchInts(prefix, target)
		if start <= end-1 {
			total += (end - start)
		}
	}
	return int64(total)
}
