package main

func mostCompetitive(nums []int, k int) []int {
	n := len(nums)
	stk := make([]int, 0)
	for i, num := range nums {
		if len(stk) == 0 {
			stk = append(stk, num)
			continue
		}
		residue := n - i - 1
		for len(stk) > 0 && len(stk)+residue >= k && num < stk[len(stk)-1] {
			stk = stk[:len(stk)-1]
		}
		if len(stk) < k {
			stk = append(stk, num)
		}
	}
	return stk
}
