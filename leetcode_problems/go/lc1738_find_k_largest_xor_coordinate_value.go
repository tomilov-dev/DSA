package main

import "sort"

func kthLargestValue(matrix [][]int, k int) int {
	m, n := len(matrix), len(matrix[0])
	xor := make([][]int, m)
	for i := range xor {
		xor[i] = make([]int, n)
	}

	res := make([]int, 0)
	for i := range m {
		for j := range n {
			xor[i][j] = matrix[i][j]
			if i > 0 {
				xor[i][j] ^= xor[i-1][j]
			}
			if j > 0 {
				xor[i][j] ^= xor[i][j-1]
			}
			if i > 0 && j > 0 {
				xor[i][j] ^= xor[i-1][j-1]
			}
			res = append(res, xor[i][j])
		}
	}
	sort.Sort(sort.Reverse(sort.IntSlice(res)))
	return res[k-1]
}
