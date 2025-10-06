package main

func semiOrderedPermutation(nums []int) int {
	fi := 0
	li := 0
	n := len(nums)
	for i, val := range nums {
		if val == 1 {
			fi = i
		} else if val == n {
			li = i
		}
	}
	if li < fi {
		return n + fi - li - 2
	} else {
		return n - li + fi - 1
	}
}
