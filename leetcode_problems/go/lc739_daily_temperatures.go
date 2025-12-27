package main

type DailyTemp struct {
	i int
	v int
}

func dailyTemperatures(temperatures []int) []int {
	stk := make([]DailyTemp, 0)
	res := make([]int, len(temperatures))
	for i, v := range temperatures {
		t := DailyTemp{i, v}
		for len(stk) > 0 {
			p := stk[len(stk)-1]
			if p.v < t.v {
				res[p.i] = t.i - p.i
				stk = stk[:len(stk)-1]
			} else {
				break
			}
		}
		stk = append(stk, t)
	}
	for len(stk) > 0 {
		p := stk[len(stk)-1]
		res[p.i] = 0
		stk = stk[:len(stk)-1]
	}
	return res
}
