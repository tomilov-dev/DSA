package main

func minimumNumbers(num int, k int) int {
	nums := make([]int, 0)
	for i := 0; i <= num; i++ {
		if i%10 == k {
			nums = append(nums, i)
		}
	}
	dp := make([]int, num+1)
	for i := range dp {
		dp[i] = 4000
	}
	dp[0] = 0
	for _, n := range nums {
		for i := n; i < num+1; i++ {
			dp[i] = min(dp[i], 1+dp[i-n])
		}
	}
	if dp[num] == 4000 {
		return -1
	}
	return dp[num]
}

func minimumNumbersGreedy(num int, k int) int {
	if num == 0 {
		return 0
	}
	for cnt := 1; cnt <= num; cnt++ {
		if num >= k*cnt && (num-k*cnt)%10 == 0 {
			return cnt
		}
	}
	return -1
}
