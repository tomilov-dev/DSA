package main

import "strings"

func evaluate1807(s string, knowledge [][]string) string {
	mp := make(map[string]string)
	for _, know := range knowledge {
		mp[know[0]] = know[1]
	}
	var res strings.Builder
	i := 0
	for i < len(s) {
		if s[i] == '(' {
			j := i + 1
			for j < len(s) && s[j] != ')' {
				j++
			}
			key := s[i+1 : j]
			val, matched := mp[key]
			if !matched {
				val = "?"
			}
			res.WriteString(val)
			i = j + 1
		} else {
			res.WriteByte(s[i])
			i++
		}
	}
	return res.String()
}
