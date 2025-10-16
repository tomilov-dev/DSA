package main

func findKOr(nums []int, k int) int {
	ans := 0
	for bit := 0; bit < 32; bit++ {
		cnt := 0
		for _, num := range nums {
			if (num>>bit)&1 == 1 {
				cnt++
			}
		}
		if cnt >= k {
			ans |= 1 << bit
		}
	}
	return ans
}
