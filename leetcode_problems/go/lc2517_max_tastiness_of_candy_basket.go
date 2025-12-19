package main

import "sort"

func maximumTastinessCheck(price []int, k, m int) bool {
	last := price[0]
	count := 1
	for i := 1; count < k && i < len(price); i++ {
		if price[i]-last >= m {
			last = price[i]
			count++
		}
	}
	return count == k
}

func maximumTastiness(price []int, k int) int {
	n := len(price)
	sort.Ints(price)
	l := 0
	h := price[n-1] - price[0] + 1
	for h-l > 1 {
		m := l + (h-l)/2
		if maximumTastinessCheck(price, k, m) {
			l = m
		} else {
			h = m
		}
	}
	return l
}
