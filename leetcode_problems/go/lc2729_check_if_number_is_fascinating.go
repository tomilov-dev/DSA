package main

func parseDigits(n int) []int {
	digits := make([]int, 0)
	for n > 0 {
		num := n % 10
		digits = append(digits, num)
		n /= 10
	}
	return digits
}

func isFascinating(n int) bool {
	nums := make([]int, 10)
	digits := make([]int, 0)
	digits = append(digits, parseDigits(n)...)
	digits = append(digits, parseDigits(2*n)...)
	digits = append(digits, parseDigits(3*n)...)
	for _, d := range digits {
		if d == 0 {
			return false
		}
		nums[d]++
	}
	for i := 1; i <= 9; i++ {
		if nums[i] != 1 {
			return false
		}
	}
	return true
}
