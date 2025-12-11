package main

import "sort"

type RangeFreqQuery struct {
	pos map[int][]int
}

func Constructor(arr []int) RangeFreqQuery {
	pos := make(map[int][]int)
	for i, v := range arr {
		pos[v] = append(pos[v], i)
	}
	return RangeFreqQuery{pos}
}

func (this *RangeFreqQuery) Query(left int, right int, value int) int {
	indices := this.pos[value]
	if len(indices) == 0 {
		return 0
	}
	l := sort.Search(len(indices), func(i int) bool { return indices[i] >= left })
	r := sort.Search(len(indices), func(i int) bool { return indices[i] > right })
	return r - l
}
