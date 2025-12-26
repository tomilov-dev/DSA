package main

func minSwaps(s string) int {
	stack := make([]rune, 0)
	for _, c := range s {
		if len(stack) == 0 {
			stack = append(stack, c)
			continue
		}
		i := len(stack) - 1
		if stack[i] == '[' && c == ']' {
			stack = stack[:i]
		} else {
			stack = append(stack, c)
		}
	}
	return (len(stack)/2 + 1) / 2 // it means ceil(len(stack) / 4)
}

func minSwapsOptimal(s string) int {
	balance := 0
	maxUnbalanced := 0
	for _, c := range s {
		if c == '[' {
			balance++
		} else {
			balance--
			if balance < 0 {
				maxUnbalanced++
				balance = 0
			}
		}
	}
	return (maxUnbalanced + 1) / 2
}
