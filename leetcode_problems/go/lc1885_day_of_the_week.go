package main

import "time"

func dayOfTheWeek(day int, month int, year int) string {
	days := [7]string{"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}
	if month < 3 {
		month += 12
		year -= 1
	}
	c := year / 100
	y := year % 100
	w := (c/4 - 2*c + y + y/4 + 13*(month+1)/5 + day - 1)
	w = ((w % 7) + 7) % 7
	return days[w]
}

func dayOfTheWeekGoWay(day int, month int, year int) string {
	t := time.Date(year, time.Month(month), day, 0, 0, 0, 0, time.UTC)
	return t.Weekday().String()
}
