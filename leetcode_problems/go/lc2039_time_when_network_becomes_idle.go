package main

func networkBecomesIdleBFS(adj [][]int, init int) []int {
	dist := make([]int, len(adj))
	for i := range dist {
		dist[i] = -1
	}

	q := []int{init}
	dist[init] = 0
	for len(q) > 0 {
		u := q[0]
		q = q[1:]
		for _, v := range adj[u] {
			if dist[v] == -1 {
				dist[v] = dist[u] + 1
				q = append(q, v)
			}
		}
	}
	return dist
}

func networkBecomesIdle(edges [][]int, patience []int) int {
	n := len(patience)
	adj := make([][]int, n)
	// Создаем adj list
	for _, e := range edges {
		u, v := e[0], e[1]
		adj[u] = append(adj[u], v)
		adj[v] = append(adj[v], u)
	}
	// Определяем расстояние от 0 до всех узлов через базовый BFS
	dist := networkBecomesIdleBFS(adj, 0)

	res := 0
	// Перебираем все узлы и считаем их путь до 0
	for i := 1; i < n; i++ {
		roundTrip := 2 * dist[i]
		if patience[i] >= roundTrip {
			// Если patience[i] больше или равен пути, тогда будет 1 отправка сообщения
			res = max(res, roundTrip)
			continue
		}
		// Если же patience[i] меньше пути, тогда будет несколько отправок
		// Вычисляем последнее время отправки
		lastSend := ((roundTrip - 1) / patience[i]) * patience[i]
		arrival := lastSend + roundTrip
		res = max(res, arrival)
	}
	return res + 1
}
