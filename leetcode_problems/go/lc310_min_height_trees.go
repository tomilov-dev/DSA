package main

func findMinHeightTrees(n int, edges [][]int) []int {
	if n == 1 {
		return []int{0}
	}
	adj := make([][]int, n)
	for _, e := range edges {
		u := e[0]
		v := e[1]
		adj[u] = append(adj[u], v)
		adj[v] = append(adj[v], u)
	}
	degree := make([]int, n)
	for i := range n {
		degree[i] = len(adj[i])
	}
	leaves := make([]int, 0)
	for i := range n {
		if degree[i] == 1 {
			leaves = append(leaves, i)
		}
	}
	remaining := n
	for remaining > 2 {
		newLeaves := make([]int, 0)
		remaining -= len(leaves)
		for _, leaf := range leaves {
			for _, nei := range adj[leaf] {
				degree[nei]--
				if degree[nei] == 1 {
					newLeaves = append(newLeaves, nei)
				}
			}
		}
		leaves = newLeaves
	}
	return leaves
}
