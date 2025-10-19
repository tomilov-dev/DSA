package main

func canReachHelper(arr []int, i int, mem map[int]bool, visited map[int]bool) bool {
	if i < 0 || i >= len(arr) || visited[i] {
		return false
	}
	if arr[i] == 0 {
		return true
	}
	visited[i] = true
	left := canReachHelper(arr, i-arr[i], mem, visited)
	right := canReachHelper(arr, i+arr[i], mem, visited)
	return left || right
}

func canReach(arr []int, start int) bool {
	visited := make(map[int]bool, len(arr))
	return canReachHelper(arr, start, nil, visited)
}
