package main

func countGoodRectangles(rectangles [][]int) int {
	maxi := 0
	for _, rec := range rectangles {
		maxi = max(maxi, min(rec[0], rec[1]))
	}
	sum := 0
	for _, rec := range rectangles {
		if min(rec[0], rec[1]) == maxi {
			sum++
		}
	}
	return sum
}
