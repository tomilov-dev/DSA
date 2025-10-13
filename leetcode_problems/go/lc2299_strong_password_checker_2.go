package main

import (
	"unicode"
)

func strongPasswordCheckerII(password string) bool {
	if len(password) < 8 {
		return false
	}
	lower_case := false
	upper_case := false
	digit := false
	special := false
	specials := map[rune]struct{}{
		'!': {}, '@': {}, '#': {}, '$': {}, '%': {}, '^': {}, '&': {}, '*': {},
		'(': {}, ')': {}, '-': {}, '+': {},
	}
	prev := ' '
	for _, char := range password {
		if unicode.IsDigit(char) {
			digit = true
		} else if unicode.IsLower(char) {
			lower_case = true
		} else if unicode.IsUpper(char) {
			upper_case = true
		} else if _, is_special := specials[char]; is_special {
			special = true
		}
		if prev == char {
			return false
		}
		prev = char
	}
	return lower_case && upper_case && digit && special
}
