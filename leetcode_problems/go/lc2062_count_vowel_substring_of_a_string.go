package main

func countVowelSubstringsCheck(mp map[byte]int) bool {
	vowels := []byte{'a', 'e', 'i', 'o', 'u'}
	for _, v := range vowels {
		if mp[v] < 1 {
			return false
		}
	}
	return true
}

func countVowelSubstringsReverseCheck(c byte) bool {
	if c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u' {
		return true
	}
	return false
}

func countVowelSubstringsBF(word string) int {
	n := len(word)
	c := 0
	for i := 0; i < n; i++ {
		mp := make(map[byte]int)
		for j := i; j < n; j++ {
			if countVowelSubstringsReverseCheck(word[j]) {
				break
			}
			mp[word[j]]++
			if countVowelSubstringsCheck(mp) {
				c++
			}
		}
	}
	return c
}

func countVowelSubstringsSlidingWindow(word string) int {
	vowels := map[byte]bool{'a': true, 'e': true, 'i': true, 'o': true, 'u': true}
	n := len(word)
	c := 0
	mp := make([]int, 123)
	vow := 0
	j, k := 0, 0

	for i := 0; i < n; i++ {
		if vowels[word[i]] {
			mp[word[i]]++
			if mp[word[i]] == 1 {
				vow++
			}
			for vow == 5 {
				mp[word[k]]--
				if mp[word[k]] == 0 {
					vow--
				}
				k++
			}
			c += k - j
		} else {
			mp['a'], mp['e'], mp['i'], mp['o'], mp['u'] = 0, 0, 0, 0, 0
			vow = 0
			j, k = i+1, i+1
		}
	}
	return c
}
