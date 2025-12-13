package main

func findPoisonedDuration(timeSeries []int, duration int) int {
	if len(timeSeries) == 1 {
		return duration
	}
	c := duration
	for i := 1; i < len(timeSeries); i++ {
		t1 := timeSeries[i-1]
		t2 := timeSeries[i]
		c += min(t2-t1, duration)
	}
	return c
}
