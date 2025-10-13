package main

import "strings"

func divideString(s string, k int, fill byte) []string {
	res := make([]string, 0)
	for i := 0; i < len(s); i += k {
		end := i + k
		if end > len(s) {
			group := s[i:] + strings.Repeat(string(fill), end-len(s))
			res = append(res, group)
		} else {
			res = append(res, s[i:end])
		}
	}
	return res
}
