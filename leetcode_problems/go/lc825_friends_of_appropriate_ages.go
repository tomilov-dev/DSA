package main

import "sort"

func numFriendRequests(ages []int) int {
	sort.Ints(ages)
	n := len(ages)
	p2 := n - 1
	requests := 0
	for p2 > 0 {
		c1 := ages[p2]/2 + 7
		p1 := p2 - 1
		for p1 >= 0 && c1 < ages[p1] {
			requests++
			if ages[p1] == ages[p2] {
				requests++
			}
			p1--
		}
		p2--
	}
	return requests
}

func numFriendRequestsOptimized(ages []int) int {
	sort.Ints(ages)
	n := len(ages)
	requests := 0
	left, right := 0, 0

	for i := range n {
		if ages[i] < 15 {
			continue
		}
		for left < i && ages[left] <= ages[i]/2+7 {
			left++
		}
		for right+1 < n && ages[right+1] <= ages[i] {
			right++
		}
		requests += right - left
	}
	return requests
}
