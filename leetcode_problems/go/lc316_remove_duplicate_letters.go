package main

func removeDuplicateLetters(s string) string {
	n := len(s)
	sfm := make([][]int, 26)
	for i := range sfm {
		sfm[i] = make([]int, n+1)
	}
	for i := n - 1; i >= 0; i-- {
		for j := range 26 {
			sfm[j][i] = sfm[j][i+1]
		}
		x := s[i] - 'a'
		sfm[x][i]++
	}
	stk := make([]rune, 0)
	added := make([]bool, 26)
	for i, c := range s {
		if len(stk) == 0 {
			stk = append(stk, c)
			added[c-'a'] = true
			continue
		}
		if added[c-'a'] {
			continue
		}
		for len(stk) > 0 && c < stk[len(stk)-1] && sfm[stk[len(stk)-1]-'a'][i+1] > 0 {
			added[stk[len(stk)-1]-'a'] = false
			stk = stk[:len(stk)-1]
		}
		stk = append(stk, c)
		added[c-'a'] = true
	}
	return string(stk)
}
