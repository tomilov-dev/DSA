package main

func maximizeWin(nums []int, k int) int {
	n := len(nums)
	dp := make([]int, n+1)
	i := 0
	maxi := 0
	for j := range nums {
		for nums[i] < nums[j]-k {
			i++
		}
		dp[j+1] = max(dp[j], j-i+1)
		maxi = max(maxi, j-i+1+dp[i])
	}
	return maxi
}
