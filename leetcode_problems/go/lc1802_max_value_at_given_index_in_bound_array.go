package main

func maxValueBF(n int, index int, maxSum int) int {
	l := index
	r := n - index - 1
	v := 1
	for {
		sum := v
		if v-1 >= l {
			sum += (2*v - 1 - l) * l / 2
		} else {
			sum += v * (v - 1) / 2
			sum += l - (v - 1)
		}
		if v-1 >= r {
			sum += (2*v - 1 - r) * r / 2
		} else {
			sum += v * (v - 1) / 2
			sum += r - (v - 1)
		}
		if sum > maxSum {
			return v - 1
		}
		v++
	}
}

func maxValue(n int, index int, maxSum int) int {
	l := index
	r := n - index - 1
	lo, hi := 1, maxSum
	for lo < hi {
		mid := (lo + hi + 1) / 2
		if maxValueCheck(l, r, mid, maxSum) {
			lo = mid
		} else {
			hi = mid - 1
		}
	}
	return lo
}

func maxValueCheck(l, r, v, maxSum int) bool {
	sum := v
	if v-1 >= l {
		sum += (2*v - 1 - l) * l / 2
	} else {
		sum += v * (v - 1) / 2
		sum += l - (v - 1)
	}
	if v-1 >= r {
		sum += (2*v - 1 - r) * r / 2
	} else {
		sum += v * (v - 1) / 2
		sum += r - (v - 1)
	}
	return sum <= maxSum
}
