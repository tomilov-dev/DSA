package main

import "sort"

func tileWhiteLen(tile []int) int {
	return tile[1] - tile[0] + 1
}

func maximumWhiteTilesSlidingWindow(tiles [][]int, carpetLen int) int {
	sort.Slice(tiles, func(i, j int) bool {
		return tiles[i][0] < tiles[j][0]
	})
	maxi := 0
	cover := 0
	l := 0
	n := len(tiles)
	for r := 0; maxi < carpetLen && r < n; {
		if tiles[l][0]+carpetLen > tiles[r][1] {
			cover += tileWhiteLen(tiles[r])
			maxi = max(maxi, cover)
			r++
		} else {
			partial := max(0, tiles[l][0]+carpetLen-tiles[r][0])
			maxi = max(maxi, cover+partial)
			cover -= tileWhiteLen(tiles[l])
			l++
		}
	}
	return maxi
}

func maximumWhiteTilesBinarySearch(tiles [][]int, carpetLen int) int {
	sort.Slice(tiles, func(i, j int) bool {
		return tiles[i][0] < tiles[j][0]
	})
	n := len(tiles)
	pref := make([]int, n+1)
	for i := range n {
		pref[i+1] = pref[i] + tileWhiteLen(tiles[i])
	}
	maxi := 0
	for i := range n {
		coverStart := tiles[i][0]
		coverEnd := coverStart + carpetLen - 1
		l := i
		h := n
		for h-l > 1 {
			m := l + (h-l)/2
			if tiles[m][0] <= coverEnd {
				l = m
			} else {
				h = m
			}
		}
		total := pref[l+1] - pref[i]
		if tiles[l][1] > coverEnd {
			total -= tiles[l][1] - coverEnd
		}
		maxi = max(maxi, total)
		if maxi >= carpetLen {
			return carpetLen
		}
	}
	return maxi
}
