package main

func characterReplacementMaxLen(fq []int) int {
	maxi := 0
	for _, x := range fq {
		maxi = max(maxi, x)
	}
	return maxi
}

func characterReplacement(s string, k int) int {
	n := len(s)
	fq := make([]int, 26)
	maxLen := 0
	i := 0
	maxi := 0
	for j := range n {
		c := int(s[j] - 'A')
		fq[c]++
		maxLen = characterReplacementMaxLen(fq)
		if j-i+1 > maxLen+k {
			fq[int(s[i]-'A')]--
			i++
		}
		if j-i+1 <= maxLen+k {
			maxi = max(maxi, j-i+1)
		}
	}
	return maxi
}
