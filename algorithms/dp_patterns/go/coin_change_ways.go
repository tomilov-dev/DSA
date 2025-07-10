package dp_patterns

type pair struct {
	sum int
	i   int
}

func CoinChangeWaysRecursive(sum int, coins []int, i int) int {
	if sum == 0 {
		return 1
	}
	if i >= len(coins) || sum < 0 {
		return 0
	}
	return CoinChangeWaysRecursive(sum-coins[i], coins, i) + CoinChangeWaysRecursive(sum, coins, i+1)
}

func CoinChangeWaysTopDownHelper(sum int, coins []int, i int, mem map[pair]int) int {
	if sum == 0 {
		return 1
	}
	if i >= len(coins) || sum < 0 {
		return 0
	}
	key := pair{sum, i}
	if _, exists := mem[key]; !exists {
		mem[key] = CoinChangeWaysRecursive(sum-coins[i], coins, i) + CoinChangeWaysRecursive(sum, coins, i+1)
	}
	return mem[key]
}

func CoinChangeWaysTopDown(sum int, coins []int, i int) int {
	mem := make(map[pair]int)
	return CoinChangeWaysTopDownHelper(sum, coins, 0, mem)
}

func CoinChangeWaysBottomUp(sum int, coins []int, i int) int {
	dp := make([]int, sum+1)
	dp[0] = 1
	for _, coin := range coins {
		for s := coin; s < sum+1; s++ {
			dp[s] = dp[s] + dp[s-coin]
		}
	}
	return dp[sum]
}
