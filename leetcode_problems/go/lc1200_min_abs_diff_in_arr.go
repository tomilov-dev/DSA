package main

import (
	"sort"
)

func minimumAbsDifference(arr []int) [][]int {
	sort.Ints(arr)
	min_abs := arr[1] - arr[0]
	for i := 1; i < len(arr)-1; i++ {
		diff := arr[i+1] - arr[i]
		if diff < min_abs {
			min_abs = diff
		}
	}
	res := make([][]int, 0)
	for i := 0; i < len(arr)-1; i++ {
		if arr[i+1]-arr[i] == min_abs {
			res = append(res, []int{arr[i], arr[i+1]})
		}
	}
	return res
}
