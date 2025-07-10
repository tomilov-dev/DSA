package dp_patterns

import "testing"

type fibFunc func(int) int

func TestFibonacciAll(t *testing.T) {
	funcs := []struct {
		name string
		fn   fibFunc
	}{
		{"Recursive", FibonacciRecursive},
		{"TopDown", FibonacciTopDown},
		{"BottomUp", FibonacciBottomUp},
		{"BottomUpOptimized", FibonacciBottomUpOptimized},
	}

	tests := []struct {
		n    int
		want int
	}{
		{0, 0},
		{1, 1},
		{2, 1},
		{3, 2},
		{4, 3},
		{5, 5},
		{6, 8},
		{7, 13},
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
