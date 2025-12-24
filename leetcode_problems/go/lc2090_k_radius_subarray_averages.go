package main

func getAverages(nums []int, k int) []int {
	n := len(nums)
	ans := make([]int, n)
	for i := range ans {
		ans[i] = -1
	}
	s := 0
	i := 0
	for j, nj := range nums {
		s += nj
		if j-i < 2*k {
			continue
		}
		avg := s / (j - i + 1)
		ans[j-k] = avg
		s -= nums[i]
		i++
	}
	return ans
}
