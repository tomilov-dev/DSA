package main

import "strings"

func interpret(command string) string {
	arr := make([]string, 0)
	skip := 0
	for i, char := range command {
		if skip > 0 {
			skip--
			continue
		}
		if char == 'G' {
			arr = append(arr, "G")
		} else if char == '(' && command[i:i+2] == "(a" {
			arr = append(arr, "al")
			skip = 3
		} else {
			arr = append(arr, "o")
			skip = 1
		}
	}
	return strings.Join(arr, "")
}

func interpretGoWay(command string) string {
	res := strings.ReplaceAll(command, "()", "o")
	res = strings.ReplaceAll(res, "(al)", "al")
	return res
}
