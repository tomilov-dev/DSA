package main

func maximumPopulation(logs [][]int) int {
	years := make([]int, 2051)
	maxi := 0
	for _, log := range logs {
		start := log[0]
		end := log[1]
		for i := start; i < end; i++ {
			years[i]++
			maxi = max(maxi, years[i])
		}
	}
	for year, count := range years {
		if count == maxi {
			return year
		}
	}
	return logs[0][0]
}

func maximumPopulationOptimal(logs [][]int) int {
	years := make([]int, 2051)
	for _, log := range logs {
		years[log[0]]++
		years[log[1]]--
	}
	maxPop := 0
	curPop := 0
	resYear := 0
	for year := 1950; year < 2051; year++ {
		curPop += years[year]
		if curPop > maxPop {
			maxPop = curPop
			resYear = year
		}
	}
	return resYear
}
