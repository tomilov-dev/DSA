package main

import "slices"

func countSymmetricIntegersSum(nums []int) int {
	sum := 0
	for _, num := range nums {
		sum += num
	}
	return sum
}

func countSymmetricIntegersParseDigits(k int) []int {
	arr := make([]int, 0)
	for k > 0 {
		num := k % 10
		arr = append(arr, num)
		k /= 10
	}
	slices.Reverse(arr)
	return arr
}

func countSymmetricIntegers(low int, high int) int {
	res := 0
	for num := low; num <= high; num++ {
		if 0 <= num && num <= 10 {
			continue
		} else if 100 <= num && num <= 999 {
			continue
		} else if num >= 10000 {
			continue
		} else {
			digits := countSymmetricIntegersParseDigits(num)
			n := len(digits)
			if n%2 != 0 {
				continue
			}
			if countSymmetricIntegersSum(digits[:n/2]) == countSymmetricIntegersSum(digits[n/2:]) {
				res += 1
			}
		}
	}
	return res
}
