package main

func missingIntegerWrong(nums []int) int {
	cur_prefix_sum := nums[0]
	cur_prefix_len := 1
	max_prefix_sum := nums[0]
	max_prefix_len := 1
	mem := make(map[int]struct{})
	mem[nums[0]] = struct{}{}
	for i := 1; i < len(nums); i++ {
		mem[nums[i]] = struct{}{}
		if nums[i]-nums[i-1] == 1 {
			cur_prefix_sum += nums[i]
			cur_prefix_len += 1
		} else {
			cur_prefix_sum = nums[i]
			cur_prefix_len = 1
		}
		if cur_prefix_len == max_prefix_len {
			max_prefix_sum = max(max_prefix_sum, cur_prefix_sum)
		}
		if cur_prefix_len > max_prefix_len {
			max_prefix_len = cur_prefix_len
			max_prefix_sum = cur_prefix_sum
		}
	}
	for x := max_prefix_sum; x <= 51; x++ {
		if _, exists := mem[x]; !exists {
			return x
		}
	}
	return max_prefix_sum
}

func missingInteger(nums []int) int {
	prefix_sum := nums[0]
	prefix_len := 1
	for i := 1; i < len(nums); i++ {
		if nums[i] == nums[i-1]+1 {
			prefix_sum += nums[i]
			prefix_len += 1
		} else {
			break
		}
	}
	mem := make(map[int]struct{})
	for _, v := range nums {
		mem[v] = struct{}{}
	}
	for x := prefix_sum; x <= 51; x++ {
		if _, exists := mem[x]; !exists {
			return x
		}
	}
	return prefix_sum
}
