package main

func totalNumbers(digits []int) int {
	uniq := make([]int, 10)
	for _, v := range digits {
		uniq[v] += 1
	}

	uniq_nums := make(map[int]struct{})
	nums := 0
	for v1, c1 := range uniq {
		uniq[v1]--
		for v2, c2 := range uniq {
			uniq[v2]--
			for v3, c3 := range uniq {
				if c1 == 0 || c2 == 0 || c3 == 0 {
					continue
				}
				if v1 == 0 {
					continue
				}
				if v3%2 == 1 {
					continue
				}
				num := v1*100 + v2*10 + v3
				if _, exists := uniq_nums[num]; exists {
					continue
				}
				uniq_nums[num] = struct{}{}
				nums++
			}
			uniq[v2]++
		}
		uniq[v1]++
	}

	return nums
}
