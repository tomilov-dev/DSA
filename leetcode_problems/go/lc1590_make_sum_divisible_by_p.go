package main

func minSubarray(nums []int, p int) int {
	n := len(nums)
	total := 0
	pref := make([]int, n+1)
	for i, num := range nums {
		pref[i+1] = pref[i] + num
		total += num
	}
	if total%p == 0 {
		return 0
	}
	mini := n
	for i := range n {
		for j := i; j < n; j++ {
			subsum := pref[j+1] - pref[i]
			xsum := total - subsum
			if xsum%p == 0 {
				mini = min(mini, j-i+1)
			}
		}
	}
	if mini == n {
		return -1
	}
	return mini
}

func minSubarrayHashMap(nums []int, p int) int {
	n := len(nums)
	total := 0
	for _, num := range nums {
		total = (total + num) % p
	}
	if total == 0 {
		return 0
	}

	res := n
	prefix := 0
	last := map[int]int{0: -1}
	for i, num := range nums {
		prefix = (prefix + num) % p
		want := (prefix - total + p) % p
		if idx, ok := last[want]; ok {
			if i-idx < res {
				res = i - idx
			}
		}
		last[prefix] = i
	}
	if res == n {
		return -1
	}
	return res
}
