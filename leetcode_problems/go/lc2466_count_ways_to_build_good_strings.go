package main

func countGoodStringsRecursiveHelper(low int, high int, zero int, one int, l int) int {
	if l > high {
		return 0
	}
	ways := 0
	if l >= low {
		ways++
	}
	add_zero := countGoodStringsRecursiveHelper(low, high, zero, one, l+zero)
	add_one := countGoodStringsRecursiveHelper(low, high, zero, one, l+one)
	return ((ways+add_zero)%MOD + add_one) % MOD
}

func countGoodStringsRecursive(low int, high int, zero int, one int) int {
	return countGoodStringsRecursiveHelper(low, high, zero, one, 0)
}

func countGoodStringsTopDownHelper(low int, high int, zero int, one int, l int, mem map[int]int) int {
	if l > high {
		return 0
	}
	key := l
	if _, solved := mem[key]; !solved {
		ways := 0
		if l >= low {
			ways++
		}
		add_zero := countGoodStringsTopDownHelper(low, high, zero, one, l+zero, mem)
		add_one := countGoodStringsTopDownHelper(low, high, zero, one, l+one, mem)
		mem[key] = ((ways+add_zero)%MOD + add_one) % MOD
	}
	return mem[key]
}

func countGoodStringsTopDown(low int, high int, zero int, one int) int {
	mem := make(map[int]int)
	return countGoodStringsTopDownHelper(low, high, zero, one, 0, mem)
}

func countGoodStringsBottomUp(low int, high int, zero int, one int) int {
	dp := make([]int, high+1)
	dp[0] = 1
	for i := 1; i <= high; i++ {
		if i >= zero {
			dp[i] = (dp[i] + dp[i-zero]) % MOD
		}
		if i >= one {
			dp[i] = (dp[i] + dp[i-one]) % MOD
		}
	}
	res := 0
	for i := low; i <= high; i++ {
		res = (res + dp[i]) % MOD
	}
	return res
}
