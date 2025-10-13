package main

import "strings"

func hasMatch(s string, p string) bool {
	parts := strings.Split(p, "*")
	if len(parts) != 2 {
		return false
	}
	prefix, suffix := parts[0], parts[1]
	start := strings.Index(s, prefix)
	if start == -1 {
		return false
	}
	rest := s[start+len(prefix):]
	return strings.Contains(rest, suffix)
}
