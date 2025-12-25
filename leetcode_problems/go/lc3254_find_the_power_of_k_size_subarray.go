package main

func resultsArray(nums []int, k int) []int {
	n := len(nums)
	if n == 1 || k == 1 {
		return nums
	}
	ans := make([]int, n-k+1)
	for i := range ans {
		ans[i] = -1
	}
	i := 0
	j := 0
	for i < n-k+1 {
		if j > i && nums[j-1]+1 != nums[j] {
			i++
			j = i
			continue
		}
		if j-i+1 == k {
			ans[i] = nums[j]
			i++
			j = i
		} else if j+1 < n {
			j++
		} else {
			break
		}
	}
	return ans
}
