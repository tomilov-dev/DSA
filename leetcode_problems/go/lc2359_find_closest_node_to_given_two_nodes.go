package main

import "math"

func closestMeetingNodeDFS(edges []int, x, dist int, mem []int) {
	for x != -1 && mem[x] == -1 {
		dist++
		mem[x] = dist
		x = edges[x]
	}
}

func closestMeetingNode(edges []int, node1 int, node2 int) int {
	n := len(edges)
	m1 := make([]int, n)
	m2 := make([]int, n)
	for i := range m1 {
		m1[i] = -1
		m2[i] = -1
	}
	res := -1
	mini := math.MaxInt
	closestMeetingNodeDFS(edges, node1, 0, m1)
	closestMeetingNodeDFS(edges, node2, 0, m2)
	for x := range n {
		if m1[x] == -1 || m2[x] == -1 {
			continue
		}
		if max(m1[x], m2[x]) < mini {
			mini = max(m1[x], m2[x])
			res = x
		}
	}
	return res
}
