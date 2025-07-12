package dp_patterns

import "testing"

type numDecodingsFunc func(string) int

func TestNumDecodingsAll(t *testing.T) {
	funcs := []struct {
		name string
		fn   numDecodingsFunc
	}{
		{"Recursive", NumDecodingsRecursive},
		{"TopDown", NumDecodingsTopDown},
		{"BottomUp", NumDecodingsBottomUp},
	}

	tests := []struct {
		input string
		want  int
	}{
		{"12", 2},    // "AB", "L"
		{"226", 3},   // "BBF", "BZ", "VF"
		{"0", 0},     // нельзя декодировать
		{"06", 0},    // нельзя декодировать
		{"10", 1},    // "J"
		{"27", 1},    // "BG"
		{"11106", 2}, // "AAJF", "KJF"
		{"", 1},      // пустая строка — 0 способов
		{"1", 1},     // "A"
		{"101", 1},   // "JA"
		{"100", 0},   // нельзя декодировать
	}

	for _, f := range funcs {
		for _, tt := range tests {
			got := f.fn(tt.input)
			if got != tt.want {
				t.Errorf("%s(%q) = %d; want %d", f.name, tt.input, got, tt.want)
			}
		}
	}
}
