package main

type StockSpan struct {
	val  int
	span int
}

type StockSpanner struct {
	stack []StockSpan
}

func ConstructorStockSpanner() StockSpanner {
	return StockSpanner{}
}

func (s *StockSpanner) Next(price int) int {
	cur := StockSpan{price, 1}
	for len(s.stack) > 0 && s.stack[len(s.stack)-1].val <= cur.val {
		cur.span += s.stack[len(s.stack)-1].span
		s.stack = s.stack[:len(s.stack)-1]
	}
	s.stack = append(s.stack, cur)
	return cur.span
}
