package main

func canConstruct(s string, k int) bool {
	r := []rune(s)
	if len(r) < k {
		return false
	}
	mp := make(map[rune]int)
	for _, c := range r {
		mp[c]++
	}
	odd := 0
	for _, c := range mp {
		if c%2 == 1 {
			odd++
		}
	}
	return odd <= k
}
