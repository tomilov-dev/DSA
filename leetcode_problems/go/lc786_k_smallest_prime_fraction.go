package main

import "container/heap"

type Fraction struct {
	numerator   int
	denominator int
	value       float64
}

type FractionHeap []Fraction

func (h FractionHeap) Len() int           { return len(h) }
func (h FractionHeap) Less(i, j int) bool { return h[i].value < h[j].value }
func (h FractionHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *FractionHeap) Push(x interface{}) {
	*h = append(*h, x.(Fraction))
}

func (h *FractionHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func kthSmallestPrimeFractionBruteForce(arr []int, k int) []int {
	h := &FractionHeap{}
	heap.Init(h)
	n := len(arr)
	for i := range n {
		for j := i + 1; j < n; j++ {
			frac := Fraction{
				numerator:   arr[i],
				denominator: arr[j],
				value:       float64(arr[i]) / float64(arr[j]),
			}
			heap.Push(h, frac)
		}
	}

	var ans Fraction
	for i := 0; i < k; i++ {
		ans = heap.Pop(h).(Fraction)
	}
	return []int{ans.numerator, ans.denominator}
}

func kthSmallestPrimeFractionTwoPointers(arr []int, k int) []int {
	n := len(arr)
	left, right := 0.0, 1.0
	var resNum, resDen int

	for right-left > 1e-9 {
		mid := (left + right) / 2
		count := 0
		maxNum, maxDen := 0, 1
		j := 1
		for i := 0; i < n-1; i++ {
			for j < n && float64(arr[i])/float64(arr[j]) > mid {
				j++
			}
			if j == n {
				break
			}
			count += n - j
			if n-j > 0 && maxNum*arr[j] < arr[i]*maxDen {
				maxNum, maxDen = arr[i], arr[j]
			}
		}
		if count < k {
			left = mid
		} else {
			right = mid
			resNum, resDen = maxNum, maxDen
		}
	}
	return []int{resNum, resDen}
}
