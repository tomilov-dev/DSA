package bw165

func maxXorSubsequences(nums []int) int {
	basis := make([]int, 0)
	for _, num := range nums {
		for _, b := range basis {
			num = min(num, num^b)
		}
		if num > 0 {
			basis = append(basis, num)
		}
	}
	res := 0
	for _, b := range basis {
		res = max(res, res^b)
	}
	return res
}
