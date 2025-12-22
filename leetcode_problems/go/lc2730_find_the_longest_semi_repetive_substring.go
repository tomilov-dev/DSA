package main

func longestSemiRepetitiveSubstring(s string) int {
	r := []rune(s)
	maxi := 0
	i := 0
	adj := 0
	prev := [2]int{0, 0}
	for j := range r {
		if j > 0 && r[j] == r[j-1] {
			adj++
			prev[0] = prev[1]
			prev[1] = j
		}
		if adj <= 1 {
			maxi = max(maxi, j-i+1)
		} else {
			adj--
			i = prev[0]
		}
	}
	return maxi
}

func longestSemiRepetitiveSubstringTwoLoops(s string) int {
	r := []rune(s)
	i := 0
	adj := 0
	n := len(r)
	maxi := 1
	for j := 1; j < n; j++ {
		if r[j] == r[j-1] {
			adj++
		}
		for adj > 1 {
			i++
			if r[i] == r[i-1] {
				adj--
			}
		}
		if j-i+1 > maxi {
			maxi = j - i + 1
		}
	}
	return maxi
}
