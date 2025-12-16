package main

func countPairs(deliciousness []int) int {
	const MOD = 1_000_000_007
	mp := make(map[int]int)
	powers := make([]int, 0, 22)
	for p := 0; p <= 21; p++ {
		powers = append(powers, 1<<p)
	}
	count := 0
	for _, num := range deliciousness {
		for _, pow := range powers {
			if c, exists := mp[pow-num]; exists {
				count = (count + c) % MOD
			}
		}
		mp[num]++
	}
	return count
}

func lowerBound(arr []int, target int) int {
	lo, hi := 0, len(arr)
	for lo < hi {
		mid := lo + (hi-lo)/2
		if arr[mid] < target {
			lo = mid + 1
		} else {
			hi = mid
		}
	}
	return lo
}

func upperBound(arr []int, target int) int {
	lo, hi := 0, len(arr)
	for lo < hi {
		mid := lo + (hi-lo)/2
		if arr[mid] <= target {
			lo = mid + 1
		} else {
			hi = mid
		}
	}
	return lo
}

func countPairsOptimalBinarySearch(deliciousness []int) int {
	const MOD = 1_000_000_007
	mp := make(map[int]int)
	powers := make([]int, 0, 22)
	for p := 0; p <= 21; p++ {
		powers = append(powers, 1<<p)
	}
	count := 0
	maxKey := 0
	for _, num := range deliciousness {
		minSum := num
		maxSum := num + maxKey
		i := lowerBound(powers, minSum)
		j := upperBound(powers, maxSum)
		for k := i; k < j; k++ {
			if c, exists := mp[powers[k]-num]; exists {
				count = (count + c) % MOD
			}
		}
		mp[num]++
		if num > maxKey {
			maxKey = num
		}
	}
	return count
}
