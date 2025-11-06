package main

func twoEggDropRecursiveHelper(n int) int {
	if n <= 0 {
		return 0
	}
	mini := n // максимум n бросков
	for i := 1; i < n; i++ {
		cur := 1 + max(i-1, twoEggDropRecursiveHelper(n-i))
		mini = min(mini, cur)
	}
	return mini
}

func twoEggDropRecursive(n int) int {
	return twoEggDropRecursiveHelper(n)
}

func twoEggDropTopDownHelper(n int, mem map[int]int) int {
	if n <= 0 {
		return 0
	}
	key := n
	if _, solved := mem[key]; !solved {
		mini := n // максимум n бросков
		for i := 1; i < n; i++ {
			cur := 1 + max(i-1, twoEggDropTopDownHelper(n-i, mem))
			mini = min(mini, cur)
		}
		mem[key] = mini
	}
	return mem[key]
}

func twoEggDropTopDown(n int) int {
	mem := make(map[int]int)
	return twoEggDropTopDownHelper(n, mem)
}

func twoEggDropBottomUp(n int) int {
	dp := make([]int, n+1)
	for i := range dp {
		dp[i] = n
	}
	dp[0] = 0

	for i := 1; i < n+1; i++ {
		for j := 1; j <= i; j++ {
			dp[i] = min(dp[i], 1+max(j-1, dp[i-j]))
		}
	}
	return dp[n]
}

func twoEggDropMath(n int) int {
	k := 0
	sum := 0
	for sum < n {
		k++
		sum += k
	}
	return k
}
