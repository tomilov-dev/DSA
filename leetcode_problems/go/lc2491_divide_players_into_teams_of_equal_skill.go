package main

func dividePlayers(skill []int) int64 {
	n := len(skill)
	if n%2 != 0 {
		return -1
	}

	// count sort - make solution O(N)
	const maxSkill = 1000
	count := make([]int, maxSkill+1)
	for _, v := range skill {
		count[v]++
	}
	sorted := make([]int, 0, n)
	for v := 1; v <= maxSkill; v++ {
		for count[v] > 0 {
			sorted = append(sorted, v)
			count[v]--
		}
	}

	// search target sum of team + pre drop if it is not int
	nTeams := n / 2
	skillSum := 0
	for _, v := range skill {
		skillSum += v
	}
	if skillSum%nTeams != 0 {
		return -1
	}

	// exec result (chemistry)
	chemistry := 0
	target := skillSum / nTeams
	p1 := 0
	p2 := n - 1
	for p1 < p2 {
		teamSkill := sorted[p1] + sorted[p2]
		if teamSkill != target {
			return -1
		}
		chemistry += sorted[p1] * sorted[p2]
		p1++
		p2--
	}
	return int64(chemistry)
}
