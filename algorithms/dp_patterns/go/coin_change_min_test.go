package dp_patterns

import "testing"

type coinChangeMinFunc func(int, []int) int

func TestCoinChangeMinAll(t *testing.T) {
	funcs := []struct {
		name string
		fn   coinChangeMinFunc
	}{
		{"Recursive", CoinChangeMinRecursive},
		{"TopDown", CoinChangeMinTopDown},
		{"BottomUp", CoinChangeMinBottomUp},
	}

	tests := []struct {
		sum   int
		coins []int
		want  int
	}{
		{11, []int{1, 2, 5}, 3},      // 5+5+1
		{3, []int{2}, -1},            // невозможно
		{0, []int{1, 2, 5}, 0},       // сумма 0 — 0 монет
		{7, []int{2, 3, 6, 7}, 1},    // 7
		{27, []int{2, 5, 10, 20}, 3}, // 20+5+2
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
