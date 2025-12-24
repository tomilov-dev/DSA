package main

func validSubstringCount(word1 string, word2 string) int64 {
	// Решение задачи следующее:
	// 1. Создаем маппер mp - в нем храним количество символов из word2
	// 2. Создаем match - это переменная, которая отвечает за то, сколько уникальных символов нужно собрать
	// 2.1 Мы можем выполнять альтернативную проверку - по mp, проверять что всех символов <= 0, но это O(26)
	// 3. Заполняем mp символами из word2. Если встречаем новый символ (mp[c] == 0), то match++
	// 4. Проходим i, j окном по word1.
	// 4.1 Пока match != 0 - мы "опустошаем" mp[c]--
	// 4.2 Если mp[c] == 0, то match-- т.к. мы его "заполнили"
	// 5. Как только match == 0 - мы двигаем указатель i, добавляя к результату n - j
	// 5.1 Каждое передвижение i = mp[c]++
	// 5.2 Если mp[c] == 0, то match++ т.к. у нас появился новый символ к заполнению
	mp := make([]int, 26)
	match := 0
	total := int64(0)
	n := len(word1)
	for _, c := range word2 {
		cp := int(c - 'a')
		if mp[cp] == 0 {
			match++
		}
		mp[cp]++
	}
	i := 0
	for j, c := range word1 {
		cj := int(c - 'a')
		mp[cj]--
		if mp[cj] == 0 {
			match--
		}
		for match == 0 {
			total += int64(n - j)
			ci := word1[i] - 'a'
			if mp[ci] == 0 {
				match++
			}
			mp[ci]++
			i++
		}
	}
	return total
}

func validSubstringCountWithMapCheck(chars []int) bool {
	for _, fq := range chars {
		if fq > 0 {
			return false
		}
	}
	return true
}

func validSubstringCountWithMap(w1 string, w2 string) int64 {
	chars := make([]int, 26)
	for _, c := range w2 {
		chars[int(c-'a')]++
	}
	i := 0
	total := 0
	for j, c := range w1 {
		chars[int(c-'a')]--
		for validSubstringCountWithMapCheck(chars) {
			total += len(w1) - j
			chars[int(w1[i]-'a')]++
			i++
		}
	}
	return int64(total)
}
