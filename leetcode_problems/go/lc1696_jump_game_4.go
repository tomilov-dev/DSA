package main

import (
	"math"
)

func maxResult(nums []int, k int) int {
	n := len(nums)
	dp := make([]int, n)
	for i := range dp {
		dp[i] = math.MinInt
	}
	dp[0] = 0
	for i := 0; i < n-1; i++ {
		val := nums[i]
		for j := i + 1; j < n && j <= i+k; j++ {
			dp[j] = max(dp[j], dp[i]+val)
		}
	}
	return dp[n-1] + nums[n-1]
}

func maxResultDeq(nums []int, k int) int {
	n := len(nums)
	dp := make([]int, n)
	dp[0] = nums[0]

	// будем хранить интервал с максимальными значениям dp
	// чтобы не обходить k раз массив dp
	q := []int{0}
	for i := 1; i < n; i++ {
		// дропаем все, что не входит в наш интервал
		for len(q) > 0 && q[0] < i-k {
			q = q[1:]
		}
		// заполняем текущий i исходя из [i-k, i)
		dp[i] = dp[q[0]] + nums[i]
		// поддерживаем монотонность - удаляем все, что меньше текущего dp[i]
		for len(q) > 0 && dp[q[len(q)-1]] <= dp[i] {
			q = q[:len(q)-1]
		}
		// добавляем индекс текущего значения dp[i]
		q = append(q, i)
	}
	return dp[n-1]
}
