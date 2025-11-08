package main

import "sort"

func matchPlayersAndTrainers(players []int, trainers []int) int {
	matches := 0
	sort.Ints(players)
	sort.Ints(trainers)

	m := len(players)
	n := len(trainers)
	pi := 0
	ti := 0
	for pi < m && ti < n {
		p := players[pi]
		t := trainers[ti]
		if p <= t {
			matches++
			pi++
			ti++
		} else {
			ti++
		}
	}
	return matches
}
