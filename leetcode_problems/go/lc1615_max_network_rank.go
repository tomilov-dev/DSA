package main

func maximalNetworkRank(n int, roads [][]int) int {
	connections := make([]int, n)
	connected := make([][]bool, n)
	for i := range connected {
		connected[i] = make([]bool, n)
	}
	for _, r := range roads {
		u := r[0]
		v := r[1]
		connections[u]++
		connections[v]++
		connected[u][v] = true
		connected[v][u] = true
	}
	maxi := 0
	for i := range n {
		for j := i + 1; j < n; j++ {
			rank := connections[i] + connections[j]
			// Чтобы не считать одну дорогу дважды - вычитаем 1
			if connected[i][j] {
				rank--
			}
			maxi = max(maxi, rank)
		}
	}
	return maxi
}
