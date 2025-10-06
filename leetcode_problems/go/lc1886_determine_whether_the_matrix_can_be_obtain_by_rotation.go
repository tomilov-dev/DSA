package main

func rotateMatrix90(matrix [][]int) [][]int {
	n := len(matrix)
	res := make([][]int, n)
	for i := range res {
		res[i] = make([]int, n)
	}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			res[j][n-1-i] = matrix[i][j]
		}
	}
	return res
}

func matrixIsEqual(mat [][]int, target [][]int) bool {
	if len(mat) != len(target) {
		return false
	}
	if len(mat[0]) != len(target[0]) {
		return false
	}
	m := len(mat)
	n := len(mat[0])
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if mat[i][j] != target[i][j] {
				return false
			}
		}
	}
	return true
}

func findRotation(mat [][]int, target [][]int) bool {
	if matrixIsEqual(mat, target) {
		return true
	}
	new_mat := rotateMatrix90(mat)
	for i := 0; i < 3; i++ {
		if matrixIsEqual(new_mat, target) {
			return true
		}
		new_mat = rotateMatrix90(new_mat)
	}
	return false
}
