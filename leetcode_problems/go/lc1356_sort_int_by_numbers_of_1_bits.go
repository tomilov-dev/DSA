package main

import (
	"math/bits"
	"sort"
)

func sortByBits(arr []int) []int {
	tosort := make([][]int, 0, len(arr))
	for _, num := range arr {
		c := bits.OnesCount(uint(num))
		tosort = append(tosort, []int{c, num})
	}

	sort.Slice(tosort, func(i, j int) bool {
		if tosort[i][0] == tosort[j][0] {
			return tosort[i][1] < tosort[j][1]
		}
		return tosort[i][0] < tosort[j][0]
	})

	res := make([]int, 0, len(arr))
	for _, sub := range tosort {
		res = append(res, sub[1])
	}
	return res
}
