package main

import (
	"math"
	"sort"
)

func successfulPairs(spells []int, potions []int, success int64) []int {
	sort.Ints(potions)
	n := len(spells)
	right := len(potions)
	res := make([]int, 0, n)
	for _, sp := range spells {
		target := int(math.Ceil(float64(success) / float64(sp)))
		left := sort.SearchInts(potions, target)
		res = append(res, right-left)
	}
	return res
}
