package main

import (
	"math"
	"unicode"
)

func reformat(s string) string {
	new := make([]rune, 0)
	let := make([]rune, 0)
	dig := make([]rune, 0)
	for _, char := range s {
		if unicode.IsDigit(char) {
			dig = append(dig, char)
		} else {
			let = append(let, char)
		}
	}
	if math.Abs(float64(len(let)-len(dig))) > 1 {
		return ""
	}
	if len(let) > len(dig) {
		for i := 0; i < max(len(let), len(dig)); i++ {
			if i < len(let) {
				new = append(new, let[i])
			}
			if i < len(dig) {
				new = append(new, dig[i])
			}
		}
	} else {
		for i := 0; i < max(len(let), len(dig)); i++ {
			if i < len(dig) {
				new = append(new, dig[i])
			}
			if i < len(let) {
				new = append(new, let[i])
			}
		}
	}
	return string(new)
}
