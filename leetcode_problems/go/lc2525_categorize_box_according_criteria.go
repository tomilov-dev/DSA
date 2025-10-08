package main

import "math"

func categorizeBox(length int, width int, height int, mass int) string {
	bulky := false
	heavy := false
	volume := length * width * height
	four := int(math.Pow(10, 4))
	nine := int(math.Pow(10, 9))
	if length >= four || width >= four || height >= four || volume >= nine {
		bulky = true
	}
	if mass >= 100 {
		heavy = true
	}
	if bulky && heavy {
		return "Both"
	} else if !bulky && !heavy {
		return "Neither"
	} else if bulky && !heavy {
		return "Bulky"
	} else {
		return "Heavy"
	}
}
