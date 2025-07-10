package dp_patterns

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func HouseRobberRecursive(arr []int, i int) int {
	if i >= len(arr) {
		return 0
	}
	return max(arr[i]+HouseRobberRecursive(arr, i+2), HouseRobberRecursive(arr, i+1))
}

func HouseRobberTopDownHelper(arr []int, i int, mem map[int]int) int {
	if i >= len(arr) {
		return 0
	}
	key := i
	if _, exists := mem[key]; !exists {
		mem[key] = max(arr[i]+HouseRobberRecursive(arr, i+2), HouseRobberRecursive(arr, i+1))
	}
	return mem[key]
}

func HouseRobberTopDown(arr []int, i int) int {
	mem := make(map[int]int)
	return HouseRobberTopDownHelper(arr, i, mem)
}

func HouseRobberBottomUp(arr []int, i int) int {
	n := len(arr)
	if n == 0 {
		return 0
	}
	if n == 1 {
		return arr[0]
	}
	dp := make([]int, n+1)
	dp[0] = 0
	dp[1] = arr[0]
	for j := 2; j <= n; j++ {
		dp[j] = max(arr[j-1]+dp[j-2], dp[j-1])
	}
	return dp[n]
}

func HouseRobberBottomUpOptimized(arr []int, i int) int {
	n := len(arr)
	if n == 0 {
		return 0
	}
	if n == 1 {
		return arr[0]
	}
	dp := 0
	ndp := arr[0]
	for j := 2; j <= n; j++ {
		cur := max(arr[j-1]+dp, ndp)
		dp = ndp
		ndp = cur
	}
	return ndp
}
