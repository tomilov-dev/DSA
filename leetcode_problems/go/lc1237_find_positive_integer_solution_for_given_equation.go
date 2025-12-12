package main

func findSolution(customFunction func(int, int) int, z int) [][]int {
	res := make([][]int, 0)
	x := 1
	y := 1000
	for x <= 1000 && y >= 1 {
		v := customFunction(x, y)
		if v == z {
			res = append(res, []int{x, y})
			x++
			y--
		} else if v < z {
			x++
		} else {
			y--
		}
	}
	return res
}
