package main

func calculate(s string) int {
	stk := make([]int, 0)
	num := 0
	sign := '+'
	for _, c := range s + "+" {
		if c == ' ' {
			continue
		}
		if c >= '0' && c <= '9' {
			num = num*10 + int(c-'0')
		} else {
			switch sign {
			case '+':
				stk = append(stk, num)
			case '-':
				stk = append(stk, -num)
			case '*':
				stk[len(stk)-1] *= num
			case '/':
				stk[len(stk)-1] /= num
			}
			sign = c
			num = 0
		}
	}
	total := 0
	for _, v := range stk {
		total += v
	}
	return total
}
