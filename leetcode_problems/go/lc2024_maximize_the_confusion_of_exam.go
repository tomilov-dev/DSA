package main

func maxConsecutiveAnswers(answerKey string, k int) int {
	runes := []rune(answerKey)
	n := len(runes)
	maxf := 0
	i := 0
	mp := make(map[rune]int)
	for j := range n {
		c := runes[j]
		mp[c]++
		maxf = max(maxf, mp[c])
		if j-i+1 > maxf+k {
			mp[runes[i]]--
			i++
		}
	}
	return n - i
}
