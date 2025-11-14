package main

func sortColorsCountSort(nums []int) {
	count := make([]int, 3)
	for _, v := range nums {
		count[v]++
	}
	i := 0
	for v, c := range count {
		for c > 0 {
			nums[i] = v
			i++
			c--
		}
	}
}

func sortColorsTwoPointers(nums []int) {
	red := 0
	white := 0
	blue := len(nums) - 1
	for red <= blue {
		if nums[white] == 0 {
			nums[red], nums[white] = nums[white], nums[red]
			red++
			white++
		} else if nums[white] == 1 {
			white++
		} else {
			nums[white], nums[blue] = nums[blue], nums[white]
			blue -= 1
		}
	}
}
