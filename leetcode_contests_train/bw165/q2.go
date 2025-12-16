package bw165

func minArrivalsToDiscard(arrivals []int, w int, m int) int {
	mp := make(map[int]int)
	deleted := make([]bool, len(arrivals))
	c := 0
	for i, num := range arrivals {
		if i >= w && !deleted[arrivals[i-w]] {
			mp[arrivals[i-w]]--
		}
		mp[num]++
		if mp[num] > m {
			c++
			mp[num]--
			deleted[i] = true
		}
	}
	return c
}
