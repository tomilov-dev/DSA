package main

func check(nums []int) bool {
	n := len(nums)
	count := 0
	for i := range n {
		if nums[i] > nums[(i+1)%n] {
			count++
		}
		if count > 1 {
			return false
		}
	}
	return true
}
