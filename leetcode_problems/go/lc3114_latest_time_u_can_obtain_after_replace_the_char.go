package main

func findLatestTime(s string) string {
	new := []rune(s)
	if new[0] == '?' && new[1] == '?' {
		new[0], new[1] = '1', '1'
	} else if new[0] == '?' {
		if new[1] <= '1' {
			new[0] = '1'
		} else {
			new[0] = '0'
		}
	} else if new[1] == '?' {
		if new[0] == '1' {
			new[1] = '1'
		} else {
			new[1] = '9'
		}
	}
	if new[3] == '?' {
		new[3] = '5'
	}
	if new[4] == '?' {
		new[4] = '9'
	}
	return string(new)
}
