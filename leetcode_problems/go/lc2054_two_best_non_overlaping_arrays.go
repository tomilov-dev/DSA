package main

import "sort"

func maxTwoEventsBS(ends [][2]int, start int) int {
	l := -1
	h := len(ends)
	for h-l > 1 {
		m := l + (h-l)/2
		if ends[m][0] < start {
			l = m
		} else {
			h = m
		}
	}
	return l
}

func maxTwoEvents(events [][]int) int {
	sort.Slice(events, func(i, j int) bool {
		if events[i][0] == events[j][0] {
			return events[i][1] < events[j][1]
		}
		return events[i][0] < events[j][0]
	})

	ends := make([][2]int, len(events))
	for i, e := range events {
		ends[i] = [2]int{e[1], e[2]}
	}
	sort.Slice(ends, func(i, j int) bool {
		return ends[i][0] < ends[j][0]
	})
	pref := make([]int, len(ends))
	pref[0] = ends[0][1]
	for i := 1; i < len(ends); i++ {
		pref[i] = max(pref[i-1], ends[i][1])
	}

	maxi := 0
	for _, e := range events {
		maxi = max(maxi, e[2])
		index := maxTwoEventsBS(ends, e[0])
		if index >= 0 {
			maxi = max(maxi, e[2]+pref[index])
		}
	}
	return maxi
}
