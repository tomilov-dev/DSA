package main

func intersectQuadTree(q1, q2 *QuadTree) *QuadTree {
	if q1.IsLeaf {
		if q1.Val {
			return &QuadTree{Val: true, IsLeaf: true}
		}
		return cloneQuadTree(q2)
	}
	if q2.IsLeaf {
		if q2.Val {
			return &QuadTree{Val: true, IsLeaf: true}
		}
		return cloneQuadTree(q1)
	}

	topLeft := intersectQuadTree(q1.TopLeft, q2.TopLeft)
	topRight := intersectQuadTree(q1.TopRight, q2.TopRight)
	bottomLeft := intersectQuadTree(q1.BottomLeft, q2.BottomLeft)
	bottomRight := intersectQuadTree(q1.BottomRight, q2.BottomRight)

	if topLeft.IsLeaf &&
		topRight.IsLeaf &&
		bottomLeft.IsLeaf &&
		bottomRight.IsLeaf &&
		topLeft.Val == topRight.Val &&
		topLeft.Val == bottomLeft.Val &&
		topLeft.Val == bottomRight.Val {
		return &QuadTree{Val: topLeft.Val, IsLeaf: true}
	}

	return &QuadTree{
		Val:         false,
		IsLeaf:      false,
		TopLeft:     topLeft,
		TopRight:    topRight,
		BottomLeft:  bottomLeft,
		BottomRight: bottomRight,
	}
}

func cloneQuadTree(q *QuadTree) *QuadTree {
	if q == nil {
		return nil
	}
	return &QuadTree{
		Val:         q.Val,
		IsLeaf:      q.IsLeaf,
		TopLeft:     cloneQuadTree(q.TopLeft),
		TopRight:    cloneQuadTree(q.TopRight),
		BottomLeft:  cloneQuadTree(q.BottomLeft),
		BottomRight: cloneQuadTree(q.BottomRight),
	}
}
