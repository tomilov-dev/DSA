package dp_patterns

import "testing"

type coinChangeFunc func(int, []int) int

func TestCoinChangeWaysAll(t *testing.T) {
	funcs := []struct {
		name string
		fn   coinChangeFunc
	}{
		{"Recursive", func(sum int, coins []int) int { return CoinChangeWaysRecursive(sum, coins, 0) }},
		{"TopDown", func(sum int, coins []int) int { return CoinChangeWaysTopDown(sum, coins, 0) }},
		{"BottomUp", func(sum int, coins []int) int { return CoinChangeWaysBottomUp(sum, coins, 0) }},
	}

	tests := []struct {
		sum   int
		coins []int
		want  int
	}{
		{4, []int{1, 2, 3}, 4},
		{5, []int{1, 2, 5}, 4},
		{0, []int{1, 2, 3}, 1},
		{3, []int{2}, 0},
		{10, []int{2, 5, 3, 6}, 5},
		{7, []int{2, 3, 6, 7}, 2},
	}

	for _, f := range funcs {
		for _, tt := range tests {
			got := f.fn(tt.sum, tt.coins)
			if got != tt.want {
				t.Errorf("%s(sum=%d, coins=%v) = %d; want %d", f.name, tt.sum, tt.coins, got, tt.want)
			}
		}
	}
}
