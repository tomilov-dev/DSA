package main

func checkStraightLine(coordinates [][]int) bool {
	x0, y0 := coordinates[0][0], coordinates[0][1]
	x1, y1 := coordinates[1][0], coordinates[1][1]
	dx, dy := x1-x0, y1-y0
	for i := 2; i < len(coordinates); i++ {
		x, y := coordinates[i][0], coordinates[i][1]
		if (x-x0)*dy != (y-y0)*dx {
			return false
		}
	}
	return true
}
