package main

func minimumSizeCheck(nums []int, maxOperations, x int) bool {
	c := 0
	for _, num := range nums {
		c += (num - 1) / x
	}
	return c > maxOperations
}

func minimumSizeMaxNum(nums []int) int {
	maxi := 0
	for _, num := range nums {
		maxi = max(maxi, num)
	}
	return maxi
}

func minimumSize(nums []int, maxOperations int) int {
	l := 0
	h := minimumSizeMaxNum(nums) + 1
	// h := 1_000_000_001
	for h-l > 1 {
		m := l + (h-l)/2
		if minimumSizeCheck(nums, maxOperations, m) {
			l = m
		} else {
			h = m
		}
	}
	return h
}
