package main

func longestArithSeqLength(nums []int) int {
	dp := make(map[[2]int]int, 0)
	maxi := 0
	for i := range nums {
		for j := i + 1; j < len(nums); j++ {
			diff := nums[j] - nums[i]
			k1 := [2]int{j, diff}
			k2 := [2]int{i, diff}
			dp[k1] = 1 + max(dp[k2], 1)
			maxi = max(maxi, dp[k1])
		}
	}
	return maxi
}
