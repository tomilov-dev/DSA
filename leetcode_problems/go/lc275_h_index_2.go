package main

import "sort"

func hIndexCheck(citations []int, x int) bool {
	n := len(citations)
	i := sort.SearchInts(citations, x)
	return n-i >= x
}

func hIndex(citations []int) int {
	n := len(citations)
	l := 0
	h := citations[n-1] + 1
	for h-l > 1 {
		m := l + (h-l)/2
		if hIndexCheck(citations, m) {
			l = m
			println(m, "true")
		} else {
			h = m
			println(m, "false")
		}
	}
	return l
}
