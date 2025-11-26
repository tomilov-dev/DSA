package main

func findCircleNumDFS(graph [][]int, color []int, init int) {
	stack := make([]int, 0)
	stack = append(stack, init)
	for len(stack) > 0 {
		v := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if color[v] > 0 {
			continue
		}

		color[v] = 1
		for i := len(graph[v]) - 1; i >= 0; i-- {
			if graph[v][i] == 1 && color[i] == 0 {
				stack = append(stack, i)
			}
		}
		color[v] = 2
	}
}

func findCircleNum(isConnected [][]int) int {
	n := len(isConnected)
	color := make([]int, n)
	components := 0
	for v := range n {
		if color[v] == 0 {
			components++
			findCircleNumDFS(isConnected, color, v)
		}
	}
	return components
}
