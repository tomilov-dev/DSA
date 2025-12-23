package main

func shortestBeautifulSubstring(s string, k int) string {
	n := len(s)
	i := 0
	ones := 0
	best := ""
	for j := range n {
		if s[j] == '1' {
			ones++
		}
		if ones < k {
			continue
		}
		if ones == k {
			for i < n && s[i] == '0' {
				i++
			}
			sub := s[i : j+1]
			if best == "" || len(sub) < len(best) || len(sub) == len(best) && sub < best {
				best = sub
			}
		}
	}
	return best
}
