package main

func numberOfAlternatingGroups(colors []int, k int) int {
	n := len(colors)
	total := 0
	i := 0
	j := 0
	for i < n {
		if j-i+1 == k {
			total++
			i++
		} else if colors[j%n] != colors[(j+1)%n] {
			j++
		} else {
			i = j + 1
			j = i
		}
	}
	return total
}
