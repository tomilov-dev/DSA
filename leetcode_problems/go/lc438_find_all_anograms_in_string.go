package main

func findAnagramsIsAnogram(smap, pmap []int) bool {
	for i := range smap {
		if smap[i] != pmap[i] {
			return false
		}
	}
	return true
}

func findAnagrams(s string, p string) []int {
	res := make([]int, 0)
	plen := len(p)
	pmap := make([]int, 26)
	smap := make([]int, 26)
	for _, c := range p {
		pmap[int(c-'a')]++
	}

	for i, c := range s {
		smap[int(c-'a')]++
		if i >= plen {
			smap[int(s[i-plen]-'a')]--
		}
		if i >= plen-1 && findAnagramsIsAnogram(smap, pmap) {
			res = append(res, i-plen+1)
		}
	}
	return res
}
