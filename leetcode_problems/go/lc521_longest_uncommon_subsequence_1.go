package main

func findLUSlength1(a string, b string) int {
	if a == b {
		return -1
	}
	return max(len(a), len(b))
}
