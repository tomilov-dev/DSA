package main

import (
	"strconv"
	"strings"
)

func sortSentence(s string) string {
	n := 1
	for _, ch := range s {
		if ch == ' ' {
			n++
		}
	}
	words := make([]string, n)

	start := 0
	for end, char := range s {
		if char == ' ' {
			index, _ := strconv.Atoi(s[end-1 : end])
			words[index-1] = s[start : end-1]
			start = end + 1
		}
	}
	index, _ := strconv.Atoi(s[len(s)-1:])
	words[index-1] = s[start : len(s)-1]
	return strings.Join(words, " ")
}

func sortSentenceGoWay(s string) string {
	parts := strings.Split(s, " ")
	words := make([]string, len(parts))
	for _, part := range parts {
		l := len(part)
		index, _ := strconv.Atoi(part[l-1:])
		words[index-1] = part[:l-1]
	}
	return strings.Join(words, " ")
}
