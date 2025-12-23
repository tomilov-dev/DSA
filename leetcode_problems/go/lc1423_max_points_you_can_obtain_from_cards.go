package main

func maxScore1423(cardPoints []int, k int) int {
	n := len(cardPoints)
	curSum := 0
	for i := range k {
		curSum += cardPoints[i]
	}
	maxSum := curSum
	i := k - 1
	j := n - 1
	for k > 0 {
		curSum -= cardPoints[i]
		curSum += cardPoints[j]
		maxSum = max(maxSum, curSum)
		k--
		i--
		j--
	}
	return maxSum
}
