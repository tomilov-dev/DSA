package main

func left_smaller(nums []int) int {
	for i := len(nums) - 1; i > 0; i-- {
		if nums[i-1] < nums[i] {
			return i - 1
		}
	}
	return -1
}

func right_bigger(nums []int, left int) int {
	for i := len(nums) - 1; i >= left; i-- {
		if nums[i] > nums[left] {
			return i
		}
	}
	return -1
}

func reverse_tail(nums []int, ifrom int) {
	p1 := ifrom
	p2 := len(nums) - 1
	for p1 < p2 {
		nums[p1], nums[p2] = nums[p2], nums[p1]
		p1++
		p2--
	}
}

func nextPermutation(nums []int) {
	left := left_smaller(nums)
	if left == -1 {
		reverse_tail(nums, 0)
		return
	}

	right := right_bigger(nums, left)
	nums[left], nums[right] = nums[right], nums[left]
	reverse_tail(nums, left+1)
}
