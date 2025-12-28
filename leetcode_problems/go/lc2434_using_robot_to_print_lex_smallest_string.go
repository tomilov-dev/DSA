package main

func robotWithString(s string) string {
	r := []rune(s)
	n := len(r)
	rbt := make([]rune, 0)
	res := make([]rune, 0)
	suff := make([]rune, n+1)
	for i := range suff {
		suff[i] = '}'
	}
	for i := n - 1; i >= 0; i-- {
		suff[i] = min(suff[i+1], rune(s[i]))
	}
	for i, c := range s {
		nxtMin := suff[i+1]
		rbt = append(rbt, c)
		for len(rbt) > 0 && rbt[len(rbt)-1] <= nxtMin {
			res = append(res, rbt[len(rbt)-1])
			rbt = rbt[:len(rbt)-1]
		}
	}
	for len(rbt) > 0 {
		res = append(res, rbt[len(rbt)-1])
		rbt = rbt[:len(rbt)-1]
	}
	return string(res)
}
