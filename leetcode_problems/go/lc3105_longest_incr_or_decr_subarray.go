package main

func longestMonotonicSubarray(nums []int) int {
	max_incr := 1
	max_decr := 1
	cur_incr := 1
	cur_decr := 1
	for i := 1; i < len(nums); i++ {
		prev := nums[i-1]
		cur := nums[i]
		if cur > prev {
			cur_incr++
		} else {
			max_incr = max(max_incr, cur_incr)
			cur_incr = 1
		}
		if cur < prev {
			cur_decr++
		} else {
			max_decr = max(max_decr, cur_decr)
			cur_decr = 1
		}
	}
	return max(max_incr, max_decr, cur_incr, cur_decr)
}
