package main

func minimumRefill(plants []int, capacityA int, capacityB int) int {
	p1 := 0
	p2 := len(plants) - 1
	c1 := capacityA
	c2 := capacityB
	refills := 0
	for p1 <= p2 {
		if p1 == p2 {
			maxi := max(c1, c2)
			if maxi < plants[p1] {
				refills++
			}
			break
		}

		if c1 < plants[p1] {
			c1 = capacityA
			refills++
		}
		if c2 < plants[p2] {
			c2 = capacityB
			refills++
		}
		c1 -= plants[p1]
		c2 -= plants[p2]
		p1++
		p2--
	}
	return refills
}
