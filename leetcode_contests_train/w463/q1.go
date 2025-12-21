package main

func maxProfit(prices []int, strategy []int, k int) int64 {
	n := len(prices)
	pref := make([]int, n+1)
	sell := make([]int, n+1)
	for i := range n {
		pref[i+1] = pref[i] + prices[i]*strategy[i]
		sell[i+1] = sell[i] + prices[i]
	}
	q := k / 2
	maxi := pref[n]
	for i := 0; i <= n-k; i++ {
		old := pref[i+k] - pref[i]
		newSum := sell[i+k] - sell[i+q]
		maxi = max(maxi, pref[n]-old+newSum)
	}
	return int64(maxi)
}
