package main

func validateStackSequences(pushed []int, popped []int) bool {
	if len(pushed) != len(popped) {
		return false
	}
	stk := make([]int, 0)
	push := 0
	pop := 0
	for push < len(pushed) {
		l := len(stk)
		if l == 0 {
			stk = append(stk, pushed[push])
			push++
		} else if pop < len(popped) && stk[l-1] == popped[pop] {
			stk = stk[:l-1]
			pop++
		} else {
			stk = append(stk, pushed[push])
			push++
		}
	}
	for pop < len(popped) && len(stk) > 0 && stk[len(stk)-1] == popped[pop] {
		stk = stk[:len(stk)-1]
		pop++
	}
	return push >= len(pushed) && pop >= len(popped)
}
