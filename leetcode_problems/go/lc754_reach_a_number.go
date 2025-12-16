package main

func reachNumber(target int) int {
	if target < 0 {
		target = -target
	}
	sum := 0
	steps := 0
	for {
		steps++
		sum += steps
		if sum >= target && (sum-target)%2 == 0 {
			return steps
		}
	}
}
