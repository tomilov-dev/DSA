package main

func flipGameCheck(arr []int, x, i int, mp map[int][]int) bool {
	if _, exists := mp[x]; !exists {
		return true
	}
	indices := mp[x]
	for _, j := range indices {
		if i == j {
			continue
		}
		if arr[j] == x {
			return false
		}
	}
	return true
}

func flipgame(fronts []int, backs []int) int {
	const MAX = 1 << 20
	mp := make(map[int][]int)
	for i, num := range fronts {
		if _, exists := mp[num]; !exists {
			mp[num] = make([]int, 0)
		}
		mp[num] = append(mp[num], i)
	}

	mini := MAX
	for i := range fronts {
		if fronts[i] == backs[i] {
			continue
		}
		if flipGameCheck(backs, fronts[i], i, mp) {
			mini = min(mini, fronts[i])
		}
		if flipGameCheck(fronts, backs[i], i, mp) {
			mini = min(mini, backs[i])
		}
	}

	if mini == MAX {
		return 0
	}
	return mini
}

func flipgameOptimal(fronts []int, backs []int) int {
	// более оптимальное решение с точки зрения количества кода\
	// логика более простая:
	// мы собираем маппер с "запрещенными" значениями карт
	// это такое значение, которое есть на обоих сторонах одной и той же карты
	forbidden := make(map[int]struct{})
	for i := range fronts {
		if fronts[i] == backs[i] {
			forbidden[fronts[i]] = struct{}{}
		}
	}
	mini := 1 << 20
	for i := range fronts {
		if _, bad := forbidden[fronts[i]]; !bad {
			mini = min(mini, fronts[i])
		}
		if _, bad := forbidden[backs[i]]; !bad {
			mini = min(mini, backs[i])
		}
	}
	if mini == 1<<20 {
		return 0
	}
	return mini
}
