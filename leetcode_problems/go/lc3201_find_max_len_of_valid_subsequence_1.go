package main

func maximumLengthRecursiveHelper(nums []int, i int, j int, prevState int) int {
	if i >= len(nums) {
		return 0
	}
	if j >= len(nums) {
		return 0
	}

	take := 0
	currState := (nums[i] + nums[j]) % 2
	if prevState == -1 || currState == prevState {
		take = 1 + maximumLengthRecursiveHelper(nums, j, j+1, currState)
	}
	not_take := maximumLengthRecursiveHelper(nums, i, j+1, prevState)
	return max(take, not_take)
}

func maximumLengthRecursive(nums []int) int {
	n := len(nums)
	res := 0
	for i := range n {
		for j := i + 1; j < n; j++ {
			res = max(res, 1+maximumLengthRecursiveHelper(nums, i, j, -1))
		}
	}
	return res
}

func maximumLengthTopDownHelper(nums []int, i int, j int, prevState int, mem map[[3]int]int) int {
	if i >= len(nums) {
		return 0
	}
	if j >= len(nums) {
		return 0
	}

	key := [3]int{i, j, prevState}
	if _, solved := mem[key]; !solved {
		take := 0
		currState := (nums[i] + nums[j]) % 2
		if prevState == -1 || currState == prevState {
			take = 1 + maximumLengthTopDownHelper(nums, j, j+1, currState, mem)
		}
		not_take := maximumLengthTopDownHelper(nums, i, j+1, prevState, mem)
		mem[key] = max(take, not_take)
	}
	return mem[key]
}

func maximumLengthTopDown(nums []int) int {
	mem := make(map[[3]int]int)
	n := len(nums)
	res := 0
	for i := range n {
		for j := i + 1; j < n; j++ {
			res = max(res, 1+maximumLengthTopDownHelper(nums, i, j, -1, mem))
		}
	}
	return res
}

func maximumLengthBottomUp(nums []int) int {
	n := len(nums)
	stateIdx := func(s int) int {
		if s == -1 {
			return 0
		}
		return s + 1
	}
	dp := make([][][]int, n+1)
	for i := range dp {
		dp[i] = make([][]int, n+1)
		for j := range dp[i] {
			dp[i][j] = make([]int, 3)
		}
	}

	for i := n; i >= 0; i-- {
		for j := n; j >= 0; j-- {
			for prevState := -1; prevState <= 1; prevState++ {
				if i >= n || j >= n {
					dp[i][j][stateIdx(prevState)] = 0
					continue
				}
				take := 0
				currState := (nums[i] + nums[j]) % 2
				if prevState == -1 || currState == prevState {
					if j+1 <= n {
						take = 1 + dp[j][j+1][stateIdx(currState)]
					}
				}
				notTake := 0
				if j+1 <= n {
					notTake = dp[i][j+1][stateIdx(prevState)]
				}
				dp[i][j][stateIdx(prevState)] = max(take, notTake)
			}
		}
	}

	res := 0
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			res = max(res, 1+dp[i][j][stateIdx(-1)])
		}
	}
	return res
}

func maximumLengthBottomUpHashMap(nums []int) int {
	n := len(nums)
	dp := make(map[[3]int]int)
	for i := n - 1; i >= 0; i-- {
		for j := n - 1; j >= 0; j-- {
			for prevState := -1; prevState <= 1; prevState++ {
				if i >= n || j >= n {
					dp[[3]int{i, j, prevState}] = 0
					continue
				}
				take := 0
				currState := (nums[i] + nums[j]) % 2
				if prevState == -1 || currState == prevState {
					take = 1 + dp[[3]int{j, j + 1, currState}]
				}
				notTake := dp[[3]int{i, j + 1, prevState}]
				dp[[3]int{i, j, prevState}] = max(take, notTake)
			}
		}
	}

	res := 0
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			res = max(res, 1+dp[[3]int{i, j, -1}])
		}
	}
	return res
}

func maximumLengthBottomUpOptimized(nums []int) int {
	n := len(nums)
	dp := make([][2]int, n)
	res := 1
	for i := range n {
		for j := range i {
			state := (nums[i] + nums[j]) % 2
			dp[i][state] = max(dp[i][state], 1+dp[j][state])
			res = max(res, dp[i][state])
		}
		dp[i][0] = max(dp[i][0], 1)
		dp[i][1] = max(dp[i][1], 1)
	}
	return res
}

func maximumLengthBottomUpSuperOptimized(nums []int) int {
	k := 2
	dp := make([][]int, k)
	res := 1
	for i := range dp {
		dp[i] = make([]int, k)
	}
	for _, num := range nums {
		for state := range k {
			dp[state][num%k] = dp[num%k][state] + 1
			res = max(res, dp[state][num%k])
		}
	}
	return res
}
