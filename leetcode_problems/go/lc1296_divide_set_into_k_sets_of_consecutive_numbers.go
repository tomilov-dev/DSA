package main

import "sort"

func isPossibleDivide(nums []int, k int) bool {
	mp := make(map[int]int)
	for _, num := range nums {
		mp[num]++
	}
	keys := make([]int, 0, len(mp))
	for k := range mp {
		keys = append(keys, k)
	}
	sort.Ints(keys)
	for _, i := range keys {
		if mp[i] == 0 {
			continue
		}
		c := mp[i]
		for j := i; j < i+k; j++ {
			if mp[j] < c {
				return false
			}
			mp[j] -= c
		}
	}
	return true
}
