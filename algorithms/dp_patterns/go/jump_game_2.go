package dp_patterns

import "math"

var MAXV = math.MaxInt64

func JumpRecursiveHelper(nums []int, i int) int {
	if i >= len(nums)-1 {
		return 0
	}
	mini := MAXV
	for j := 1; j <= nums[i]; j++ {
		if i+j >= len(nums) {
			continue
		}
		mini = Min(mini, 1+JumpRecursiveHelper(nums, i+j))
	}
	return mini
}

func JumpRecursive(nums []int, i int) int {
	return JumpRecursiveHelper(nums, 0)
}

func JumpTopDownHelper(nums []int, i int, mem map[int]int) int {
	if i >= len(nums)-1 {
		return 0
	}
	key := i
	if _, exists := mem[key]; !exists {
		mini := MAXV
		for j := 1; j <= nums[i]; j++ {
			if i+j >= len(nums) {
				continue
			}
			mini = Min(mini, 1+JumpTopDownHelper(nums, i+j, mem))
		}
		mem[key] = mini
	}
	return mem[key]
}

func JumpTopDown(nums []int, i int) int {
	mem := make(map[int]int)
	return JumpTopDownHelper(nums, 0, mem)
}

func JumpBottomUp(nums []int) int {
	n := len(nums)
	dp := make([]int, n)
	for i := range n {
		dp[i] = MAXV
	}

	dp[0] = 0
	for i := range n {
		for j := 1; j <= nums[i] && i+j < n; j++ {
			dp[i+j] = Min(dp[i+j], 1+dp[i])
		}
	}
	return dp[n-1]
}
