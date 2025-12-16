package bw165

func smallestAbsent(nums []int) int {
	sum := 0
	set := make(map[int]struct{})
	for _, num := range nums {
		sum += num
		set[num] = struct{}{}
	}
	avg := float64(sum) / float64(len(nums))
	for x := 1; x < 101; x++ {
		if float64(x) <= avg {
			continue
		}
		if _, exists := set[x]; !exists {
			return x
		}
	}
	return 101
}
