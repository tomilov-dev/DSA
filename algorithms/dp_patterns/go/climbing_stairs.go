package dp_patterns

func ClimbingStairsRecursive(n int) int {
	if n == 0 {
		return 1
	}
	if n == 1 {
		return 1
	}
	return ClimbingStairsRecursive(n-1) + ClimbingStairsRecursive(n-2)
}

func ClimbingStairsTopDownHelper(n int, mem map[int]int) int {
	if n == 0 {
		return 1
	}
	if n == 1 {
		return 1
	}

	key := n
	if _, exists := mem[key]; !exists {
		mem[key] = ClimbingStairsTopDownHelper(n-1, mem) + ClimbingStairsTopDownHelper(n-2, mem)
	}
	return mem[key]
}

func ClimbingStairsTopDown(n int) int {
	mem := make(map[int]int)
	return ClimbingStairsTopDownHelper(n, mem)
}

func ClimbingStairsBottomUp(n int) int {
	if n == 0 {
		return 1
	}
	if n == 1 {
		return 1
	}
	dp := make([]int, n+1)
	dp[0] = 1
	dp[1] = 1
	for i := 2; i <= n; i++ {
		dp[i] = dp[i-1] + dp[i-2]
	}
	return dp[n]
}

func ClimbingStairsBottomUpOptimized(n int) int {
	if n == 0 {
		return 1
	}
	if n == 1 {
		return 1
	}
	dp := 1
	ndp := 1
	for i := 2; i <= n; i++ {
		cur := dp + ndp
		dp = ndp
		ndp = cur
	}
	return ndp
}
