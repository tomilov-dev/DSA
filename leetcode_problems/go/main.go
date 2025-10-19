package main

func main() {
	m := 3
	n := 2
	hc := []int{1, 3}
	vc := []int{5}
	res := minimumCostForCuttingCake(m, n, hc, vc)
	println(res)
}
