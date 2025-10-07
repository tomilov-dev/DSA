package main

func sumCounts(nums []int) int {
	sm := 0
	n := len(nums)
	for i := 0; i < n; i++ {
		uniq := make(map[int]struct{})
		for j := i; j < n; j++ {
			uniq[nums[j]] = struct{}{}
			cnt := len(uniq)
			sm += cnt * cnt
		}
	}
	return sm
}
