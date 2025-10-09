package main

func findMiddleIndex(nums []int) int {
	left := 0
	right := 0
	for _, num := range nums {
		right += num
	}
	for i, num := range nums {
		right -= num
		if left == right {
			return i
		}
		left += num
	}
	return -1
}
