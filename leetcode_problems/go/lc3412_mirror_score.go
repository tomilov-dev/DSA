package main

func calculateScore(s string) int64 {
	total := 0
	stk := make(map[int][]int)
	mir := make([]int, 26)
	for i := range 26 {
		mir[25-i] = i
	}
	for i, c := range s {
		x := int(c - 'a')
		if idxs, exists := stk[mir[x]]; exists && len(idxs) > 0 {
			j := idxs[len(idxs)-1]
			stk[mir[x]] = idxs[:len(idxs)-1]
			total += i - j
		} else {
			if _, exists := stk[x]; !exists {
				stk[x] = make([]int, 0)
			}
			stk[x] = append(stk[x], i)
		}
	}
	return int64(total)
}
