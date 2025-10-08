package main

import "strings"

func stringMatching(words []string) []string {
	n := len(words)
	mem := make(map[string]struct{})
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			w1 := words[i]
			w2 := words[j]
			if strings.Contains(w1, w2) {
				mem[w2] = struct{}{}
			}
			if strings.Contains(w2, w1) {
				mem[w1] = struct{}{}
			}
		}
	}
	res := make([]string, 0, len(mem))
	for word := range mem {
		res = append(res, word)
	}
	return res
}
