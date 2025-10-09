package main

import "math"

func minIncrementOperationsRecursionHelper(nums []int, k int, i int) int64 {
	if i > len(nums)-3 {
		return 0
	}
	op1 := int64(max(k-nums[i], 0)) + minIncrementOperationsRecursionHelper(nums, k, i+1)
	op2 := int64(max(k-nums[i+1], 0)) + minIncrementOperationsRecursionHelper(nums, k, i+2)
	op3 := int64(max(k-nums[i+2], 0)) + minIncrementOperationsRecursionHelper(nums, k, i+3)
	return min(op1, op2, op3)
}

func minIncrementOperationsRecursion(nums []int, k int) int64 {
	return minIncrementOperationsRecursionHelper(nums, k, 0)
}

func minIncrementOperationsTopDownHelper(nums []int, k int, i int, mem map[int]int64) int64 {
	if i > len(nums)-3 {
		return 0
	}
	key := i
	if _, solved := mem[key]; !solved {
		op1 := int64(max(k-nums[i], 0)) + minIncrementOperationsTopDownHelper(nums, k, i+1, mem)
		op2 := int64(max(k-nums[i+1], 0)) + minIncrementOperationsTopDownHelper(nums, k, i+2, mem)
		op3 := int64(max(k-nums[i+2], 0)) + minIncrementOperationsTopDownHelper(nums, k, i+3, mem)
		mem[key] = min(op1, op2, op3)
	}
	return mem[key]
}

func minIncrementOperationsTopDown(nums []int, k int) int64 {
	mem := make(map[int]int64)
	return minIncrementOperationsTopDownHelper(nums, k, 0, mem)
}

func minIncrementOperationsBottomUp(nums []int, k int) int64 {
	n := len(nums)
	dp := make([]int64, n+1)
	for i := range dp {
		dp[i] = math.MaxInt64
	}
	dp[n] = 0
	dp[n-1] = 0
	dp[n-2] = 0

	for i := n - 3; i >= 0; i-- {
		op1 := int64(max(k-nums[i], 0)) + dp[i+1]
		op2 := int64(max(k-nums[i+1], 0)) + dp[i+2]
		op3 := int64(max(k-nums[i+2], 0)) + dp[i+3]
		dp[i] = min(op1, op2, op3)
	}
	return dp[0]
}
