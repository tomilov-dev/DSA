package dp_patterns

import "testing"

type jumpFunc func([]int) int

func TestJumpGame2All(t *testing.T) {
	funcs := []struct {
		name string
		fn   jumpFunc
	}{
		{"Recursive", func(nums []int) int { return JumpRecursive(nums, 0) }},
		{"TopDown", func(nums []int) int { return JumpTopDown(nums, 0) }},
		{"BottomUp", JumpBottomUp},
	}

	tests := []struct {
		nums []int
		want int
	}{
		{[]int{2, 3, 1, 1, 4}, 2}, // 0->1->4
		{[]int{1, 1, 1, 1}, 3},    // 0->1->2->3
		{[]int{1, 2, 1, 1, 1}, 3}, // 0->1->2->4
		{[]int{0}, 0},             // уже на финише
		{[]int{1, 2}, 1},          // 0->1
		{[]int{2, 1}, 1},          // 0->1
	}

	for _, f := range funcs {
		for _, tt := range tests {
			got := f.fn(tt.nums)
			if got != tt.want {
				t.Errorf("%s(%v) = %d; want %d", f.name, tt.nums, got, tt.want)
			}
		}
	}
}
