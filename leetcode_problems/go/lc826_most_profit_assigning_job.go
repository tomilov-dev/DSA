package main

func maxProfitAssignmentPrefix(difficulty, profit []int) []int {
	count := make([]int, 100001)
	for i, diff := range difficulty {
		count[diff] = max(count[diff], profit[i])
	}
	for i := 1; i < len(count); i++ {
		count[i] = max(count[i], count[i-1])
	}
	return count
}

func maxProfitAssignment(difficulty []int, profit []int, worker []int) int {
	pref := maxProfitAssignmentPrefix(difficulty, profit)
	total := 0
	for _, w := range worker {
		total += pref[w]
	}
	return total
}
