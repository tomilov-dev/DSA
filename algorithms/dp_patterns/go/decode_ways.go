package dp_patterns

import "unicode/utf8"

func toInt(s []rune) int {
	res := 0
	for _, v := range s {
		res = res*10 + int(v-'0')
	}
	return res
}

func NumDecodingsRecursiveHelper(s []rune, i int) int {
	if i >= len(s) {
		return 1
	}
	if s[i] == '0' {
		return 0
	}
	res := NumDecodingsRecursiveHelper(s, i+1)
	if i+1 < len(s) && toInt(s[i:i+2]) <= 26 {
		res += NumDecodingsRecursiveHelper(s, i+2)
	}
	return res
}

func NumDecodingsRecursive(s string) int {
	str := []rune(s)
	return NumDecodingsRecursiveHelper(str, 0)
}

func NumDecodingsTopDownHelper(s []rune, i int, mem map[int]int) int {
	if i >= len(s) {
		return 1
	}
	if s[i] == '0' {
		return 0
	}
	key := i
	if _, exists := mem[key]; !exists {
		res := NumDecodingsTopDownHelper(s, i+1, mem)
		if i+1 < len(s) && toInt(s[i:i+2]) <= 26 {
			res += NumDecodingsTopDownHelper(s, i+2, mem)
		}
		mem[key] = res
	}
	return mem[key]
}

func NumDecodingsTopDown(s string) int {
	str := []rune(s)
	mem := make(map[int]int)
	return NumDecodingsTopDownHelper(str, 0, mem)
}

func NumDecodingsBottomUp(s string) int {
	n := utf8.RuneCountInString(s)
	str := []rune(s)
	dp := make([]int, n+1)
	dp[0] = 1
	for i := 1; i <= n; i++ {
		if str[i-1] != '0' {
			dp[i] += dp[i-1]
		}
		if i >= 2 {
			two := toInt(str[i-2 : i])
			if two >= 10 && two <= 26 {
				dp[i] += dp[i-2]
			}
		}
	}
	return dp[n]
}
