package main

func possibleBipartition(n int, dislikes [][]int) bool {
	adj := make([][]int, n)
	// Составляем двусторонний граф dislike
	// Не важно кто кого не любит - связь будет двусторонняя
	// Важно, что эти люди не могут быть в одной компоненте
	for _, d := range dislikes {
		u := d[0] - 1
		v := d[1] - 1
		adj[u] = append(adj[u], v)
		adj[v] = append(adj[v], u)
	}

	uf := NewUnionFindInt(n)
	// Перебираем все узлы
	for u := range n {
		if len(adj[u]) == 0 {
			continue
		}

		// Объединяем всех dislike в одну компоненту
		first := adj[u][0]
		for _, v := range adj[u] {
			uf.Union(first, v)
		}

		// Проверяем, находится ли u в той же самой компоненте
		if uf.Find(u) == uf.Find(first) {
			return false
		}

	}
	return true
}
