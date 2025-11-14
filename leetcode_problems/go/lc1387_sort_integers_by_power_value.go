package main

import "sort"

func getKthPowerValue(x int, mem map[int]int) int {
	if x <= 1 {
		return 0
	}
	if _, solved := mem[x]; !solved {
		if x%2 == 0 {
			mem[x] = 1 + getKthPowerValue(x/2, mem)
		} else {
			mem[x] = 1 + getKthPowerValue(3*x+1, mem)
		}
	}
	return mem[x]
}

func getKth(lo int, hi int, k int) int {
	mem := make(map[int]int)
	res := make([][]int, 0)
	for x := lo; x < hi+1; x++ {
		p := getKthPowerValue(x, mem)
		res = append(res, []int{p, x})
	}
	sort.Slice(res, func(i, j int) bool {
		if res[i][0] == res[j][0] {
			return res[i][1] < res[j][1]
		}
		return res[i][0] < res[j][0]
	})
	return res[k-1][1]
}

func getKthBottomUp(lo int, hi int, k int) int {
	mem := make(map[int]int)
	for x := lo; x <= hi; x++ {
		val := x
		steps := 0
		for val != 1 {
			if v, ok := mem[val]; ok {
				steps += v
				break
			}
			if val%2 == 0 {
				val /= 2
			} else {
				val = 3*val + 1
			}
			steps++
		}
		mem[x] = steps
	}

	res := make([][]int, 0)
	for x := lo; x <= hi; x++ {
		res = append(res, []int{mem[x], x})
	}
	sort.Slice(res, func(i, j int) bool {
		if res[i][0] == res[j][0] {
			return res[i][1] < res[j][1]
		}
		return res[i][0] < res[j][0]
	})
	return res[k-1][1]
}
