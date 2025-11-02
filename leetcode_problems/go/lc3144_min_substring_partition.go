package main

import (
	"fmt"
	"strings"
)

func isBalanced(freq []int) bool {
	prev := -1
	for _, f := range freq {
		if f == 0 {
			continue
		}
		if prev == -1 {
			prev = f
		}
		if prev != f {
			return false
		}
	}
	return prev != -1
}

func freqKey(freq []int) string {
	var b strings.Builder
	for _, v := range freq {
		b.WriteByte(byte(v))
	}
	return b.String()
}

func minimumSubstringsInPartitionHelper(s []rune, i int, freq []int, memo map[string]int) int {
	const MAX = 1 << 20
	if i >= len(s) {
		if isBalanced(freq) {
			return 1
		}
		return MAX
	}

	key := fmt.Sprintf("%d_%s", i, freqKey(freq))
	if _, solved := memo[key]; !solved {
		// option 1 - continue substring
		freq[s[i]-'a']++
		balanced := isBalanced(freq)
		not_part := minimumSubstringsInPartitionHelper(s, i+1, freq, memo)
		// option 2 - end substring if it is balanced
		part := MAX
		if balanced {
			emptyFreq := make([]int, 26)
			part = 1 + minimumSubstringsInPartitionHelper(s, i+1, emptyFreq, memo)
		}
		memo[key] = min(part, not_part)
	}
	return memo[key]
}

func minimumSubstringsInPartitionTopDown(s string) int {
	runes := []rune(s)
	freq := make([]int, 26)
	memo := make(map[string]int)
	return minimumSubstringsInPartitionHelper(runes, 0, freq, memo)
}

func minimumSubstringsInPartitionBottomUp(s string) int {
	n := len(s)
	const MAX = 1 << 20
	dp := make([]int, n+1)
	for i := range dp {
		dp[i] = MAX
	}
	dp[n] = 0
	for i := n - 1; i >= 0; i-- {
		freq := make([]int, 26)
		for j := i; j < n; j++ {
			freq[s[j]-'a']++
			if isBalanced(freq) {
				dp[i] = min(dp[i], dp[j+1]+1)
			}
		}
	}
	return dp[0]
}
