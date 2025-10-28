package main

import "sort"

func isInTaxiTimeRange(r1, r2 []int) bool {
	return r1[1] <= r2[0]
}

func maxTaxiEarningsValue(ride []int) int {
	return ride[1] - ride[0] + ride[2]
}

func maxTaxiEarningsRecursiveHelper(n int, rides [][]int, i int) int64 {
	if i >= len(rides) {
		return 0
	}

	// option 1 - take ride
	take_earn := maxTaxiEarningsValue(rides[i])
	next := len(rides)
	for j := i + 1; j < len(rides); j++ {
		if isInTaxiTimeRange(rides[i], rides[j]) {
			next = j
			break
		}
	}
	take := int64(take_earn) + maxTaxiEarningsRecursiveHelper(n, rides, next)

	// option 2 - not take ride
	not_take := maxTaxiEarningsRecursiveHelper(n, rides, i+1)
	return max(take, not_take)
}

func maxTaxiEarningsRecursive(n int, rides [][]int) int64 {
	sort.Slice(rides, func(i, j int) bool {
		if rides[i][0] == rides[j][0] {
			return rides[i][1] < rides[j][1]
		}
		return rides[i][0] < rides[j][0]
	})
	return maxTaxiEarningsRecursiveHelper(n, rides, 0)
}

func maxTaxiEarningsTopDownHelper(n int, rides [][]int, i int, mem map[int]int64) int64 {
	if i >= len(rides) {
		return 0
	}

	key := i
	if _, solved := mem[key]; !solved {
		// option 1 - take ride
		take_earn := maxTaxiEarningsValue(rides[i])
		next := len(rides)
		for j := i + 1; j < len(rides); j++ {
			if isInTaxiTimeRange(rides[i], rides[j]) {
				next = j
				break
			}
		}
		take := int64(take_earn) + maxTaxiEarningsTopDownHelper(n, rides, next, mem)

		// option 2 - not take ride
		not_take := maxTaxiEarningsTopDownHelper(n, rides, i+1, mem)
		mem[key] = max(take, not_take)
	}
	return mem[key]
}

func maxTaxiEarningsTopDown(n int, rides [][]int) int64 {
	sort.Slice(rides, func(i, j int) bool {
		if rides[i][0] == rides[j][0] {
			return rides[i][1] < rides[j][1]
		}
		return rides[i][0] < rides[j][0]
	})
	mem := make(map[int]int64)
	return maxTaxiEarningsTopDownHelper(n, rides, 0, mem)
}

func maxTaxiEarningsBottomUp(n int, rides [][]int) int64 {
	sort.Slice(rides, func(i, j int) bool {
		return rides[i][0] < rides[j][0]
	})
	dp := make([]int64, n+1)
	m := len(rides)
	j := m - 1
	for i := n - 1; i >= 0; i-- {
		dp[i] = dp[i+1]
		for j >= 0 && rides[j][0] == i {
			dp[i] = max(dp[i], dp[rides[j][1]]+int64(maxTaxiEarningsValue(rides[j])))
			j--
		}
	}
	return dp[0]
}
