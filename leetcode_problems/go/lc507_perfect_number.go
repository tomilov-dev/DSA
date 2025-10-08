package main

func checkPerfectNumber(num int) bool {
	if num == 1 {
		return false
	}
	sum := 0
	for div := 1; div < num/2+1; div++ {
		if num%div == 0 {
			sum += div
		}
	}
	return num == sum
}

func checkPerfectNumberOptimal(num int) bool {
	if num == 1 {
		return false
	}
	sum := 1
	for div := 2; div*div <= num; div++ {
		if num%div == 0 {
			sum += div
			if div != num/div {
				sum += num / div
			}
		}
	}
	return sum == num
}
