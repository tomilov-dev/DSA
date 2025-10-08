package main

import "math"

func maxSum(nums []int) int {
	mem := make(map[int]struct{})
	sum := 0
	maxi := math.MinInt64
	for _, num := range nums {
		maxi = max(maxi, num)
		if num < 0 {
			continue
		}
		if _, exists := mem[num]; !exists {
			sum += num
			mem[num] = struct{}{}
		}
	}
	if len(mem) == 0 {
		return maxi
	}
	return sum
}
