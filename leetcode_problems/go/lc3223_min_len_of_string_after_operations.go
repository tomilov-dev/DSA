package main

func minimumLength(s string) int {
	count := make([]int, 26)
	for _, c := range s {
		count[int(c-'a')]++
	}
	minlen := 0
	for _, q := range count {
		if q == 0 {
			continue
		}
		if q%2 == 0 {
			minlen += 2
		} else {
			minlen += 1
		}
	}
	return minlen
}
