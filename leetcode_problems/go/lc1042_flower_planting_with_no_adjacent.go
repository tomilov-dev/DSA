package main

func gardenNoAdjDFS(adj [][]int, color, res []int, init int) {
	stack := []int{init}
	for len(stack) > 0 {
		v := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if color[v] > 0 {
			continue
		}

		color[v] = 1
		used := [5]bool{}
		for _, child := range adj[v] {
			if res[child] > 0 {
				used[res[child]] = true
			}
		}
		for c := 1; c <= 4; c++ {
			if !used[c] {
				res[v] = c
				break
			}
		}
		for i := len(adj[v]) - 1; i >= 0; i-- {
			child := adj[v][i]
			if color[child] == 0 {
				stack = append(stack, child)
			}
		}
		color[v] = 2
	}
}

func gardenNoAdj(n int, paths [][]int) []int {
	res := make([]int, n)
	if len(paths) == 0 {
		for i := range res {
			res[i] = 1
		}
		return res
	}

	adj := make([][]int, n)
	for _, path := range paths {
		u, v := path[0]-1, path[1]-1
		adj[u] = append(adj[u], v)
		adj[v] = append(adj[v], u)
	}
	color := make([]int, n)
	for v := range n {
		if color[v] > 0 {
			continue
		}
		gardenNoAdjDFS(adj, color, res, v)
	}
	return res
}
