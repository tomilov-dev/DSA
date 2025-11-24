package main

import "strings"

func spellcheckerVowelInsensitive(w string) string {
	vowels := []string{"a", "e", "i", "o", "u"}
	res := w
	for _, vowel := range vowels {
		res = strings.ReplaceAll(res, vowel, "_")
	}
	return res
}

func spellcheckerCaseInsensitive(w string) string {
	return strings.ToLower(w)
}

func spellchecker(wordlist []string, queries []string) []string {
	caseMap := make(map[string]string)
	noCaseMap := make(map[string]string)
	vowelMap := make(map[string]string)
	for _, w := range wordlist {
		caseMap[w] = w

		ci := spellcheckerCaseInsensitive(w)
		vi := spellcheckerVowelInsensitive(ci)
		if _, exists := noCaseMap[ci]; !exists {
			noCaseMap[ci] = w
		}
		if _, exists := vowelMap[vi]; !exists {
			vowelMap[vi] = w
		}
	}
	res := make([]string, 0)
	for _, q := range queries {
		if v, matched := caseMap[q]; matched {
			res = append(res, v)
			continue
		}
		ci := spellcheckerCaseInsensitive(q)
		if v, matched := noCaseMap[ci]; matched {
			res = append(res, v)
			continue
		}
		vi := spellcheckerVowelInsensitive(ci)
		if v, matched := vowelMap[vi]; matched {
			res = append(res, v)
			continue
		}
		res = append(res, "")
	}
	return res
}
