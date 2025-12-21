package main

func xorAfterQueries(nums []int, queries [][]int) int {
	for _, q := range queries {
		l := q[0]
		r := q[1]
		k := q[2]
		v := q[3]
		for i := l; i <= r; i += k {
			nums[i] = (nums[i] * v) % (1_000_000_000 + 7)
		}
	}
	xor := nums[0]
	for i := 1; i < len(nums); i++ {
		xor ^= nums[i]
	}
	return xor
}
