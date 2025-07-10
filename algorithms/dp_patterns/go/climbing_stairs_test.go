package dp_patterns

import "testing"

func TestClimbingStairsRecursive(t *testing.T) {
	funcs := []struct {
		name string
		fn   fibFunc
	}{
		{"Recursive", ClimbingStairsRecursive},
		{"TopDown", ClimbingStairsTopDown},
		{"BottomUp", ClimbingStairsBottomUp},
		{"BottomUpOptimized", ClimbingStairsBottomUpOptimized},
	}

	tests := []struct {
		n    int
		want int
	}{
		{0, 1},
		{1, 1},
		{2, 2},
		{3, 3},
		{4, 5},
		{5, 8},
		{6, 13},
		{7, 21},
	}

	for _, f := range funcs {
		for _, tt := range tests {
			got := f.fn(tt.n)
			if got != tt.want {
				t.Errorf("%s(%d) = %d; want %d", f.name, tt.n, got, tt.want)
			}
		}
	}
}
