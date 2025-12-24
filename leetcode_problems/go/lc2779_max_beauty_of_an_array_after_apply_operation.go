package main

import "sort"

func maximumBeauty(nums []int, k int) int {
	n := len(nums)
	sort.Ints(nums)
	i := 0
	j := 0
	maxi := 0
	for ; i < n && j < n; j++ {
		if nums[j]-nums[i] > 2*k {
			maxi = max(maxi, j-i)
			i++
		}
	}
	maxi = max(maxi, j-i)
	return maxi
}
