package dp_patterns

func MinCostClimbingStairsRecursiveHelper(cost []int, i int) int {
	if i >= len(cost) {
		return 0
	}
	return cost[i] + Min(
		MinCostClimbingStairsRecursiveHelper(cost, i+1),
		MinCostClimbingStairsRecursiveHelper(cost, i+2),
	)
}

func MinCostClimbingStairsRecursive(cost []int) int {
	return Min(MinCostClimbingStairsRecursiveHelper(cost, 0), MinCostClimbingStairsRecursiveHelper(cost, 1))
}

func MinCostClimbingStairsTopDownHelper(cost []int, i int, mem map[int]int) int {
	if i >= len(cost) {
		return 0
	}
	key := i
	if _, exists := mem[key]; !exists {
		mem[key] = cost[i] + Min(
			MinCostClimbingStairsTopDownHelper(cost, i+1, mem),
			MinCostClimbingStairsTopDownHelper(cost, i+2, mem),
		)

	}
	return mem[key]
}

func MinCostClimbingStairsTopDown(cost []int) int {
	mem := make(map[int]int)
	return Min(MinCostClimbingStairsTopDownHelper(cost, 0, mem), MinCostClimbingStairsTopDownHelper(cost, 1, mem))
}

func MinCostClimbingStairsBottomUp(cost []int) int {
	n := len(cost)
	dp := make([]int, n)
	dp[0] = cost[0]
	dp[1] = cost[1]
	for i := 2; i < n; i++ {
		dp[i] = cost[i] + Min(dp[i-1], dp[i-2])
	}
	return Min(dp[n-1], dp[n-2])
}

func MinCostClimbingStairsBottomUpOptimized(cost []int) int {
	n := len(cost)
	dp := cost[0]
	ndp := cost[1]
	for i := 2; i < n; i++ {
		cur := cost[i] + Min(dp, ndp)
		dp = ndp
		ndp = cur
	}
	return Min(dp, ndp)
}
