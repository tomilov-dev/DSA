package main

func main() {
	grid := [][]int{
		{3, 8, 1, 9},
		{19, 7, 2, 5},
		{4, 6, 11, 10},
		{12, 0, 21, 13},
	}
	k := 4
	res := shiftGrid(grid, k)
	println(res)
}
