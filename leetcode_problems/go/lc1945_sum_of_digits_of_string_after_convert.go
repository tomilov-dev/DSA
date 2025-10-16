package main

import "strconv"

func getLucky(s string, k int) int {
	digits := ""
	for _, char := range s {
		num := int(char-'a') + 1
		digits += strconv.Itoa(num)
	}
	for k > 0 {
		sum := 0
		for _, d := range digits {
			sum += int(d - '0')
		}
		digits = strconv.Itoa(sum)
		k--
	}
	res, _ := strconv.Atoi(digits)
	return res
}
