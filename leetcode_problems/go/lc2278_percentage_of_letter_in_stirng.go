package main

func percentageLetter(s string, letter byte) int {
	c := 0
	for _, char := range s {
		if char == rune(letter) {
			c++
		}
	}
	return int(float64(c) / float64(len(s)) * 100)
}
