package main

func main() {
	nums := []int{1, 2, 0, 0}
	k := 34
	res := addToArrayForm(nums, k)
	for _, num := range res {
		println(num)
	}
}
