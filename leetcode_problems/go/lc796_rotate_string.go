package main

import "strings"

func rotateStringHelper(s string, goal string, i int, j int) (int, int) {
	n := len(s)
	for i < n && j < n {
		if s[i] == goal[j] {
			i++
			j++
		} else {
			break
		}
	}
	return i, j
}

func rotateString(s string, goal string) bool {
	if len(s) != len(goal) {
		return false
	}
	n := len(s)
	for i := 0; i < n; i++ {
		is, js := rotateStringHelper(s, goal, i, 0)
		if is >= n {
			_, je := rotateStringHelper(s, goal, is%n, js%n)
			if je >= n {
				return true
			}
		}
	}
	return false
}

func rotateStringGoStyle(s string, goal string) bool {
	return len(s) == len(goal) && strings.Contains(s+s, goal)
}
