package main

import "sort"

type TopVotedCandidate struct {
	times   []int
	leaders []int
}

func TopVotedCandidateConstructor(persons []int, times []int) TopVotedCandidate {
	count := make(map[int]int)
	leaders := make([]int, len(persons))

	leader := -1
	maxVotes := 0
	for i, p := range persons {
		count[p]++
		if count[p] >= maxVotes {
			leader = p
			maxVotes = count[p]
		}
		leaders[i] = leader
	}
	return TopVotedCandidate{times, leaders}

}

func (this *TopVotedCandidate) Q(t int) int {
	i := sort.Search(len(this.times), func(j int) bool { return this.times[j] > t })
	if i == 0 {
		return this.leaders[0]
	}
	return this.leaders[i-1]
}
