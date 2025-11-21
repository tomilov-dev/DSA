package main

func minDifference(nums []int, queries [][]int) []int {
	// суть решения простая - строим матрицу n+1 для хранения count-мапов (freq)
	// размер freq по условию составляет 100 [1..100]
	// базовый случай матрица n=0 - пустой массив nums, не хранит ничего
	// далее для каждого i in [0..n] добавляем 1 в count[i+1][nums[i]]
	// таким образом мы храним частоты между всеми подмассивами нашего массива
	// мы можем найти частоту любого подмассива nums[l..r]
	// вычитая count[r+1][v] - count[l][v]; если fq >= 1 тогда число есть в подмассиве
	n := len(nums)
	const MAX = 101
	prefixFreq := make([][]int, n+1)
	for i := range prefixFreq {
		prefixFreq[i] = make([]int, MAX)
	}
	for i, num := range nums {
		for v := 1; v < MAX; v++ {
			prefixFreq[i+1][v] = prefixFreq[i][v]
		}
		prefixFreq[i+1][num]++
	}

	res := make([]int, len(queries))
	for qi, q := range queries {
		l := q[0]
		r := q[1]
		uniq := make([]int, 0)
		for v := 1; v < MAX; v++ {
			if prefixFreq[r+1][v]-prefixFreq[l][v] > 0 {
				uniq = append(uniq, v)
			}
		}
		if len(uniq) < 2 {
			res[qi] = -1
			continue
		}
		minDiff := MAX
		for i := 1; i < len(uniq); i++ {
			diff := uniq[i] - uniq[i-1]
			minDiff = min(minDiff, diff)
		}
		res[qi] = minDiff
	}
	return res
}
