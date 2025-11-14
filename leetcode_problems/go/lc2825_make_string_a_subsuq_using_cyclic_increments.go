package main

func canMakeSubsequenceIsGood(c1 rune, c2 rune) bool {
	if c1 == c2 {
		return true
	}
	if (c1-'a'+1)%26 == c2-'a' {
		return true
	}
	return false
}

func canMakeSubsequence(str1 string, str2 string) bool {
	r1 := []rune(str1)
	r2 := []rune(str2)
	n := len(r1)
	m := len(r2)
	if n < m {
		return false
	}
	p1 := 0
	p2 := 0
	for p1 < n && p2 < m {
		if canMakeSubsequenceIsGood(r1[p1], r2[p2]) {
			p1++
			p2++
		} else {
			p1++
		}
	}
	return p2 == m
}
