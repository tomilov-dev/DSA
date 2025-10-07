package main

func hasAlternatingBits(n int) bool {
	b := 0
	for b < 33 {
		if (1 << b) < n {
			b += 1
		} else {
			break
		}
	}
	b -= 1
	prev := -1
	for b >= 0 {
		if (n & (1 << b)) != 0 {
			if prev == 1 {
				return false
			}
			prev = 1
		} else {
			if prev == 0 {
				return false
			}
			prev = 0
		}
		b -= 1
	}
	return true
}

func hasAlternatingBitsBestSolution(n int) bool {
	x := n ^ (n >> 1)
	return x&(x+1) == 0
}
