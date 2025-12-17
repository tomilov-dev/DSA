package main

import "sort"

func maxPossibleScoreCan(start []int, d, m int) bool {
	prev := start[0]
	for i := 1; i < len(start); i++ {
		next := max(prev+m, start[i])
		if next > start[i]+d {
			return false
		}
		prev = next
	}
	return true
}

func maxPossibleScore(start []int, d int) int {
	sort.Ints(start)
	l := 0
	h := start[len(start)-1] + start[0] + d + 1
	for h-l > 1 {
		m := l + (h-l)/2
		if maxPossibleScoreCan(start, d, m) {
			l = m
		} else {
			h = m
		}
	}
	return l
}
