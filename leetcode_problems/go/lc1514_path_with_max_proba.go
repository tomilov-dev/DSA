package main

import "container/heap"

type MaxProbabilityItem struct {
	node int
	prob float64
}
type MaxProbabilityHeap []MaxProbabilityItem

func (h MaxProbabilityHeap) Len() int            { return len(h) }
func (h MaxProbabilityHeap) Less(i, j int) bool  { return h[i].prob > h[j].prob } // max-heap
func (h MaxProbabilityHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *MaxProbabilityHeap) Push(x interface{}) { *h = append(*h, x.(MaxProbabilityItem)) }
func (h *MaxProbabilityHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func maxProbability(n int, edges [][]int, succProb []float64, start_node int, end_node int) float64 {
	adj := make([][]struct {
		to   int
		prob float64
	}, n)
	for i, edge := range edges {
		u, v := edge[0], edge[1]
		p := succProb[i]
		adj[u] = append(adj[u], struct {
			to   int
			prob float64
		}{v, p})
		adj[v] = append(adj[v], struct {
			to   int
			prob float64
		}{u, p})
	}

	dist := make([]float64, n)
	dist[start_node] = 1.0
	h := &MaxProbabilityHeap{{start_node, 1.0}}
	heap.Init(h)

	for h.Len() > 0 {
		item := heap.Pop(h).(MaxProbabilityItem)
		u, curProb := item.node, item.prob
		if u == end_node {
			return curProb
		}
		if curProb < dist[u] {
			continue
		}
		for _, e := range adj[u] {
			v, p := e.to, e.prob
			newProb := curProb * p
			if newProb > dist[v] {
				dist[v] = newProb
				heap.Push(h, MaxProbabilityItem{v, newProb})
			}
		}
	}
	return 0.0
}
