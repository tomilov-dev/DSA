package dp_patterns

import "testing"

type houseRobberFunc func([]int) int

func TestHouseRobberAll(t *testing.T) {
	funcs := []struct {
		name string
		fn   houseRobberFunc
	}{
		{"Recursive", func(arr []int) int { return HouseRobberRecursive(arr, 0) }},
		{"TopDown", func(arr []int) int { return HouseRobberTopDown(arr, 0) }},
		{"BottomUp", func(arr []int) int { return HouseRobberBottomUp(arr, 0) }},
		{"BottomUp", func(arr []int) int { return HouseRobberBottomUpOptimized(arr, 0) }},
	}

	tests := []struct {
		arr  []int
		want int
	}{
		{[]int{}, 0},
		{[]int{1}, 1},
		{[]int{2, 7, 9, 3, 1}, 12},
		{[]int{2, 1, 1, 2}, 4},
		{[]int{5, 3, 4, 11, 2}, 16},
		{[]int{1, 2, 3, 1}, 4},
		{[]int{2, 1, 1, 2, 10}, 13},
	}

	for _, f := range funcs {
		for _, tt := range tests {
			got := f.fn(tt.arr)
			if got != tt.want {
				t.Errorf("%s(%v) = %d; want %d", f.name, tt.arr, got, tt.want)
			}
		}
	}
}
