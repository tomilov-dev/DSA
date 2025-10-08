package main

func sumOfGoodNumbers(nums []int, k int) int {
	sum := 0
	n := len(nums)
	for i := 0; i < n; i++ {
		bad := false
		if i-k >= 0 {
			bad = bad || nums[i] <= nums[i-k]
		}
		if i+k < n {
			bad = bad || nums[i] <= nums[i+k]
		}
		if !bad {
			sum += nums[i]
		}
	}
	return sum
}
