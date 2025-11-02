package main

func minOperations3192(nums []int) int {
	n := len(nums)
	dp := make([]int, n)
	if nums[n-1] == 0 {
		dp[n-1] = 1
	} else {
		dp[n-1] = 0
	}
	for i := n - 2; i >= 0; i-- {
		if nums[i] == 0 {
			if nums[i] == nums[i+1] {
				dp[i] = dp[i+1]
			} else {
				dp[i] = 2 + dp[i+1]
			}
		} else {
			dp[i] = dp[i+1]
		}
	}
	return dp[0]
}
