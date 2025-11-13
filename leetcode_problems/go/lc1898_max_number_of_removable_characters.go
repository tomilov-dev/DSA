package main

func maximumRemovalsIsSubstring(str, sub []rune, removed []bool) bool {
	n := len(str)
	m := len(sub)
	j := 0 // index for substring
	for i := range n {
		if removed[i] {
			continue
		}
		if str[i] == sub[j] {
			j++
		}
		if j >= m {
			return true
		}
	}
	return false
}

func maximumRemovals(s string, p string, removable []int) int {
	str := []rune(s)
	sub := []rune(p)
	n := len(removable)
	removed := make([]bool, len(str))
	count := 0

	removeIndex := 0
	for removeIndex < n {
		removed[removable[removeIndex]] = true
		if maximumRemovalsIsSubstring(str, sub, removed) {
			count++
		} else {
			break
		}
		removeIndex++
	}

	return count
}

func maximumRemovalsBinarySearch(s string, p string, removable []int) int {
	str := []rune(s)
	sub := []rune(p)
	left := 0
	right := len(removable)

	res := 0
	for left <= right {
		mid := left + (right-left)/2
		removed := make([]bool, len(str))
		for i := range mid {
			removed[removable[i]] = true
		}
		if maximumRemovalsIsSubstring(str, sub, removed) {
			res = mid
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return res
}
