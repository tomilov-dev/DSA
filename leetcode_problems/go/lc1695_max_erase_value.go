package main

func maximumUniqueSubarray(nums []int) int {
	maxSum := 0
	curSum := 0
	fq := make(map[int]int)
	i := 0
	for j := range nums {
		fq[nums[j]]++
		curSum += nums[j]
		for fq[nums[j]] > 1 {
			fq[nums[i]]--
			curSum -= nums[i]
			i++
		}
		maxSum = max(maxSum, curSum)
	}
	return maxSum
}
