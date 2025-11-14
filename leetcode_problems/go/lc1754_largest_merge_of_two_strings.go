package main

func largestMerge(word1 string, word2 string) string {
	w1 := []rune(word1)
	w2 := []rune(word2)
	merge := make([]rune, 0)
	p1 := 0
	p2 := 0
	for p1 < len(w1) && p2 < len(w2) {
		i, j := p1, p2
		for i < len(w1) && j < len(w2) && w1[i] == w2[j] {
			i++
			j++
		}
		if j == len(w2) || (i < len(w1) && w1[i] > w2[j]) {
			merge = append(merge, w1[p1])
			p1++
		} else {
			merge = append(merge, w2[p2])
			p2++
		}
	}
	for p1 < len(w1) {
		merge = append(merge, w1[p1])
		p1++
	}
	for p2 < len(w2) {
		merge = append(merge, w2[p2])
		p2++
	}
	return string(merge)
}

func largetsMergeCompare(a string, i int, b string, j int) int {
	for i < len(a) && j < len(b) {
		if a[i] != b[j] {
			return int(a[i]) - int(b[j])
		}
		i++
		j++
	}
	return (len(a) - i) - (len(b) - j)
}

func largestMergeWithCompare(word1 string, word2 string) string {
	res := make([]byte, 0, len(word1)+len(word2))
	i, j := 0, 0
	for i < len(word1) && j < len(word2) {
		if largetsMergeCompare(word1, i, word2, j) > 0 {
			res = append(res, word1[i])
			i++
		} else {
			res = append(res, word2[j])
			j++
		}
	}
	res = append(res, word1[i:]...)
	res = append(res, word2[j:]...)
	return string(res)
}
