package main

import (
	"sort"
	"strings"
)

func suggestedProducts(products []string, searchWord string) [][]string {
	sort.Strings(products)
	answer := make([][]string, 0)
	for i := 1; i <= len(searchWord); i++ {
		prefix := searchWord[:i]
		left := sort.SearchStrings(products, prefix)
		suggestions := make([]string, 0)
		for j := left; j < len(products) && len(suggestions) < 3; j++ {
			if strings.HasPrefix(products[j], prefix) {
				suggestions = append(suggestions, products[j])
			} else {
				break
			}
		}
		answer = append(answer, suggestions)
	}
	return answer
}
