package main

import "math"

func maximumProduct(nums []int, m int) int64 {
	maxi := nums[0]
	mini := nums[0]
	score := math.MinInt
	for i := m - 1; i < len(nums); i++ {
		maxi = max(maxi, nums[i-m+1])
		mini = min(mini, nums[i-m+1])
		score = max(score, nums[i]*maxi)
		score = max(score, nums[i]*mini)
	}
	return int64(score)
}
