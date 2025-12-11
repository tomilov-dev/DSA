package main

func maximumLengthGroup(indices []int) []int {
	groups := make([]int, 0)
	c := 1
	for i := 1; i < len(indices); i++ {
		if indices[i]-indices[i-1] == 1 {
			c++
		} else {
			groups = append(groups, c)
			c = 1
		}
	}
	groups = append(groups, c)
	return groups
}

func canForm(groups []int, x int) bool {
	count := 0
	for _, g := range groups {
		if g >= x {
			count += g - x + 1
		}
	}
	return count >= 3
}

func maximumLengthBS(groups []int) int {
	l, r := 1, 0
	for _, g := range groups {
		r = max(r, g)
	}
	ans := -1
	for l <= r {
		m := l + (r-l)/2
		if canForm(groups, m) {
			ans = m
			l = m + 1
		} else {
			r = m - 1
		}
	}
	return ans
}

func maximumLength(s string) int {
	mp := make(map[rune][]int)
	for i, c := range s {
		if _, ok := mp[c]; !ok {
			mp[c] = make([]int, 0)
		}
		mp[c] = append(mp[c], i)
	}
	maxlen := -1
	for _, indices := range mp {
		if len(indices) < 3 {
			continue
		}
		groups := maximumLengthGroup(indices)
		maxlen = max(maxlen, maximumLengthBS(groups))
	}
	return maxlen
}
