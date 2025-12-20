package main

func equalSubstringSlidingWindow(s string, t string, maxCost int) int {
	n := len(s)
	pref := make([]int, n+1)
	for i := 1; i <= n; i++ {
		pref[i] = pref[i-1] + abs(int(s[i-1])-int(t[i-1]))
	}
	maxi := 0
	i := 0
	j := 0
	for i <= n && j <= n {
		cost := pref[j] - pref[i]
		if cost <= maxCost {
			maxi = max(maxi, j-i)
			j++
		} else {
			i++
		}
	}
	return maxi
}

func equalSubstringBinarySearchCheck(pref []int, x, maxCost int) bool {
	for i := 0; i+x <= len(pref); i++ {
		cost := pref[i+x] - pref[i]
		if cost <= maxCost {
			return true
		}
	}
	return false
}

func equalSubstringBinarySearch(s string, t string, maxCost int) int {
	n := len(s)
	pref := make([]int, n+1)
	for i := 1; i <= n; i++ {
		pref[i] = pref[i-1] + abs(int(s[i-1])-int(t[i-1]))
	}

	l := 0
	h := n + 1
	for h-l > 1 {
		m := l + (h-l)/2
		if equalSubstringBinarySearchCheck(pref, m, maxCost) {
			l = m
		} else {
			h = m
		}
	}
	return l
}
