package main

func edgeScore(edges []int) int {
	mp := make(map[int]int)
	maxi := 0
	maxv := 0
	for v, i := range edges {
		mp[i] += v
		if mp[i] == maxv && i < maxi {
			maxi = i
		} else if mp[i] > maxv {
			maxi = i
			maxv = mp[i]
		}
	}
	return maxi
}

func edgeScoreCount(edges []int) int {
	c := make([]int, len(edges))
	maxi := 0
	maxv := 0
	for v, i := range edges {
		c[i] += v
		if c[i] == maxv && i < maxi {
			maxi = i
		} else if c[i] > maxv {
			maxi = i
			maxv = c[i]
		}
	}
	return maxi
}
