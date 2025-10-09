package main

import "math"

func findMinimumTimeBacktrackingHelper(strength []int, k int, opened []bool, x int) int {
	mini := math.MaxInt64
	for lock_index, lock_strength := range strength {
		if opened[lock_index] {
			continue
		}
		opened[lock_index] = true
		wait := lock_strength / x
		if lock_strength%x > 0 {
			wait++
		}
		mini = min(mini, wait+findMinimumTimeBacktrackingHelper(strength, k, opened, x+k))
		opened[lock_index] = false

	}
	if mini == math.MaxInt64 {
		return 0
	}
	return mini
}

func findMinimumTimeBacktracking(strength []int, k int) int {
	n := len(strength)
	opened := make([]bool, n)
	return findMinimumTimeBacktrackingHelper(strength, k, opened, 1)
}

func findMinimumTimeBitmaskTopDownHelper(strength []int, k int, mask int, x int, mem map[[2]int]int) int {
	n := len(strength)
	if mask == (1<<n)-1 {
		return 0
	}
	key := [2]int{mask, x}
	if val, solved := mem[key]; solved {
		return val
	}
	mini := math.MaxInt64
	for i := 0; i < n; i++ {
		if mask&(1<<i) == 0 {
			wait := strength[i] / x
			if strength[i]%x > 0 {
				wait++
			}
			mini = min(mini, wait+findMinimumTimeBitmaskTopDownHelper(strength, k, mask|(1<<i), x+k, mem))
		}
	}
	mem[key] = mini
	return mini
}

func findMinimumTimeBitmaskTopDown(strength []int, k int) int {
	mask := 0
	x := 1
	mem := make(map[[2]int]int)
	return findMinimumTimeBitmaskTopDownHelper(strength, k, mask, x, mem)
}
