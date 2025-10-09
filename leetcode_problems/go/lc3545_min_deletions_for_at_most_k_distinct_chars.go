package main

import "sort"

func minDeletion(s string, k int) int {
	mem := make(map[rune]int)
	for _, char := range s {
		mem[char]++
	}
	freqs := make([]int, 0, len(mem))
	for _, count := range mem {
		freqs = append(freqs, count)
	}
	sort.Sort(sort.Reverse(sort.IntSlice(freqs)))
	sum := 0
	for i := k; i < len(freqs); i++ {
		sum += freqs[i]
	}
	return sum
}
