package main

func majorityElement(nums []int) []int {
	n := len(nums)
	res := make([]int, 0)
	mp := make(map[int]int)
	for _, num := range nums {
		mp[num]++
	}
	for num, fq := range mp {
		if fq > n/3 {
			res = append(res, num)
		}
	}
	return res
}

func majorityElementBoyerMooreVoting(nums []int) []int {
	n := len(nums)
	var cand1, cand2, cnt1, cnt2 int
	for _, num := range nums {
		switch {
		case cnt1 > 0 && num == cand1:
			cnt1++
		case cnt2 > 0 && num == cand2:
			cnt2++
		case cnt1 == 0:
			cand1, cnt1 = num, 1
		case cnt2 == 0:
			cand2, cnt2 = num, 1
		default:
			cnt1--
			cnt2--
		}
	}
	cnt1, cnt2 = 0, 0
	for _, num := range nums {
		if num == cand1 {
			cnt1++
		} else if num == cand2 {
			cnt2++
		}
	}
	res := []int{}
	if cnt1 > n/3 {
		res = append(res, cand1)
	}
	if cnt2 > n/3 {
		res = append(res, cand2)
	}
	return res
}
