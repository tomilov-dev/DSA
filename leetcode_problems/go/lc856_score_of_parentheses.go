package main

func scoreOfParentheses(s string) int {
	stk := make([]int, 0)
	total := 0
	for _, c := range s {
		l := len(stk)
		if c == '(' {
			stk = append(stk, total)
			total = 0
		} else {
			total += stk[l-1] + max(total, 1)
			stk = stk[:l-1]
		}
	}
	return total
}
