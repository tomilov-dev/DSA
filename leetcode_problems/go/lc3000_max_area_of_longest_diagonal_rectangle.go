package main

import "math"

func areaOfMaxDiagonal(dimensions [][]int) int {
	max_diagonal := 0.0
	max_area := 0
	for _, dimension := range dimensions {
		lenght, width := dimension[0], dimension[1]
		diagonal := math.Sqrt(float64(lenght*lenght + width*width))
		area := lenght * width
		if diagonal == float64(max_diagonal) {
			max_area = max(max_area, area)
		} else if diagonal > float64(max_diagonal) {
			max_diagonal = diagonal
			max_area = area
		}
	}
	return max_area
}
