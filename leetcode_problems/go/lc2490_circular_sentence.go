package main

import "strings"

func isCircularSentence(sentence string) bool {
	words := strings.Split(sentence, " ")
	n := len(words)
	for i := range words {
		w1 := []rune(words[i%n])
		w2 := []rune(words[(i+1)%n])
		if w1[len(w1)-1] != w2[0] {
			return false
		}
	}
	return true
}
