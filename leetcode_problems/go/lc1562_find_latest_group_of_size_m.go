package main

func findLatestStep(arr []int, m int) int {
	n := len(arr)
	if m == n {
		return n
	}
	lengths := make([]int, n+2)
	count := make(map[int]int)
	res := -1

	for step, pos := range arr {
		left := lengths[pos-1]
		right := lengths[pos+1]
		total := left + right + 1

		lengths[pos-left] = total
		lengths[pos+right] = total

		count[left]--
		count[right]--
		count[total]++

		if count[m] > 0 {
			res = step + 1
		}
	}
	return res
}
