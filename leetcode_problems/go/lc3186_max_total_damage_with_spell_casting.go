package main

import "sort"

func searchNextIndexAfterUse(lastIndex map[int]int, powerValue int) int {
	if index, exists := lastIndex[powerValue+2]; exists {
		return index + 1
	}
	if index, exists := lastIndex[powerValue+1]; exists {
		return index + 1
	}
	return lastIndex[powerValue] + 1
}

func maximumTotalDamageTopDownHelper(power []int, powerDamage map[int]int64, lastIndex map[int]int, i int, mem map[int]int64) int64 {
	if i >= len(power) {
		return 0
	}

	powerValue := power[i]
	if _, solved := mem[powerValue]; !solved {
		// option 1 - use power
		nextIndexAfterUse := searchNextIndexAfterUse(lastIndex, powerValue)
		use := powerDamage[powerValue] + maximumTotalDamageTopDownHelper(power, powerDamage, lastIndex, nextIndexAfterUse, mem)
		// option 2 - not use power
		not_use := maximumTotalDamageTopDownHelper(power, powerDamage, lastIndex, lastIndex[powerValue]+1, mem)
		mem[powerValue] = max(int64(use), not_use)
	}
	return mem[powerValue]
}

func maximumTotalDamageTopDown(power []int) int64 {
	sort.Ints(power)
	powerDamage := make(map[int]int64)
	lastIndex := make(map[int]int)
	for index, damage := range power {
		powerDamage[damage] += int64(damage)
		lastIndex[damage] = index
	}
	mem := make(map[int]int64)
	return maximumTotalDamageTopDownHelper(power, powerDamage, lastIndex, 0, mem)
}

func maximumTotalDamageBottomUp(power []int) int64 {
	sort.Ints(power)
	powerValues := make([]int, 0)      // последовательный массив уникальные power[i] значений
	powerDamage := make(map[int]int64) // маппер сумм для каждой power[i]
	lastIndex := make(map[int]int)     // маппер индексов, когда кончается последовательность power[i]
	for i, v := range power {
		if i == 0 || v != power[i-1] {
			powerValues = append(powerValues, v)
		}
		powerDamage[v] += int64(v)
		lastIndex[v] = i
	}
	dp := make(map[int]int64)

	n := len(powerValues)
	for i := n - 1; i >= 0; i-- {
		powerValue := powerValues[i]

		// next index after using v (skip v, v+1, v+2)
		j := i + 1
		for j < n && (powerValues[j] == powerValue+1 || powerValues[j] == powerValue+2) {
			j++
		}

		use := powerDamage[powerValue]
		if j < n {
			use += dp[j]
		}

		// next index after skipping v
		k := i + 1
		not_use := int64(0)
		if k < n {
			not_use = dp[k]
		}
		dp[i] = max(use, not_use)
	}
	return dp[0]
}
