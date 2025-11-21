package main

func countPalindromicSubsequence(s string) int {
	mp := make(map[rune]int)
	uniq := make(map[[3]rune]struct{})
	runes := []rune(s)
	for i, c := range runes {
		fq := mp[c]
		if fq >= 1 {
			for j := i - 1; j >= 0 && runes[j] != c; j-- {
				uniq[[3]rune{c, runes[j], c}] = struct{}{}
			}
		}
		if fq == 2 {
			uniq[[3]rune{c, c, c}] = struct{}{}
		}
		mp[c] = fq + 1
	}
	return len(uniq)
}

func countPalindromicSubsequenceOptimized(s string) int {
	first := make([]int, 26)
	last := make([]int, 26)
	for i := range first {
		first[i] = 1 << 20
		last[i] = -1
	}
	for i := 0; i < len(s); i++ {
		sym := int(s[i] - 'a')
		if i < first[sym] {
			first[sym] = i
		}
		last[sym] = i
	}
	res := 0
	for i := 0; i < 26; i++ {
		if first[i] >= last[i] {
			continue
		}

		subset := make(map[byte]struct{})
		for j := first[i] + 1; j < last[i]; j++ {
			subset[s[j]] = struct{}{}
		}
		res += len(subset)
	}
	return res
}
