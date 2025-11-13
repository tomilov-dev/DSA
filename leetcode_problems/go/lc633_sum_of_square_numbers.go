package main

import "math"

func judgeSquareSum(c int) bool {
	sq := int(math.Sqrt(float64(c)))
	low := 0
	high := sq
	for high >= low {
		sum := low*low + high*high
		if sum == c {
			return true
		} else if sum > c {
			high--
		} else {
			low++
		}
	}
	return false
}
