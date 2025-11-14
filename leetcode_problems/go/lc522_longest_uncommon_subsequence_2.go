package main

import "sort"

func findLUSlengthisSubsequence(a, b string) bool {
	j := 0
	for i := 0; i < len(b) && j < len(a); i++ {
		if a[j] == b[i] {
			j++
		}
	}
	return j == len(a)
}

func findLUSlength2(strs []string) int {
	sort.Slice(strs, func(i, j int) bool {
		return len(strs[i]) > len(strs[j])
	})

	for i, s := range strs {
		found := false
		for j, t := range strs {
			if i == j {
				continue
			}
			if findLUSlengthisSubsequence(s, t) {
				found = true
				break
			}
		}
		if !found {
			return len(s)
		}
	}
	return -1
}
