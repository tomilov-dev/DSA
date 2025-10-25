package main

func isAdditiveNumberParseDigits(num string) []int {
	digits := make([]int, 0)
	for _, char := range num {
		digits = append(digits, int(char-'0'))
	}
	return digits
}

func isAdditiveNumberBT(digits []int, i int, stack []int) bool {
	n := len(digits)
	if i >= n {
		if len(stack) < 3 {
			return false
		}
		for k := 2; k < len(stack); k++ {
			if stack[k] != stack[k-1]+stack[k-2] {
				return false
			}
		}
		return true
	}
	num := 0
	for j := i; j < n; j++ {
		if j > i && digits[i] == 0 {
			break
		}
		num = num*10 + digits[j]
		stack = append(stack, num)
		if isAdditiveNumberBT(digits, j+1, stack) {
			return true
		}
		stack = stack[:len(stack)-1]
	}
	return false
}

func isAdditiveNumber(num string) bool {
	stack := make([]int, 0)
	digits := isAdditiveNumberParseDigits(num)
	return isAdditiveNumberBT(digits, 0, stack)
}
