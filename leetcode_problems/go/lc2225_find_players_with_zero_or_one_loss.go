package main

func findWinners(matches [][]int) [][]int {
	const X = 10_0001
	win := make([]int, X)
	loss := make([]int, X)
	for _, match := range matches {
		win[match[0]]++
		loss[match[1]]++
	}
	res := make([][]int, 0)
	for i := 0; i < 2; i++ {
		sub := make([]int, 0)
		res = append(res, sub)
	}
	for x := 1; x < X; x++ {
		if win[x]+loss[x] == 0 {
			continue
		}
		if loss[x] == 0 {
			res[0] = append(res[0], x)
		}
		if loss[x] == 1 {
			res[1] = append(res[1], x)
		}
	}
	return res
}
