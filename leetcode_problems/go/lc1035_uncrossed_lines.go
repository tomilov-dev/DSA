package main

func maxUncrossedLinesTopDownHelper(nums1 []int, nums2 []int, i, j int, mem map[[2]int]int) int {
	if i >= len(nums1) || j >= len(nums2) {
		return 0
	}
	key := [2]int{i, j}
	if _, solved := mem[key]; !solved {
		if nums1[i] == nums2[j] {
			mem[key] = 1 + maxUncrossedLinesTopDownHelper(nums1, nums2, i+1, j+1, mem)
		} else {
			mem[key] = max(
				maxUncrossedLinesTopDownHelper(nums1, nums2, i+1, j, mem),
				maxUncrossedLinesTopDownHelper(nums1, nums2, i, j+1, mem),
			)
		}
	}
	return mem[key]
}

func maxUncrossedLinesTopDown(nums1 []int, nums2 []int) int {
	mem := make(map[[2]int]int)
	return maxUncrossedLinesTopDownHelper(nums1, nums2, 0, 0, mem)
}

func maxUncrossedLinesBottomUp(nums1, nums2 []int) int {
	n := len(nums1)
	m := len(nums2)
	dp := make([][]int, n+1)
	for i := range dp {
		dp[i] = make([]int, m+1)
	}
	for i := 1; i <= n; i++ {
		for j := 1; j <= m; j++ {
			if nums1[i-1] == nums2[j-1] {
				dp[i][j] = max(dp[i][j], 1+dp[i-1][j-1])
			} else {
				dp[i][j] = max(
					dp[i][j],
					dp[i-1][j],
					dp[i][j-1],
				)
			}
		}
	}
	return dp[n][m]
}
