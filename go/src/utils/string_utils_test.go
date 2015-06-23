package utils

import "testing"

func TestReverseString(t *testing.T) {
	tests := map[string]string{
		"abc":    "cba",
		"aaa":    "aaa",
		"aaaaab": "baaaaa",
		"caaba":  "abaac",
	}

	for k, v := range tests {
		r := ReverseString(k)
		if v != r {
			t.Errorf("ReverseString(%s) should be %s, got %s", k, v, r)
		}
	}
}

func TestASCIISum(t *testing.T) {
	tests := map[string]int{
		"abc":         294,
		"aaa":         291,
		"ABC":         198,
		"AAA":         195,
		"Hello World": 1052,
	}

	for k, v := range tests {
		r := ASCIISum(k)
		if v != r {
			t.Errorf("ASCIISum(%s) should be %d, got %d", k, v, r)
		}
	}
}

func TestWordScore(t *testing.T) {
	tests := map[string]int{
		"A":           1,
		"Z":           26,
		"AAA":         3,
		"ABC":         6,
		"HELLO":       52,
		"HELLO WORLD": 92,
	}

	for k, v := range tests {
		r := WordScore(k)
		if v != r {
			t.Errorf("WordScore(%s) should be %d, got %d", k, v, r)
		}
	}
}
