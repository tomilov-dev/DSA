package main

import "sort"

func minRemoval(nums []int, k int) int {
	sort.Ints(nums)
	i := 0
	for _, num := range nums {
		if num > nums[i]*k {
			i++
		}
	}
	return i
}
