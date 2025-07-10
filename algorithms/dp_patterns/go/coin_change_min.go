package dp_patterns

import (
	"math"
)

var MAX int = math.MaxInt32

type ccpair struct {
	sum int
	i   int
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func CoinChangeMinRecursiveHelper(sum int, coins []int, i int) int {
	if i >= len(coins) || sum < 0 {
		return MAX
	}
	if sum == 0 {
		return 0
	}
	return min(1+CoinChangeMinRecursiveHelper(sum-coins[i], coins, i), CoinChangeMinRecursiveHelper(sum, coins, i+1))
}

func CoinChangeMinRecursive(sum int, coins []int) int {
	res := CoinChangeMinRecursiveHelper(sum, coins, 0)
	if res == MAX {
		return -1
	}
	return res
}

func CoinChangeMinTopDownHelper(sum int, coins []int, i int, mem map[ccpair]int) int {
	if i >= len(coins) || sum < 0 {
		return MAX
	}
	if sum == 0 {
		return 0
	}
	key := ccpair{sum, i}
	if _, exists := mem[key]; !exists {
		mem[key] = min(
			1+CoinChangeMinTopDownHelper(sum-coins[i], coins, i, mem),
			CoinChangeMinTopDownHelper(sum, coins, i+1, mem),
		)
	}
	return mem[key]
}

func CoinChangeMinTopDown(sum int, coins []int) int {
	mem := make(map[ccpair]int)
	res := CoinChangeMinTopDownHelper(sum, coins, 0, mem)
	if res == MAX {
		return -1
	}
	return res
}

func CoinChangeMinBottomUp(sum int, coins []int) int {
	dp := make([]int, sum+1)
	for i := range dp {
		dp[i] = MAX
	}
	dp[0] = 0

	for _, coin := range coins {
		for s := coin; s <= sum; s++ {
			dp[s] = min(dp[s], 1+dp[s-coin])
		}
	}
	if dp[sum] == MAX {
		return -1
	}
	return dp[sum]
}
