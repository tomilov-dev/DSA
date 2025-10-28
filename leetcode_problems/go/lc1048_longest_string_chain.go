package main

import "sort"

func isPredecessor(w2, w1 string) bool {
	r1 := []rune(w1)
	r2 := []rune(w2)
	if len(r1) != len(r2)+1 {
		return false
	}
	add := 0
	i1 := 0
	i2 := 0
	for i1 < len(r1) && i2 < len(r2) {
		if r1[i1] == r2[i2] {
			i1++
			i2++
		} else {
			add++
			i1++
			if add > 1 {
				return false
			}
		}
	}
	if i1 < len(r1) {
		add++
	}
	return add == 1
}

func longestStrChain(words []string) int {
	sort.Slice(words, func(i, j int) bool {
		return len(words[i]) < len(words[j])
	})
	n := len(words)
	dp := make([]int, n)
	for i := range dp {
		dp[i] = 1
	}
	for i := range dp {
		for j := range i {
			if isPredecessor(words[j], words[i]) {
				dp[i] = max(dp[i], dp[j]+1)
			}
		}
	}
	res := 1
	for _, v := range dp {
		res = max(res, v)
	}
	return res
}

func longestStrChainMap(words []string) int {
	wordMap := make(map[string]int)
	sort.Slice(words, func(i, j int) bool {
		return len(words[i]) < len(words[j])
	})
	res := 1
	for _, w := range words {
		wordMap[w] = 1
		for i := 0; i < len(w); i++ {
			prev := w[:i] + w[i+1:]
			if val, ok := wordMap[prev]; ok {
				wordMap[w] = max(wordMap[w], val+1)
			}
		}
		res = max(res, wordMap[w])
	}
	return res
}
