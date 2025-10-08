package main

func distanceTraveled(mainTank int, additionalTank int) int {
	distance := 0
	for mainTank >= 5 {
		distance += 50
		if additionalTank > 0 {
			mainTank++
			additionalTank--
		}
		mainTank -= 5
	}
	return distance + mainTank*10
}
