package main

import "math"

func maxScore3332RecursiveHelper(n int, k int, stayScore [][]int, travelScore [][]int, city int, day int) int {
	if day >= k {
		return 0
	}
	if city >= n {
		return 0
	}
	// option 1 - go to another city
	best_move := math.MinInt
	for dest := range n {
		if city == dest {
			continue
		}
		move := travelScore[city][dest] + maxScore3332RecursiveHelper(n, k, stayScore, travelScore, dest, day+1)
		best_move = max(best_move, move)
	}
	// option 2 - stay
	stay := stayScore[day][city] + maxScore3332RecursiveHelper(n, k, stayScore, travelScore, city, day+1)
	return max(best_move, stay)
}

func maxScore3332Recursive(n int, k int, stayScore [][]int, travelScore [][]int) int {
	maxi := math.MinInt
	for city := range n {
		maxi = max(maxi, maxScore3332RecursiveHelper(n, k, stayScore, travelScore, city, 0))
	}
	return maxi
}

func maxScore3332TopDownHelper(n int, k int, stayScore [][]int, travelScore [][]int, city int, day int, mem map[[2]int]int) int {
	if day >= k {
		return 0
	}
	if city >= n {
		return 0
	}
	key := [2]int{city, day}
	if _, solved := mem[key]; !solved {
		// option 1 - go to another city
		best_move := math.MinInt
		for dest := range n {
			if city == dest {
				continue
			}
			move := travelScore[city][dest] + maxScore3332TopDownHelper(n, k, stayScore, travelScore, dest, day+1, mem)
			best_move = max(best_move, move)
		}
		// option 2 - stay
		stay := stayScore[day][city] + maxScore3332TopDownHelper(n, k, stayScore, travelScore, city, day+1, mem)
		mem[key] = max(best_move, stay)
	}
	return mem[key]
}

func maxScore3332TopDown(n int, k int, stayScore [][]int, travelScore [][]int) int {
	maxi := math.MinInt
	mem := make(map[[2]int]int)
	for city := range n {
		maxi = max(maxi, maxScore3332TopDownHelper(n, k, stayScore, travelScore, city, 0, mem))
	}
	return maxi
}

func maxScore3332BottomUp(n int, k int, stayScore [][]int, travelScore [][]int) int {
	dp := make([][]int, k+1)
	for i := range dp {
		dp[i] = make([]int, n)
	}
	for day := 1; day < k+1; day++ {
		for city := range n {
			stay := stayScore[day-1][city] + dp[day-1][city]

			// city == destintation in this case
			// cityFrom == original city from which we departed
			bestMove := math.MinInt
			for cityFrom := range n {
				if city == cityFrom {
					continue
				}
				move := travelScore[cityFrom][city] + dp[day-1][cityFrom]
				bestMove = max(bestMove, move)
			}
			dp[day][city] = max(stay, bestMove)
		}
	}
	maxi := math.MinInt
	for city := range n {
		maxi = max(maxi, dp[k][city])
	}
	return maxi
}

func maxScore3332BottomUpOptimized(n int, k int, stayScore [][]int, travelScore [][]int) int {
	dpp := make([]int, n)
	dpc := make([]int, n)
	for day := 1; day <= k; day++ {
		for city := range n {
			stay := stayScore[day-1][city] + dpp[city]
			bestMove := math.MinInt
			for cityFrom := range n {
				if city == cityFrom {
					continue
				}
				move := travelScore[cityFrom][city] + dpp[cityFrom]
				bestMove = max(bestMove, move)
			}
			dpc[city] = max(stay, bestMove)
		}
		copy(dpp, dpc)
	}
	maxi := math.MinInt
	for city := range n {
		maxi = max(maxi, dpp[city])
	}
	return maxi
}
