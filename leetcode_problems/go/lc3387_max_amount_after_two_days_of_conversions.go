package main

type MaxAmountEdge struct {
	src, tgt string
	wgt      float64
}

func maxAmountBF(edges []MaxAmountEdge, init string, initv float64) map[string]float64 {
	// Bellman Ford shortest path
	// n = 10 по условию задачи
	n := 10
	dist := make(map[string]float64)
	dist[init] = initv
	for i := 0; i < n; i++ {
		for _, edge := range edges {
			if _, ok := dist[edge.src]; !ok {
				continue
			}
			// tgt < src + wgt по условию задачи (реверс BF)
			// базовый BF представляет условие tgt > src + wgt
			if dist[edge.tgt] < dist[edge.src]*edge.wgt {
				dist[edge.tgt] = dist[edge.src] * edge.wgt
				// Проверка i == n - 1 отсутствует в связи с условиями задачи
			}
		}
	}
	return dist
}

func maxAmount(
	initialCurrency string,
	pairs1 [][]string,
	rates1 []float64,
	pairs2 [][]string,
	rates2 []float64) float64 {
	edges1 := make([]MaxAmountEdge, 0)
	edges2 := make([]MaxAmountEdge, 0)
	for i, pair := range pairs1 {
		u := pair[0]
		v := pair[1]
		w := rates1[i]
		edges1 = append(edges1, MaxAmountEdge{u, v, w})
		edges1 = append(edges1, MaxAmountEdge{v, u, 1.0 / w})
	}
	for i, pair := range pairs2 {
		u := pair[0]
		v := pair[1]
		w := rates2[i]
		edges2 = append(edges2, MaxAmountEdge{u, v, w})
		edges2 = append(edges2, MaxAmountEdge{v, u, 1.0 / w})
	}
	dist1 := maxAmountBF(edges1, initialCurrency, 1.0)
	maxi := dist1[initialCurrency]
	for currency, amount := range dist1 {
		dist2 := maxAmountBF(edges2, currency, amount)
		maxi = max(maxi, dist2[initialCurrency])
	}
	return maxi
}
