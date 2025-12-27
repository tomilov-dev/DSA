package main

func minInsertions(s string) int {
	total := 0
	stk := make([]byte, 0)
	for i := 0; i < len(s); i++ {
		c := s[i]
		if c == '(' {
			stk = append(stk, c)
			continue
		}

		if i+1 < len(s) && s[i+1] == ')' {
			i++
		} else {
			total++
		}
		if len(stk) > 0 {
			stk = stk[:len(stk)-1]
		} else {
			total++
		}
	}
	total += 2 * len(stk)
	return total
}
