package main

func minBitFlips(start int, goal int) int {
	xor := start ^ goal
	count := 0
	for xor > 0 {
		count += xor & 1 // check 1-st bit: if it's 1 then c++
		xor >>= 1        // drop 1-st bit
	}
	return count
}
