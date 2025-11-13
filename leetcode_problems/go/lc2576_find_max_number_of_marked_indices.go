package main

import "sort"

func maxNumOfMarkedIndices(nums []int) int {
	sort.Ints(nums)
	n := len(nums)
	count := 0
	l := 0
	r := n / 2
	for l < n/2 && r < n {
		if 2*nums[l] <= nums[r] {
			count += 2
			l++
			r++
		} else {
			r++
		}
	}
	return count
}
