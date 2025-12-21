package main

func minArraySum(nums []int, k int) int64 {
	const MAX = 1 << 32
	dp := make([]int, k+1)
	for i := 1; i <= k; i++ {
		dp[i] = MAX
	}
	res := 0
	for _, num := range nums {
		res += num
		dp[res%k] = min(dp[res%k], res)
		res = dp[res%k]
	}
	return int64(res)
}
