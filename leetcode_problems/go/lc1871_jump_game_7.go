package main

func canReachJG7RecursiveHelper(str []rune, minJump int, maxJump int, i int) bool {
	if i == len(str)-1 {
		return true
	}
	if str[i] == '1' {
		return false
	}
	if i >= len(str) {
		return false
	}
	for j := i + minJump; j <= min(i+maxJump, len(str)-1); j++ {
		res := canReachJG7RecursiveHelper(str, minJump, maxJump, j)
		if res {
			return true
		}
	}
	return false
}

func canReachJG7Recursive(s string, minJump int, maxJump int) bool {
	str := []rune(s)
	return canReachJG7RecursiveHelper(str, minJump, maxJump, 0)
}

func canReachJG7TopDownHelper(str []rune, minJump int, maxJump int, i int, mem map[int]bool) bool {
	if i == len(str)-1 {
		return true
	}
	if str[i] == '1' {
		return false
	}
	if i >= len(str) {
		return false
	}
	key := i
	if _, solved := mem[key]; !solved {
		mem[key] = false
		for j := min(i+maxJump, len(str)-1); j >= i+minJump; j-- {
			res := canReachJG7TopDownHelper(str, minJump, maxJump, j, mem)
			if res {
				mem[key] = true
				break
			}
		}
	}
	return mem[key]
}

func canReachJG7TopDown(s string, minJump int, maxJump int) bool {
	str := []rune(s)
	mem := make(map[int]bool, 0)
	return canReachJG7TopDownHelper(str, minJump, maxJump, 0, mem)
}

func canReachJG7BottomUp(s string, minJump int, maxJump int) bool {
	n := len(s)
	dp := make([]bool, n)
	dp[0] = true
	pre := 0 // количество dp[j]==true в окне

	for i := 1; i < n; i++ {
		// Обновляем окно: добавляем левую границу, если она входит в диапазон
		if i-minJump >= 0 && dp[i-minJump] {
			pre++
		}
		// Убираем правую границу, если она выходит за maxJump
		if i-maxJump-1 >= 0 && dp[i-maxJump-1] {
			pre--
		}
		// Если есть хотя бы один true в окне и s[i]=='0', то dp[i]=true
		if pre > 0 && s[i] == '0' {
			dp[i] = true
		}
	}
	return dp[n-1]
}
