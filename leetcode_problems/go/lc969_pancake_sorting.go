package main

func pancakeSortReverse(arr []int, i, j int) {
	for i < j {
		arr[i], arr[j] = arr[j], arr[i]
		i++
		j--
	}
}

func pancakeSortIndexSearch(arr []int, x int) int {
	for i, v := range arr {
		if v == x {
			return i
		}
	}
	return -1
}

func pancakeSort(arr []int) []int {
	res := make([]int, 0)
	n := len(arr)
	sortValue := 1
	sortIndex := n - 1
	for sortValue < n+1 {
		curIndex := pancakeSortIndexSearch(arr, sortValue)
		if sortIndex == curIndex {

		} else if curIndex == 0 {
			res = append(res, sortIndex+1)
			pancakeSortReverse(arr, 0, sortIndex)
		} else {
			res = append(res, curIndex+1)
			pancakeSortReverse(arr, 0, curIndex)
			res = append(res, sortIndex+1)
			pancakeSortReverse(arr, 0, sortIndex)
		}
		sortValue++
		sortIndex--
	}
	res = append(res, n)
	return res
}
