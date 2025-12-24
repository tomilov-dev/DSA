package main

func countCompleteSubarrays(nums []int) int {
	uniq := make(map[int]struct{})
	for _, num := range nums {
		uniq[num] = struct{}{}
	}
	k := len(uniq)
	total := 0
	i := 0
	c := make(map[int]int)
	for j, num := range nums {
		c[num]++
		for len(c) == k {
			ni := nums[i]
			total += len(nums) - j
			c[ni]--
			if c[ni] == 0 {
				delete(c, ni)
			}
			i++
		}
	}
	return total
}
