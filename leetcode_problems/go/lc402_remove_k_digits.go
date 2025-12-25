package main

func removeKdigits(num string, k int) string {
	stack := make([]rune, 0)
	for _, c := range num {
		for k > 0 && len(stack) > 0 && stack[len(stack)-1] > c {
			stack = stack[:len(stack)-1]
			k--
		}
		stack = append(stack, c)
	}
	if k > 0 {
		stack = stack[:len(stack)-k]
	}
	i := 0
	for i < len(stack) && stack[i] == '0' {
		i++
	}
	res := string(stack[i:])
	if res == "" {
		return "0"
	}
	return res
}
