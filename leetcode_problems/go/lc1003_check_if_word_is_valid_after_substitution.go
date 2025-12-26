package main

func isValid(s string) bool {
	stack := make([]rune, 0)
	for _, c := range s {
		if len(stack) < 2 {
			stack = append(stack, c)
			continue
		}
		stack = append(stack, c)
		if string(stack[len(stack)-3:]) == "abc" {
			stack = stack[:len(stack)-3]
		}
	}
	return len(stack) == 0
}
