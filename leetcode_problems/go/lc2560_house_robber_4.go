package main

import (
	"math"
	"math/bits"
)

func minCapabilityRecursiveHelper(nums []int, k int, i int, mask int) int {
	if i >= len(nums) {
		ones := bits.OnesCount(uint(mask))
		if ones < k {
			return math.MaxInt64
		}
		maxi := 0
		for i := range nums {
			if mask&(1<<i) != 0 {
				maxi = max(maxi, nums[i])
			}
		}
		return maxi
	}
	// option 1 - take
	take := minCapabilityRecursiveHelper(nums, k, i+2, mask|1<<i)
	// option 2 - not take
	not_take := minCapabilityRecursiveHelper(nums, k, i+1, mask)
	return min(take, not_take)
}

func minCapabilityRecursive(nums []int, k int) int {
	return minCapabilityRecursiveHelper(nums, k, 0, 0)
}

func minCapabilityTopDownHelper(nums []int, k int, i int, mask int, mem map[[2]int]int) int {
	if i >= len(nums) {
		ones := bits.OnesCount(uint(mask))
		if ones < k {
			return math.MaxInt64
		}
		maxi := 0
		for i := range nums {
			if mask&(1<<i) != 0 {
				maxi = max(maxi, nums[i])
			}
		}
		return maxi
	}
	key := [2]int{i, mask}
	if _, solved := mem[key]; !solved {
		// option 1 - take
		take := minCapabilityTopDownHelper(nums, k, i+2, mask|1<<i, mem)
		// option 2 - not take
		not_take := minCapabilityTopDownHelper(nums, k, i+1, mask, mem)
		mem[key] = min(take, not_take)
	}
	return mem[key]
}

func minCapabilityTopDown(nums []int, k int) int {
	mem := make(map[[2]int]int, 0)
	return minCapabilityTopDownHelper(nums, k, 0, 0, mem)
}

func minCapabilityBottomUpMask(nums []int, k int) int {
	n := len(nums)
	size := 1 << n
	dp := make([]int, size)
	for mask := range size {
		dp[mask] = math.MaxInt
	}
	dp[0] = 0

	for mask := range size {
		ones := bits.OnesCount(uint(mask))
		if ones > k {
			continue
		}
		for i := range n {
			if mask&(1<<i) == 0 {
				if (i > 0 && mask&(1<<(i-1)) != 0) || (i < n-1 && mask&(1<<(i+1)) != 0) {
					continue
				}
				newMask := mask | (1 << i)
				dp[newMask] = min(dp[newMask], max(dp[mask], nums[i]))
			}
		}
	}

	ans := math.MaxInt
	for mask := range size {
		if bits.OnesCount(uint(mask)) >= k {
			ans = min(ans, dp[mask])
		}
	}
	return ans
}

func canRobHelper(nums []int, k int, cap int) bool {
	count := 0
	i := 0
	for i < len(nums) {
		if nums[i] <= cap {
			count++
			i += 2
		} else {
			i++
		}
	}
	return count >= k
}

func minCapabilityBinarySearch(nums []int, k int) int {
	left, right := 0, 0
	for _, v := range nums {
		if v > right {
			right = v
		}
	}
	ans := right
	for left <= right {
		mid := (left + right) / 2
		if canRobHelper(nums, k, mid) {
			ans = mid
			right = mid - 1
		} else {
			left = mid + 1
		}
	}
	return ans
}
