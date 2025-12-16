package main

import "sort"

func maxProfit(inventory []int, orders int) int {
	const mod = 1_000_000_007
	sort.Ints(inventory)
	n := len(inventory)
	total := 0
	k := 1
	i := n - 1
	for orders > 0 {
		for i > 0 && inventory[i] == inventory[i-1] {
			k++
			i--
		}
		nextPrice := 0
		if i > 0 {
			nextPrice = inventory[i-1]
		}
		count := (inventory[i] - nextPrice) * k
		if orders >= count {
			total = (total + k*sumRange(nextPrice+1, inventory[i])) % mod
			orders -= count
		} else {
			full, rem := orders/k, orders%k
			total = (total + k*sumRange(inventory[i]-full+1, inventory[i])) % mod
			total = (total + rem*(inventory[i]-full)) % mod
			break
		}
		i--
		k++
	}
	return total
}

func sumRange(l, r int) int {
	return (r - l + 1) * (l + r) / 2
}
