package main

func canAliceWinStoneRemoval(n int) bool {
	i := 0
	for n >= 0 {
		n -= (10 - i)
		i++
	}
	return i%2 == 0
}
