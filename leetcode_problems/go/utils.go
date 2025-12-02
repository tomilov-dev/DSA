package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type QuadTree struct {
	Val         bool
	IsLeaf      bool
	TopLeft     *QuadTree
	TopRight    *QuadTree
	BottomLeft  *QuadTree
	BottomRight *QuadTree
}

type ListNode struct {
	Val  int
	Next *ListNode
}
type UnionFindInt struct {
	parent []int
	rank   []int
}

func NewUnionFindInt(n int) *UnionFindInt {
	uf := &UnionFindInt{
		parent: make([]int, n),
		rank:   make([]int, n),
	}
	for i := range uf.parent {
		uf.parent[i] = i
	}
	return uf
}

func (uf *UnionFindInt) Find(x int) int {
	if uf.parent[x] != x {
		uf.parent[x] = uf.Find(uf.parent[x])
	}
	return uf.parent[x]
}

func (uf *UnionFindInt) Union(x, y int) {
	rx, ry := uf.Find(x), uf.Find(y)
	if rx == ry {
		return
	}
	if uf.rank[rx] < uf.rank[ry] {
		uf.parent[rx] = ry
	} else if uf.rank[rx] > uf.rank[ry] {
		uf.parent[ry] = rx
	} else {
		uf.parent[ry] = rx
		uf.rank[rx]++
	}
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

const MOD = 1_000_000_007
