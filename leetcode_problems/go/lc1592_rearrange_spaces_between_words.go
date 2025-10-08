package main

import "strings"

func reorderSpaces(text string) string {
	spaces := 0
	words := []string{}
	wordRunes := []rune{}
	for _, char := range text {
		if char == ' ' {
			spaces++
			if len(wordRunes) > 0 {
				words = append(words, string(wordRunes))
				wordRunes = wordRunes[:0]
			}
		} else {
			wordRunes = append(wordRunes, char)
		}
	}
	if len(wordRunes) > 0 {
		words = append(words, string(wordRunes))
	}

	n := len(words)
	var space string
	var space_end string
	if n > 1 {
		space_len := spaces / (n - 1)
		space_end_len := spaces % (n - 1)
		space = strings.Repeat(" ", space_len)
		space_end = strings.Repeat(" ", space_end_len)
	} else {
		space = ""
		space_end = strings.Repeat(" ", spaces)
	}
	return strings.Join(words, space) + space_end
}
