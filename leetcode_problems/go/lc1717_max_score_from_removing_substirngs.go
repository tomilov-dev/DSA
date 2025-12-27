package main

func removePair(s string, a, b rune, score int) (string, int) {
	stk := make([]rune, 0)
	total := 0
	for _, c := range s {
		if len(stk) > 0 && stk[len(stk)-1] == a && c == b {
			stk = stk[:len(stk)-1]
			total += score
		} else {
			stk = append(stk, c)
		}
	}
	return string(stk), total
}

func maximumGain(s string, x int, y int) int {
	total := 0
	if x >= y {
		var t int
		s, t = removePair(s, 'a', 'b', x)
		total += t
		_, t = removePair(s, 'b', 'a', y)
		total += t
	} else {
		var t int
		s, t = removePair(s, 'b', 'a', y)
		total += t
		_, t = removePair(s, 'a', 'b', x)
		total += t
	}
	return total
}
