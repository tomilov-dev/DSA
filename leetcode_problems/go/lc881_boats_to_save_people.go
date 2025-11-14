package main

import "sort"

func numRescueBoats(people []int, limit int) int {
	sort.Ints(people)
	n := len(people)
	count := 0
	p1 := 0
	p2 := n - 1
	for p1 <= p2 {
		if people[p1]+people[p2] <= limit {
			count++
			p1++
			p2--
		} else {
			count++
			p2--
		}
	}
	return count
}
