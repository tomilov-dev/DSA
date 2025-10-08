package main

func isCovered(ranges [][]int, left int, right int) bool {
	for num := left; num <= right; num++ {
		covered := false
		for _, rng := range ranges {
			if rng[0] <= num && num <= rng[1] {
				covered = true
				break
			}
		}
		if !covered {
			return false
		}
	}
	return true
}
