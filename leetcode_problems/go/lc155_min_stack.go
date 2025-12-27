package main

type MinStack struct {
	min []int
	stk []int
}

func ConstructorMinStack() MinStack {
	return MinStack{}
}

func (s *MinStack) Push(val int) {
	l := len(s.stk)
	if l == 0 {
		s.stk = append(s.stk, val)
		s.min = append(s.min, val)
	} else {
		s.stk = append(s.stk, val)
		minv := min(s.min[l-1], val)
		s.min = append(s.min, minv)
	}
}

func (s *MinStack) Pop() {
	if len(s.stk) == 0 {
		return
	}
	l := len(s.stk)
	s.stk = s.stk[:l-1]
	s.min = s.min[:l-1]
}

func (s *MinStack) Top() int {
	if len(s.stk) == 0 {
		return 0
	}
	return s.stk[len(s.stk)-1]
}

func (s *MinStack) GetMin() int {
	if len(s.min) == 0 {
		return 0
	}
	return s.min[len(s.min)-1]
}
