package main

func calcEquationDFS(graph map[string]map[string]float64, visited map[string]bool, u, v string) float64 {
	if _, ok := graph[u]; !ok {
		return -1
	}
	if u == v {
		return 1
	}
	visited[u] = true
	for nxt, val := range graph[u] {
		if visited[nxt] {
			continue
		}
		res := calcEquationDFS(graph, visited, nxt, v)
		if res != -1 {
			return res * val
		}
	}
	return -1
}

func calcEquation(equations [][]string, values []float64, queries [][]string) []float64 {
	graph := make(map[string]map[string]float64)
	for i, eq := range equations {
		u := eq[0]
		v := eq[1]
		if graph[u] == nil {
			graph[u] = make(map[string]float64)
		}
		if graph[v] == nil {
			graph[v] = make(map[string]float64)
		}
		graph[u][v] = values[i]
		graph[v][u] = 1 / values[i]
	}
	res := make([]float64, 0, len(queries))
	for _, q := range queries {
		u := q[0]
		v := q[1]
		visited := make(map[string]bool)
		r := calcEquationDFS(graph, visited, u, v)
		res = append(res, r)
	}
	return res
}
