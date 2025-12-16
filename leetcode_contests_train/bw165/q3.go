package bw165

func generateScheduleCheck(cur []int, prev []int, set map[[2]int]struct{}) bool {
	key := [2]int{cur[0], cur[1]}
	if _, exists := set[key]; exists {
		return false
	}
	if cur[0] == prev[0] || cur[0] == prev[1] {
		return false
	}
	if cur[1] == prev[0] || cur[1] == prev[1] {
		return false
	}
	return true
}

func generateSchedule(n int) [][]int {
	res := make([][]int, 0, n*(n-1))
	set := make(map[[2]int]struct{})
	for dist := 1; dist < n; dist++ {
		for i := 0; i < 2*(n+1); i++ {
			ind1 := i % n
			ind2 := (i + dist) % n
			key := [2]int{ind1, ind2}
			cur := []int{ind1, ind2}
			if len(res) == 0 {
				res = append(res, cur)
				set[key] = struct{}{}
			} else if generateScheduleCheck(cur, res[len(res)-1], set) {
				res = append(res, cur)
				set[key] = struct{}{}
			}
		}
	}
	if len(res) == n*(n-1) {
		return res
	}
	return [][]int{}
}
