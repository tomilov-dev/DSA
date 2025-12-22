package main

func isVowel(ch rune) bool {
	return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u'
}

func countOfSubstrings(word string, k int) int64 {
	r := []rune(word)
	n := len(r)
	vowels := make(map[rune]int)
	consonantCount := 0
	total := int64(0)

	nextConsonant := make([]int, n)
	lastConsonant := n
	for i := n - 1; i >= 0; i-- {
		nextConsonant[i] = lastConsonant
		if !isVowel(r[i]) {
			lastConsonant = i
		}
	}

	left, right := 0, 0
	for right < n {
		if isVowel(r[right]) {
			vowels[r[right]]++
		} else {
			consonantCount++
		}

		for left <= right && consonantCount > k {
			if isVowel(r[left]) {
				vowels[r[left]]--
				if vowels[r[left]] == 0 {
					delete(vowels, r[left])
				}
			} else {
				consonantCount--
			}
			left++
		}

		for left < right && len(vowels) == 5 && consonantCount == k {
			total += int64(nextConsonant[right] - right)
			if isVowel(r[left]) {
				vowels[r[left]]--
				if vowels[r[left]] == 0 {
					delete(vowels, r[left])
				}
			} else {
				consonantCount--
			}
			left++
		}

		right++
	}

	return total
}
