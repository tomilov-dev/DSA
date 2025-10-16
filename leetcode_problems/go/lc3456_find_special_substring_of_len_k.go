package main

func hasSpecialSubstring(s string, k int) bool {
	str := []rune(s)
	n := len(str)
	for i := 0; i <= n-k; i++ {
		first := str[i]
		special := true
		for j := i + 1; j < i+k; j++ {
			if first != str[j] {
				special = false
				break
			}
		}
		if i > 0 && first == str[i-1] {
			special = false
		}
		if i+k < n && first == str[i+k] {
			special = false
		}
		if special {
			return true
		}
	}
	return false
}
