package main

import "sort"

func beautifulSubsetsBT(nums []int, k int, i int, fq map[int]int) int {
	if i >= len(nums) {
		if len(fq) > 0 {
			return 1
		}
		return 0
	}
	sum := beautifulSubsetsBT(nums, k, i+1, fq)
	if fq[nums[i]-k] == 0 {
		fq[nums[i]]++
		sum += beautifulSubsetsBT(nums, k, i+1, fq)
		fq[nums[i]]--
	}
	return sum
}

func beautifulSubsets(nums []int, k int) int {
	sort.Ints(nums)
	fq := make(map[int]int, 0)
	return beautifulSubsetsBT(nums, k, 0, fq)
}
