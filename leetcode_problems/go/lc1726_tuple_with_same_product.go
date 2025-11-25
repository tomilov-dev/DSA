package main

func tupleSameProduct(nums []int) int {
	res := 0
	mp := make(map[int]int)
	for i := range nums {
		for j := i + 1; j < len(nums); j++ {
			key := nums[i] * nums[j]
			res += mp[key]
			mp[key]++
		}
	}
	return 8 * res
}
