package main

import "strings"

func simplifyPath(path string) string {
	stk := make([]string, 0)
	ws := -1
	for i, c := range path + "/" {
		if c == '/' {
			if ws == -1 {
				continue
			}
			w := path[ws:i]
			if w == "." {
				ws = -1
			} else if w == ".." {
				if len(stk) > 0 {
					stk = stk[:len(stk)-1]
				}
				ws = -1
			} else {
				stk = append(stk, w)
				ws = -1
			}
		} else if ws == -1 {
			ws = i
		} else {
			continue
		}
	}
	return "/" + strings.Join(stk, "/")
}

func simplifyPathWithSTD(path string) string {
	parts := strings.Split(path, "/")
	stk := make([]string, 0)
	for _, part := range parts {
		if part == "" || part == "." {
			continue
		}
		if part == ".." {
			if len(stk) > 0 {
				stk = stk[:len(stk)-1]
			}
		} else {
			stk = append(stk, part)
		}
	}
	return "/" + strings.Join(stk, "/")
}
