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
		for child, conn := range graph[v] {
			if conn == 1 && color[child] == 0 {
				stack = append(stack, child)
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
