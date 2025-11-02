package main

import "slices"

func minOperations3191(nums []int) int {
	n := len(nums)
	res := 0
	for i := 0; i < n-2; i++ {
		if nums[i] == 0 {
			res++
			for j := i; j <= i+2; j++ {
				if nums[j] == 0 {
					nums[j] = 1
				} else {
					nums[j] = 0
				}
			}
		}
	}
	if slices.Contains(nums, 0) {
		return -1
	}
	return res
}
