package main

import "strings"

func truncateSentence(s string, k int) string {
	start := 0
	spaces := 0
	words := make([]string, 0, k)
	for end, char := range s {
		if char == ' ' {
			words = append(words, s[start:end])
			spaces++
			start = end + 1
			if spaces == k {
				break
			}
		}
	}
	if spaces < k {
		words = append(words, s[start:])
	}
	return strings.Join(words, " ")
}

func truncateSentenceGoWay(s string, k int) string {
	trunc := strings.Split(s, " ")
	return strings.Join(trunc[:4], " ")
}
