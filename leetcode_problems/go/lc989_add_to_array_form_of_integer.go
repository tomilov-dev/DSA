package main

import "slices"

func addToArrayFormParseDigits(k int) []int {
	arr := make([]int, 0)
	for k > 0 {
		num := k % 10
		arr = append(arr, num)
		k /= 10
	}
	slices.Reverse(arr)
	return arr
}

func addToArrayForm(num []int, k int) []int {
	digits := addToArrayFormParseDigits(k)
	m := len(num)
	n := len(digits)
	r := max(m, n)
	res := make([]int, r)
	residue := 0
	for i := 0; i < r; i++ {
		j := r - i - 1
		if i < m {
			res[j] += num[m-i-1]
		}
		if i < n {
			res[j] += digits[n-i-1]
		}
		res[j] += residue
		if res[j] >= 10 {
			res[j] -= 10
			residue = 1
		} else {
			residue = 0
		}
	}
	if residue == 1 {
		res = append([]int{1}, res...)
	}
	return res
}
