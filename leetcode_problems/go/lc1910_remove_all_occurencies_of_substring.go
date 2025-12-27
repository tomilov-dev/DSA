package main

func removeOccurrences(s string, part string) string {
	stk := make([]rune, 0)
	for _, c := range s {
		stk = append(stk, c)
		if len(stk) < len(part) {
			continue
		}
		if string(stk[len(stk)-len(part):]) == part {
			stk = stk[:len(stk)-len(part)]
		}
	}
	return string(stk)
}
