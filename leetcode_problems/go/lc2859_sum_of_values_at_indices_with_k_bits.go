package main

import "math/bits"

func countBits(n int) int {
	count := 0
	for n > 0 {
		count += n & 1
		n >>= 1
	}
	return count
}

func sumIndicesWithKSetBits(nums []int, k int) int {
	sum := 0
	for i, v := range nums {
		if countBits(i) == k {
			sum += v
		}
	}
	return sum
}

func sumIndicesWithKSetBitsGoPath(nums []int, k int) int {
	sum := 0
	for i, v := range nums {
		if bits.OnesCount(uint(i)) == k {
			sum += v
		}
	}
	return sum
}
