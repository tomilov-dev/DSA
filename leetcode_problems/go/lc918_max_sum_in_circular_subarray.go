package main

func maxSubarraySumCircular(nums []int) int {
	total := 0
	maxSum := nums[0]
	curMax := nums[0]
	minSum := nums[0]
	curMin := nums[0]
	for _, x := range nums {
		curMax = max(curMax+x, x)
		maxSum = max(maxSum, curMax)
		curMin = min(curMin+x, curMin)
		minSum = min(minSum, curMin)
		total += x
	}
	if maxSum > 0 {
		return max(maxSum, total-minSum)
	}
	return maxSum
}
