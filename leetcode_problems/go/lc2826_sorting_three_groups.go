package main

import "math"

func minimumOperationsRecursiveHelper(nums []int, i int, x int) int {
	if i >= len(nums) {
		return 0
	}
	if x > 3 {
		return math.MaxInt
	}
	op := 0
	if nums[i] != x {
		op++
	}
	return op + min(
		minimumOperationsRecursiveHelper(nums, i+1, x),
		minimumOperationsRecursiveHelper(nums, i+1, x+1),
		minimumOperationsRecursiveHelper(nums, i+1, x+2),
	)
}

func minimumOperationsRecursive(nums []int) int {
	return min(
		minimumOperationsRecursiveHelper(nums, 0, 1),
		minimumOperationsRecursiveHelper(nums, 0, 2),
		minimumOperationsRecursiveHelper(nums, 0, 3),
	)
}

func minimumOperationsTopDownHelper(nums []int, i int, x int, mem map[[2]int]int) int {
	if i >= len(nums) {
		return 0
	}
	if x > 3 {
		return math.MaxInt
	}
	key := [2]int{i, x}
	if _, solved := mem[key]; !solved {
		op := 0
		if nums[i] != x {
			op++
		}
		mem[key] = op + min(
			minimumOperationsTopDownHelper(nums, i+1, x, mem),
			minimumOperationsTopDownHelper(nums, i+1, x+1, mem),
			minimumOperationsTopDownHelper(nums, i+1, x+2, mem),
		)
	}
	return mem[key]
}

func minimumOperationsTopDown(nums []int) int {
	mem := make(map[[2]int]int, 0)
	return min(
		minimumOperationsTopDownHelper(nums, 0, 1, mem),
		minimumOperationsTopDownHelper(nums, 0, 2, mem),
		minimumOperationsTopDownHelper(nums, 0, 3, mem),
	)
}

func minimumOperationsBottomUp(nums []int) int {
	n := len(nums)
	const groups = 3
	dp := make([][]int, n+1)
	for i := range dp {
		dp[i] = make([]int, groups)
		for g := range dp[i] {
			dp[i][g] = math.MaxInt32
		}
	}

	for g := range groups {
		dp[0][g] = 0
	}

	for i := 1; i <= n; i++ {
		for g := range groups {
			op := 0
			if nums[i-1] != g+1 {
				op = 1
			}

			// можно перейти только из группы ≤ g
			minPrev := math.MaxInt32
			for prev := 0; prev <= g; prev++ {
				minPrev = min(minPrev, dp[i-1][prev])
			}
			dp[i][g] = minPrev + op
		}
	}

	// ответ — минимум среди dp[n][g]
	res := math.MaxInt
	for g := range groups {
		if dp[n][g] < res {
			res = dp[n][g]
		}
	}
	return res
}
