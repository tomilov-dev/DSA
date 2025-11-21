package main

func minOperations(nums []int) int {
	total := 0
	stack := make([]int, 0)
	for _, num := range nums {
		for len(stack) > 0 && stack[len(stack)-1] > num {
			stack = stack[:len(stack)-1]
		}
		if num == 0 {
			// Это условие строго здесь - ноль не добавляем
			// Предыдущий цикл удаляется весь стек при 0
			continue
		}
		if len(stack) == 0 || stack[len(stack)-1] < num {
			total++
			stack = append(stack, num)
		}
		// Нам не нужна эта операция, но она предполагается
		// else if stack[len(stack)-1] == num {
		//	continue
		// }
	}
	return total
}
