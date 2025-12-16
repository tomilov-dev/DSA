package main

func canCompleteAllTrips(time []int, totalTime, totalTrips int) bool {
	trips := 0
	for _, t := range time {
		trips += totalTime / t
		if trips >= totalTrips {
			return true
		}
	}
	return false
}

func minimumTime(time []int, totalTrips int) int64 {
	l := 0
	h := totalTrips
	for _, t := range time {
		h = max(h, t*totalTrips)
	}
	for h-l > 1 {
		m := l + (h-l)/2
		if canCompleteAllTrips(time, m, totalTrips) {
			h = m
		} else {
			l = m
		}
	}
	return int64(h)
}
