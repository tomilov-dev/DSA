package main

import "container/heap"

type MinTimeItem struct {
	u    int
	time int
}

type MinTimeAdj struct {
	v     int
	start int
	end   int
}

type MinTimeHeap []MinTimeItem

func (h MinTimeHeap) Len() int            { return len(h) }
func (h MinTimeHeap) Less(i, j int) bool  { return h[i].time < h[j].time }
func (h MinTimeHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *MinTimeHeap) Push(x interface{}) { *h = append(*h, x.(MinTimeItem)) }
func (h *MinTimeHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func minTime(n int, edges [][]int) int {
	adj := make([][]MinTimeAdj, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		adj[u] = append(adj[u], MinTimeAdj{v, e[2], e[3]})
	}

	h := &MinTimeHeap{MinTimeItem{0, 0}}
	heap.Init(h)
	seen := make([]bool, n)
	for h.Len() > 0 {
		cur := heap.Pop(h).(MinTimeItem)
		u, t := cur.u, cur.time
		if u == n-1 {
			return t
		}
		if seen[u] {
			continue
		}
		seen[u] = true
		for _, nxt := range adj[u] {
			if t <= nxt.end {
				nextTime := max(t, nxt.start) + 1
				heap.Push(h, MinTimeItem{nxt.v, nextTime})
			}
		}
	}
	return -1
}
