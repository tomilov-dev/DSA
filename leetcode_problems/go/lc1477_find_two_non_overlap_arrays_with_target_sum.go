package main

func minSumOfLengths(arr []int, target int) int {
	const MAX int = 1e9
	n := len(arr)
	minLenLeft := make([]int, n)
	for i := range minLenLeft {
		minLenLeft[i] = MAX
	}
	sumIdx := map[int]int{0: -1}
	sum := 0
	minLen := MAX
	res := MAX

	for i := range n {
		sum += arr[i]
		if idx, ok := sumIdx[sum-target]; ok {
			length := i - idx
			if idx >= 0 && minLenLeft[idx] < MAX {
				res = min(res, length+minLenLeft[idx])
			}
			minLen = min(minLen, length)
		}
		minLenLeft[i] = minLen
		sumIdx[sum] = i
	}
	if res == MAX {
		return -1
	}
	return res
}
