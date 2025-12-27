package main

func maxBalancedShipments(weight []int) int {
	total := 0
	stk := make([]int, 0)
	for _, num := range weight {
		l := len(stk)
		if l == 0 {
			stk = append(stk, num)
			continue
		}
		if stk[l-1] > num {
			stk = stk[l:]
			total++
		} else {
			stk = append(stk, num)
		}
	}
	return total
}
