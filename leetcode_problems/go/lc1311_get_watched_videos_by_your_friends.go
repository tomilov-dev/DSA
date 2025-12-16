package main

import "sort"

type VideoFreq struct {
	vid string
	fq  int
}

func watchedVideosByFriendsBFS(adj [][]int, init int) []int {
	const MAX = 1 << 32
	n := len(adj)
	color := make([]int, n)
	dist := make([]int, n)
	for i := range dist {
		dist[i] = MAX
	}
	dist[init] = 0

	q := []int{init}
	color[init] = 1
	for len(q) > 0 {
		u := q[0]
		q = q[1:]
		for _, v := range adj[u] {
			if color[v] > 0 {
				continue
			}
			color[v] = 1
			dist[v] = 1 + dist[u]
			q = append(q, v)
		}
		color[u] = 2
	}
	return dist
}

func watchedVideosByFriends(
	watchedVideos [][]string,
	friends [][]int,
	id int,
	level int) []string {

	n := len(friends)
	res := make([]string, 0)
	mp := make(map[string]int)
	dist := watchedVideosByFriendsBFS(friends, id)
	sub := make([]VideoFreq, 0)
	for friend := range n {
		if dist[friend] != level {
			// dist[id] == 0 && level >= 1 значит что всегда friend != id
			continue
		}
		for _, video := range watchedVideos[friend] {
			mp[video]++
		}
	}
	for vid, fq := range mp {
		sub = append(sub, VideoFreq{vid, fq})
	}
	sort.Slice(sub, func(i, j int) bool {
		if sub[i].fq == sub[j].fq {
			return sub[i].vid < sub[j].vid
		}
		return sub[i].fq < sub[j].fq
	})
	for i := range sub {
		res = append(res, sub[i].vid)
	}
	return res
}
