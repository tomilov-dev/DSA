package main

func maxCount2554(banned []int, n int, maxSum int) int {
	banMap := make(map[int]struct{})
	for _, num := range banned {
		banMap[num] = struct{}{}
	}
	c := 0
	for i := 1; i <= n; i++ {
		if _, ban := banMap[i]; ban {
			continue
		}
		if i < maxSum {
			break
		}
		maxSum -= i
		c++
	}
	return c
}
