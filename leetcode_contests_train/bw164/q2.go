package bw164

func scoreWrongSolution(cards []string, x byte) int {
	count := make(map[string]int)
	for _, card := range cards {
		if card[0] == x || card[1] == x {
			count[card]++
		}
	}
	maxwin := 0
	used := make(map[string]int)
	unique := make([]string, 0, len(count))
	for c := range count {
		unique = append(unique, c)
	}
	for i := 0; i < len(unique); i++ {
		for j := i + 1; j < len(unique); j++ {
			c1, c2 := unique[i], unique[j]
			diff := 0
			if c1[0] != c2[0] {
				diff++
			}
			if c1[1] != c2[1] {
				diff++
			}
			if diff == 1 {
				pairs := min(count[c1]-used[c1], count[c2]-used[c2])
				if pairs > 0 {
					maxwin += pairs
					used[c1] += pairs
					used[c2] += pairs
				}
			}
		}
	}
	for _, c := range unique {
		remain := count[c] - used[c]
		maxwin += remain / 2
	}
	return maxwin
}

func scoreCount(count []int, pairs, free *int) {
	sumi := 0
	maxi := 0
	for _, c := range count {
		sumi += c
		maxi = max(maxi, c)
	}
	p := min(sumi-maxi, sumi/2)
	*pairs += p
	*free += sumi - 2*p
}

func score(cards []string, x byte) int {
	wilds := 0
	countL := make([]int, 10)
	countR := make([]int, 10)
	for _, c := range cards {
		c0 := int(c[0] - 'a')
		c1 := int(c[1] - 'a')
		if c[0] == c[1] && c[0] == x {
			wilds++
		} else if c[0] == x {
			countL[c1]++
		} else if c[1] == x {
			countR[c0]++
		}
	}

	pairs := 0
	free := 0
	scoreCount(countL, &pairs, &free)
	scoreCount(countR, &pairs, &free)
	used := min(wilds, free)
	wilds -= used
	extra := min(pairs, wilds/2)
	return pairs + used + extra
}
