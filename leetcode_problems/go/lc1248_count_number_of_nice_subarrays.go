package main

func numberOfSubarrays(nums []int, k int) int {
	i := 0
	count := 0
	total := 0
	for j := range nums {
		if nums[j]%2 == 1 {
			k--
			count = 0
		}
		for k == 0 {
			if nums[i]%2 == 1 {
				k++
			}
			i++
			count++
		}
		total += count
	}
	return total
}

func numberOfSubarraysWithAtMostPattern(nums []int, k int) int {
	return numberOfSubarraysAtMost(nums, k) - numberOfSubarraysAtMost(nums, k-1)
}

func numberOfSubarraysAtMost(nums []int, k int) int {
	i := 0
	total := 0
	for j := range nums {
		if nums[j]%2 == 1 {
			k--
		}
		for k < 0 {
			if nums[i]%2 == 1 {
				k++
			}
			i++
		}
		total += j - i + 1
	}
	return total
}
