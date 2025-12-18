package main

func findClosestElementsBS(arr []int, x int) (int, int) {
	l := 0
	h := len(arr)
	for h-l > 1 {
		m := l + (h-l)/2
		if arr[m] < x {
			l = m
		} else {
			h = m
		}
	}
	return l, h
}

func findClosestElements(arr []int, k int, x int) []int {
	n := len(arr)
	p1, p2 := findClosestElementsBS(arr, x)
	for k > 0 {
		if p1 < 0 {
			p2++
		} else if p2 >= n {
			p1--
		} else if abs(arr[p1]-x) == abs(arr[p2]-x) && arr[p1] < arr[p2] {
			p1--
		} else if abs(arr[p1]-x) == abs(arr[p2]-x) && arr[p1] > arr[p2] {
			p2++
		} else if abs(arr[p1]-x) < abs(arr[p2]-x) {
			p1--
		} else {
			p2++
		}
		k--
	}
	return arr[p1+1 : p2]
}
