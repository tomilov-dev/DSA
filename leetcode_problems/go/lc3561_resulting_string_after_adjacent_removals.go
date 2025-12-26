package main

func resultingString(s string) string {
	stack := make([]rune, 0)
	for _, c := range s {
		if len(stack) == 0 {
			stack = append(stack, c)
			continue
		}
		p := stack[len(stack)-1]
		diff := abs(int(p - c))
		if diff == 1 || diff == 25 {
			stack = stack[:len(stack)-1]
		} else {
			stack = append(stack, c)
		}
	}
	return string(stack)
}
