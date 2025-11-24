package main

func findDuplicates(nums []int) []int {
	res := make([]int, 0)
	for _, num := range nums {
		idx := abs(num) - 1
		if nums[idx] < 0 {
			res = append(res, abs(num))
		} else {
			nums[idx] = -nums[idx]
		}
	}
	return res
}
