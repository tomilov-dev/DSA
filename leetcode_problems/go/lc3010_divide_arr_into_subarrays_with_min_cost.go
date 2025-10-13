package main

func minimumCost(nums []int) int {
	n1 := nums[0]
	min1 := nums[1]
	min2 := nums[2]
	if min2 < min1 {
		min1, min2 = min2, min1
	}
	for i := 3; i < len(nums); i++ {
		if nums[i] < min1 {
			min2 = min1
			min1 = nums[i]
		} else if nums[i] < min2 {
			min2 = nums[i]
		}
	}
	return n1 + min1 + min2
}
