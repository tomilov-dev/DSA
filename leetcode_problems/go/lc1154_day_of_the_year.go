package main

import (
	"strconv"
	"time"
)

func dayOfYear(date string) int {
	year, _ := strconv.Atoi(date[:4])
	month, _ := strconv.Atoi(date[5:7])
	day, _ := strconv.Atoi(date[8:])

	days := [12]int{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
	if (year%4 == 0 && year%100 != 0) || (year%400 == 0) {
		days[1] = 29
	}

	res := day
	for i := 0; i < month-1; i++ {
		res += days[i]
	}
	return res
}

func dayOfYearGoWay(date string) int {
	t, _ := time.Parse("2006-01-02", date)
	return t.YearDay()
}
