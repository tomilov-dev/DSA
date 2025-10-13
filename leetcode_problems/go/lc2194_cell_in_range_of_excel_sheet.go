package main

func cellsInRange(s string) []string {
	l1 := rune(s[0])
	n1 := int(s[1])
	l2 := rune(s[3])
	n2 := int(s[4])
	res := make([]string, 0)
	letters := []rune{'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
		'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
	for _, letter := range letters {
		if letter < l1 || letter > l2 {
			continue
		}
		for num := n1; num <= n2; num++ {
			res = append(res, string(letter)+string(num))
		}
	}
	return res
}

func cellsInRangeGoWay(s string) []string {
	l1, l2 := s[0], s[3]
	n1, n2 := int(s[1]-'0'), int(s[4]-'0')
	res := make([]string, 0)
	for l := l1; l <= l2; l++ {
		for n := n1; n <= n2; n++ {
			res = append(res, string(l)+string('0'+byte(n)))
		}
	}
	return res
}
