package main

import (
	"math"
	"sort"
)

func findBestValueMaxVal(arr []int) int {
	maxi := -1
	for _, x := range arr {
		maxi = max(maxi, x)
	}
	return maxi
}

func findBestValue(arr []int, target int) int {
	n := len(arr)
	sort.Ints(arr)
	pref := make([]int, n+1)
	for i := 1; i <= n; i++ {
		pref[i] = pref[i-1] + arr[i-1]
	}
	l := -1
	h := findBestValueMaxVal(arr) + 1
	res := math.MaxInt32
	resSum := math.MaxInt32
	for h-l > 1 {
		m := l + (h-l)/2
		i := sort.SearchInts(arr, m)
		left := pref[max(0, i)]
		right := m * (n - i)
		curSum := left + right
		if abs(target-resSum) == abs(target-curSum) {
			res = min(res, m)
		} else if abs(target-resSum) > abs(target-curSum) {
			res = m
			resSum = curSum
		}
		if curSum > target {
			h = m
		} else {
			l = m
		}
	}
	return res
}
