package bw164

func getLeastFrequentDigitDigits(n int) []int {
	digits := make([]int, 0)
	for n > 0 {
		digits = append(digits, n%10)
		n /= 10
	}
	return digits
}

func getLeastFrequentDigit(n int) int {
	digits := getLeastFrequentDigitDigits(n)
	mp := make(map[int]int)
	for _, d := range digits {
		mp[d]++
	}
	minfq := 1 << 33
	mind := -1
	for d, fq := range mp {
		if fq < minfq || (fq == minfq && d < mind) {
			minfq = fq
			mind = d
		}
	}
	return mind
}
