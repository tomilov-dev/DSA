package main

import "math"

func maximumSubarraySum(nums []int, k int) int64 {
	n := len(nums)
	maxi := math.MinInt64
	prefix := make([]int, n+1)
	mp := make(map[int]int)
	for i, num := range nums {
		prefix[i+1] = prefix[i] + num
		if j, exists := mp[num-k]; exists {
			maxi = max(maxi, prefix[i+1]-prefix[j])
		}
		if j, exists := mp[num+k]; exists {
			maxi = max(maxi, prefix[i+1]-prefix[j])
		}
		if k, exists := mp[num]; !exists || prefix[i]-prefix[k] <= 0 {
			// Алгоритм Кадане - суть в том, чтобы начать новую последовательность:
			// 1. Если последовательности начинающейся с num не существует
			// 2. Если на текущий момент сумма последовательности меньше или равна 0, начинаем новую
			mp[num] = i
		}
	}
	if maxi == math.MinInt64 {
		return 0
	}
	return int64(maxi)
}
