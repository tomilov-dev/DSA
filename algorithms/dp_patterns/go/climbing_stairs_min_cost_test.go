package dp_patterns

import "testing"

type minCostClimbingStairsFunc func([]int) int

func TestMinCostClimbingStairsAll(t *testing.T) {
	funcs := []struct {
		name string
		fn   minCostClimbingStairsFunc
	}{
		{"Recursive", MinCostClimbingStairsRecursive},
		{"TopDown", MinCostClimbingStairsTopDown},
		{"BottomUp", MinCostClimbingStairsBottomUp},
		{"BottomUpOptimized", MinCostClimbingStairsBottomUpOptimized},
	}

	tests := []struct {
		cost []int
		want int
	}{
		{[]int{10, 15, 20}, 15},
		{[]int{1, 100, 1, 1, 1, 100, 1, 1, 100, 1}, 6},
		{[]int{0, 0, 0, 0}, 0},
		{[]int{1, 2}, 1},
		{[]int{5, 10}, 5},
		{[]int{1, 100, 2, 3, 4}, 6},
		{[]int{0, 2, 2, 1}, 2},
	}

	for _, f := range funcs {
		for _, tt := range tests {
			got := f.fn(tt.cost)
			if got != tt.want {
				t.Errorf("%s(%v) = %d; want %d", f.name, tt.cost, got, tt.want)
			}
		}
	}
}
