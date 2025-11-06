package main

func addMinimum(word string) int {
	chars := []rune(word)
	if chars[len(chars)-1] != 'c' {
		chars = append(chars, 'a')
	}

	prev := 'c'
	total := 0
	for _, char := range chars {
		if prev == 'c' {
			println("case 1", string(char), string(prev))
			total += int(char - 'a')
			prev = char
		} else if char-prev == 1 {
			println("case 2", string(char), string(prev))
			prev = char
		} else {
			println("case 3", string(char), string(prev), abs(int(char-prev)))
			diff := int(char - prev)
			if diff > 0 {
				total += diff - 1
			} else {
				total += 2 - abs(int(char-prev))
			}
			prev = char
		}
	}
	return total
}
