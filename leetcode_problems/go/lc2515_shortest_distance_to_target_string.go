package main

import "math"

func closestTarget(words []string, target string, startIndex int) int {
	short := math.MaxInt64
	n := len(words)
	for i := 0; i < n; i++ {
		if words[i] == target {
			left := int(math.Abs(float64(startIndex - i)))
			right := n - int(math.Abs(float64(startIndex-i)))
			short = min(short, left, right)
		}
	}
	if short == math.MaxInt64 {
		short = -1
	}
	return short
}
