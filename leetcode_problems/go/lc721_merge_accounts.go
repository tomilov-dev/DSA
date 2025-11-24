package main

import "sort"

func accountsMergeWithoutTransition(accounts [][]string) [][]string {
	// В этом решение не учтена возможность того, что
	// аккаунты окажутся связаны через транзитные аккаунты
	// связь выстроена напрямую
	accountsMap := make(map[string][]int)
	merged := make([]bool, len(accounts))
	res := make([][]string, 0)
	for i, account := range accounts {
		for j := 1; j < len(account); j++ {
			email := account[j]
			if _, exists := accountsMap[email]; !exists {
				accountsMap[email] = make([]int, 0)
			}
			accountsMap[email] = append(accountsMap[email], i)
		}
	}
	for i, account := range accounts {
		if merged[i] {
			continue
		}
		name := account[0]
		used := make(map[string]struct{})
		allEmails := make([]string, 0)
		for j := 1; j < len(account); j++ {
			email := account[j]
			indices := accountsMap[email]
			for _, index := range indices {
				merged[index] = true
				for k, tryEmail := range accounts[index] {
					if k == 0 {
						continue
					}
					if _, added := used[tryEmail]; added {
						continue
					}
					used[tryEmail] = struct{}{}
					allEmails = append(allEmails, tryEmail)
				}
			}
		}
		sort.Strings(allEmails)
		subres := append([]string{name}, allEmails...)
		res = append(res, subres)
	}
	return res
}

func accountsMerge(accounts [][]string) [][]string {
	// Строим граф: email -> связанные email'ы
	graph := make(map[string][]string)
	emailToName := make(map[string]string)
	for _, account := range accounts {
		name := account[0]
		for i := 1; i < len(account); i++ {
			emailToName[account[i]] = name
			if i == 1 {
				continue
			}
			// Связываем email'ы друг с другом
			graph[account[i]] = append(graph[account[i]], account[i-1])
			graph[account[i-1]] = append(graph[account[i-1]], account[i])
		}
	}

	visited := make(map[string]bool)
	res := [][]string{}
	for email := range emailToName {
		if visited[email] {
			continue
		}
		stack := []string{email}
		group := []string{}
		visited[email] = true
		for len(stack) > 0 {
			node := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			group = append(group, node)
			for _, nei := range graph[node] {
				if !visited[nei] {
					visited[nei] = true
					stack = append(stack, nei)
				}
			}
		}
		sort.Strings(group)
		res = append(res, append([]string{emailToName[email]}, group...))
	}
	return res
}
