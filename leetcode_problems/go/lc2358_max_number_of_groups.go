package main

func maximumGroups(grades []int) int {
	// Greedy: мы должны отсортировать grades и набирать группы, учитывая сумму + размер массивов
	// Тем не менее, если мы отсортируем grades, то каждая следующая группа
	// Будет гарантированно больше по сумме, чем предыдущая, т.к. в ней будет l+1 элемент
	// Каждый из которых не меньше, чем предыдущие
	// Таким образом, нам не нужна реальная сортировка.
	// Задача сводится к учету возможности формировать нужный размер массива
	n := len(grades)
	k := 0
	for k*(k+1)/2 <= n {
		k++
	}
	return k - 1
}

func maximumGroupsBinarySearch(grades []int) int {
	n := len(grades)
	lo, hi := 1, n
	for lo < hi {
		mid := (lo + hi + 1) / 2
		if mid*(mid+1)/2 <= n {
			lo = mid
		} else {
			hi = mid - 1
		}
	}
	return lo
}
