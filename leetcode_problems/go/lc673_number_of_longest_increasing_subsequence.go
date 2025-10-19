package main

func findNumberOfLIS(nums []int) int {
	n := len(nums)
	dpl := make([]int, n)
	dpc := make([]int, n)
	maxl := 1
	for i := range dpl {
		dpl[i] = 1
		dpc[i] = 1
	}
	for i := 1; i < n; i++ {
		for j := i - 1; j >= 0; j-- {
			if nums[i] > nums[j] {
				if 1+dpl[j] > dpl[i] {
					dpl[i] = dpl[j] + 1
					dpc[i] = dpc[j]
				} else if 1+dpl[j] == dpl[i] {
					dpc[i] += dpc[j]
				}
			}
			maxl = max(maxl, dpl[i])
		}
	}
	total := 0
	for i := range dpl {
		if dpl[i] == maxl {
			total += dpc[i]
		}
	}
	return total
}
