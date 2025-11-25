package main

func canConvertString(s string, t string, k int) bool {
	sr := []rune(s)
	tr := []rune(t)
	if len(sr) != len(tr) {
		return false
	}

	available := make([]int, 27)
	for i := 1; i < 27; i++ {
		available[i] = k / 26
		if k%26 >= i {
			available[i]++
		}
	}

	for i, c := range sr {
		shift := (int(tr[i]) - int(c) + 26) % 26
		if shift == 0 {
			continue
		}
		available[shift]--
		if available[shift] < 0 {
			return false
		}
	}
	return true
}
