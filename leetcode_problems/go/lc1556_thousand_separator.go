package main

func thousandSeparatorParseDigits(n int) []int {
	if n == 0 {
		return []int{0}
	}
	digits := make([]int, 0)
	for n > 0 {
		num := n % 10
		digits = append(digits, num)
		n /= 10
	}
	return digits
}

func thousandSeparator(n int) string {
	digits := thousandSeparatorParseDigits(n)
	str := make([]rune, 0)
	for i := 0; i < len(digits); i++ {
		if i > 0 && i%3 == 0 {
			str = append(str, '.')
		}
		str = append(str, rune('0'+digits[i]))
	}
	for i, j := 0, len(str)-1; i < j; i, j = i+1, j-1 {
		str[i], str[j] = str[j], str[i]
	}
	return string(str)
}
