package main

import "sort"

func numMatchingSubseq(s string, words []string) int {
	// Формируем массив [буква][индексы буквы] например [a][0, 2, 5]
	pos := make([][]int, 26)
	for i, char := range s {
		j := char - 'a'
		pos[j] = append(pos[j], i)
	}

	res := 0
	for _, word := range words {
		prev := -1
		found := true
		for _, char := range word {
			char_arr := pos[char-'a']
			j := sort.Search(len(char_arr), func(i int) bool { return char_arr[i] > prev })
			if j == len(char_arr) {
				found = false
				break
			}
			prev = char_arr[j]
		}
		if found {
			res++
		}
	}
	return res
}

func numMatchingSubseqBottomUpHelper(s, word string) bool {
	m, n := len(word), len(s)
	dp := make([][]bool, m+1)
	for i := range dp {
		dp[i] = make([]bool, n+1)
	}
	for j := 0; j <= n; j++ {
		dp[0][j] = true
	}
	for i := 1; i <= m; i++ {
		for j := 1; j <= n; j++ {
			if word[i-1] == s[j-1] {
				dp[i][j] = dp[i-1][j-1] || dp[i][j-1]
			} else {
				dp[i][j] = dp[i][j-1]
			}
		}
	}
	return dp[m][n]
}

func numMatchingSubseqBottomUp(s string, words []string) int {
	res := 0
	for _, word := range words {
		if numMatchingSubseqBottomUpHelper(s, word) {
			res++
		}
	}
	return res
}

func numMatchingSubseqBucketQueue(s string, words []string) int {
	// waiting: для каждой буквы храним список слов, которые ждут эту букву как следующий символ
	waiting := make(map[rune][]string)
	waiting[' '] = words // все слова ждут "старт" (пробел)
	res := 0
	for _, c := range " " + s { // добавляем пробел в начало для инициализации
		advance := waiting[c]
		delete(waiting, c)
		for _, word := range advance {
			if len(word) == 0 {
				res++ // слово полностью обработано — это подпоследовательность
			} else {
				next := rune(word[0])
				waiting[next] = append(waiting[next], word[1:]) // кладём остаток слова в bucket для следующей буквы
			}
		}
	}
	return res
}
