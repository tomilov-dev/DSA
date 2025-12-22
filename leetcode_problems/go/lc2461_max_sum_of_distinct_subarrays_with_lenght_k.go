package main

func maximumSubarraySum2461(nums []int, k int) int64 {
	n := len(nums)
	curSum := 0
	mp := make(map[int]int)
	dups := make(map[int]bool)
	i := 0
	j := 0
	maxi := 0
	for i < n && j < n {
		a := nums[j]
		curSum += a
		mp[a]++
		if mp[a] >= 2 {
			dups[a] = true
		}
		j++
		if j-i < k {
			continue
		}

		if len(dups) == 0 {
			maxi = max(maxi, curSum)
		}

		b := nums[i]
		curSum -= b
		mp[b]--
		if _, inDups := dups[b]; inDups && mp[b] < 2 {
			delete(dups, b)
		}
		i++
	}
	return int64(maxi)
}
