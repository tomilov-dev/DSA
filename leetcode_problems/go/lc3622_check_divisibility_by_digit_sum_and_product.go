package main

func getDigits(n int) []int {
	digits := []int{}
	for n > 0 {
		digit := n % 10
		digits = append(digits, digit)
		n /= 10
	}
	return digits
}

func checkDivisibility(n int) bool {
	digits := getDigits(n)
	digit_sum := 0
	digit_product := 1
	for _, digit := range digits {
		digit_sum += digit
		digit_product *= digit
	}
	total := digit_sum + digit_product
	return n%total == 0
}
