package main

func totalFruit(fruits []int) int {
	n := len(fruits)
	maxi := 0
	mp := make(map[int]int)
	i := 0
	j := 0
	for i < n && j < n {
		f := fruits[j]
		_, inBasket := mp[f]
		if len(mp) == 2 && !inBasket {
			prev := fruits[i]
			mp[prev]--
			if mp[prev] == 0 {
				delete(mp, prev)
			}
			i++
		} else {
			mp[f]++
			j++
			maxi = max(maxi, j-i)
		}
	}
	return maxi
}
