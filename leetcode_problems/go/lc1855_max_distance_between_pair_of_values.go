package main

func maxDistance(nums1 []int, nums2 []int) int {
	n := len(nums1)
	m := len(nums2)
	i := 0
	j := 0
	maxi := 0
	for i < n && j < m {
		if nums1[i] > nums2[j] {
			i++
		} else {
			maxi = max(maxi, j-i)
			j++
		}
	}
	return maxi
}
