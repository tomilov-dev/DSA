package main

func findCommonResponse(responses [][]string) string {
	freq := make(map[string]int)
	maxi := 0
	for _, dups := range responses {
		mp := make(map[string]struct{})
		for _, resp := range dups {
			mp[resp] = struct{}{}
		}
		for resp := range mp {
			freq[resp]++
			maxi = max(maxi, freq[resp])
		}
	}
	best := ""
	for resp, fq := range freq {
		if fq != maxi {
			continue
		}
		if best == "" {
			best = resp
			continue
		}
		if best > resp {
			best = resp
		}
	}
	return best
}
