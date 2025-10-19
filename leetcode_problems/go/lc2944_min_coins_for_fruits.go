package main

import "math"

func minimumCoinsRecursiveHelper(prices []int, i int, free int) int {
	if i >= len(prices) {
		return 0
	}
	// op. 1 - buy
	buy := prices[i] + minimumCoinsRecursiveHelper(prices, i+1, i+1)
	// op. 2 - take free
	take := math.MaxInt
	if free > 0 {
		take = minimumCoinsRecursiveHelper(prices, i+1, free-1)
	}
	return min(buy, take)
}

func minimumCoinsRecursive(prices []int) int {
	return prices[0] + minimumCoinsRecursiveHelper(prices, 1, 1)
}

func minimumCoinsTopDownHelper(prices []int, i int, free int, mem map[[2]int]int) int {
	if i >= len(prices) {
		return 0
	}
	key := [2]int{i, free}
	if _, solved := mem[key]; !solved {
		// op. 1 - buy
		buy := prices[i] + minimumCoinsTopDownHelper(prices, i+1, i+1, mem)
		// op. 2 - take free
		take := math.MaxInt
		if free > 0 {
			take = minimumCoinsTopDownHelper(prices, i+1, free-1, mem)
		}
		mem[key] = min(buy, take)
	}
	return mem[key]
}

func minimumCoinsTopDown(prices []int) int {
	mem := make(map[[2]int]int)
	return prices[0] + minimumCoinsTopDownHelper(prices, 1, 1, mem)
}

func minimumCoinsBottomUp(prices []int) int {
	n := len(prices)
	maxFree := n + 1
	dp := make([][]int, n+1)
	for i := range dp {
		dp[i] = make([]int, maxFree)
		for j := range dp[i] {
			dp[i][j] = math.MaxInt
		}
	}
	// База: если все фрукты собраны, стоимость 0
	for free := 0; free < maxFree; free++ {
		dp[n][free] = 0
	}
	for i := n - 1; i >= 0; i-- {
		for free := 0; free < maxFree; free++ {
			// 1. Купить фрукт i
			buy := prices[i] + dp[i+1][i+1]
			// 2. Взять бесплатно, если есть бесплатные
			take := math.MaxInt
			if free > 0 {
				take = dp[i+1][free-1]
			}
			dp[i][free] = min(buy, take)
		}
	}
	return dp[0][0]
}

func minimumCoins(prices []int) int {
	n := len(prices)
	dp := make([]int, n+1)
	for i := range dp {
		dp[i] = math.MaxInt
	}
	dp[0] = 0
	// Формируем dp массив, т.к. n + 1 то начинаем с 1
	for i := 1; i <= n; i++ {
		// На этом этапе мы делаем следующее
		// Берем диапазон индексов меньше или равных i - текущей позиции
		// С помощью условия j + j >= i проверяем - достигается ли i-й индекс по условиям бесплатного получения
		// Если достигается, то мы проверяем вариант: купить j-й индекс и взять i-й индекс бесплатно
		// Соответственно, для этого мы берем j-1 цену (т.к. итерируем dp[1, n + 1])
		// А также добавляем dp[j - 1] - это минимальная стоимость товаров до j-й покупки
		for j := i; j+j >= i; j-- {
			dp[i] = min(dp[i], dp[j-1]+prices[j-1])
		}
	}
	return dp[n]
}
