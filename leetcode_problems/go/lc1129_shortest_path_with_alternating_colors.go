package main

type AltPathEdge struct {
	to int
	c  int
}

type AltPathPrev struct {
	from int
	c    int
}

func shortestAlternatingPaths(n int, redEdges [][]int, blueEdges [][]int) []int {
	const MAX = 1 << 32

	adj := make([][]AltPathEdge, n)
	for i := range adj {
		adj[i] = make([]AltPathEdge, 0)
	}
	for _, e := range redEdges {
		u := e[0]
		v := e[1]
		adj[u] = append(adj[u], AltPathEdge{v, 0})
	}
	for _, e := range blueEdges {
		u := e[0]
		v := e[1]
		adj[u] = append(adj[u], AltPathEdge{v, 1})
	}

	dist := make([][2]int, n)
	for i := range dist {
		dist[i][0], dist[i][1] = MAX, MAX
	}
	dist[0][0], dist[0][1] = 0, 0

	visited := make([][2]bool, n)
	q := []AltPathPrev{{0, 0}, {0, 1}}

	for len(q) > 0 {
		u := q[0]
		q = q[1:]
		for _, v := range adj[u.from] {
			if v.c == u.c || visited[v.to][v.c] {
				continue
			}
			visited[v.to][v.c] = true
			if v.to == 0 {
				continue
			}
			dist[v.to][v.c] = 1 + dist[u.from][u.c]
			q = append(q, AltPathPrev{v.to, v.c})
		}
	}

	res := make([]int, n)
	for i := range res {
		minDist := min(dist[i][0], dist[i][1])
		if minDist == MAX {
			res[i] = -1
		} else {
			res[i] = minDist
		}
	}
	return res
}
