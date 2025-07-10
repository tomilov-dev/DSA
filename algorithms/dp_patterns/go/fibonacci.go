package dp_patterns

func FibonacciRecursive(n int) int {
	if n == 0 {
		return 0
	}
	if n == 1 {
		return 1
	}
	return FibonacciRecursive(n-1) + FibonacciRecursive(n-2)
}

func FibonacciTopDownHelper(n int, mem map[int]int) int {
	if n == 0 {
		return 0
	}
	if n == 1 {
		return 1
	}

	key := n
	if _, exists := mem[key]; !exists {
		mem[key] = FibonacciTopDownHelper(n-1, mem) + FibonacciTopDownHelper(n-2, mem)
	}
	return mem[key]
}

func FibonacciTopDown(n int) int {
	mem := make(map[int]int)
	return FibonacciTopDownHelper(n, mem)
}

func FibonacciBottomUp(n int) int {
	if n == 0 {
		return 0
	}
	if n == 1 {
		return 1
	}
	dp := make([]int, n+1)
	dp[0] = 0
	dp[1] = 1
	for i := 2; i <= n; i++ {
		dp[i] = dp[i-1] + dp[i-2]
	}
	return dp[n]
}

func FibonacciBottomUpOptimized(n int) int {
	if n == 0 {
		return 0
	}
	if n == 1 {
		return 1
	}

	dp := 0
	ndp := 1
	for i := 2; i <= n; i++ {
		cur := dp + ndp
		dp = ndp
		ndp = cur
	}
	return ndp
}
