package main

func minMaxWeightDFS(i, m int, revGraph [][]struct{ to, w int }, vis []bool) int {
	// Проверяем, сколько узлов достижимо из i (изначально 0)
	// Ограничение - вес ребра, по которому достижим узел
	// Если вес g.w > m - мы не рассматриваем такое ребро как путь (откидываем)
	res := 1
	vis[i] = true
	for _, g := range revGraph[i] {
		if g.w <= m && !vis[g.to] {
			res += minMaxWeightDFS(g.to, m, revGraph, vis)
		}
	}
	return res
}

func minMaxWeight(n int, edges [][]int, threshold int) int {
	const MAX = 1000001
	// Строим обратный граф - список обратных ребер
	revGraph := make([][]struct{ to, w int }, n)
	for _, e := range edges {
		u := e[0]
		v := e[1]
		w := e[2]
		revGraph[v] = append(revGraph[v], struct {
			to int
			w  int
		}{u, w})
	}
	// Проводим бинарный поиск результата mid - мин. вес ребра
	// Проверка - достижимы ли ВСЕ узлы из 0 по ребрам, вес которых w <= mid
	low := 1
	high := MAX
	for low < high {
		mid := low + (high-low)/2
		vis := make([]bool, n)
		if minMaxWeightDFS(0, mid, revGraph, vis) == n {
			// Если достижимы все узлы из 0, снижаем верхний порог
			high = mid
		} else {
			// Если не достижимы все узлы, повышаем нижний порог
			low = mid + 1
		}
	}
	if low == MAX {
		return -1
	}
	return low
}
