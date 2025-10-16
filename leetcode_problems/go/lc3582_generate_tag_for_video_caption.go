package main

import "strings"

func generateTag(caption string) string {
	words := strings.Fields(caption)
	for i, word := range words {
		runes := []rune(strings.ToLower(word))
		if len(runes) == 0 {
			words[i] = ""
			continue
		}
		var first_letter rune
		if i == 0 {
			first_letter = runes[0]
		} else {
			first_letter = []rune(strings.ToUpper(string(runes[0])))[0]
		}
		new_word := string(first_letter) + string(runes[1:])
		words[i] = new_word
	}
	str := "#" + strings.Join(words, "")
	return str[:min(len(str), 100)]
}
