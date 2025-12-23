package main

func getSubarrayBeautySearch(count []int, x int) int {
	beauty := 0
	for skewNum, fq := range count {
		if x-fq > 0 {
			x -= fq
		} else {
			beauty = skewNum - 50
			break
		}
	}
	return min(beauty, 0)
}

func getSubarrayBeauty(nums []int, k int, x int) []int {
	res := make([]int, 0)
	count := make([]int, 101)
	i := 0
	for j, num := range nums {
		count[num+50]++
		if j-i+1 < k {
			continue
		}
		beauty := getSubarrayBeautySearch(count, x)
		res = append(res, beauty)
		count[nums[i]+50]--
		i++
	}
	return res
}
