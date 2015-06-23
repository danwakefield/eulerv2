package utils

import "testing"

func TestDigitLength(t *testing.T) {
	tests := map[int]int{
		1:     1,
		10:    2,
		100:   3,
		Thou:  4,
		TThou: 5,
		HThou: 6,
		Mill:  7,
		TMill: 8,
		HMill: 9,
		Bill:  10,
	}

	for k, v := range tests {
		r := DigitLength(k)
		if r != v {
			t.Errorf("DigitLength(%d) should be %d, got %d", k, v, r)
		}
	}
}

func TestGCD(t *testing.T) {
	tests := []struct {
		X        int
		Y        int
		Expected int
	}{
		{25, 15, 5},
		{7, 15, 1},
		{7, 14, 7},
		{100, 400, 100},
	}

	for _, v := range tests {
		r := GCD(v.X, v.Y)
		if r != v.Expected {
			t.Errorf("GCD(%d, %d) should be %d, got %d", v.X, v.Y, v.Expected, r)
		}
	}
}

func TestComposingDigits(t *testing.T) {
	tests := []struct {
		In       int
		Expected []rune
	}{
		{123, []rune{'1', '2', '3'}},
		{5467, []rune{'5', '4', '6', '7'}},
		{9, []rune{'9'}},
	}

	for _, v := range tests {
		r := ComposingDigits(v.In)
		if len(r) != len(v.Expected) {
			t.Errorf("ComposingDigits(%d) should be %#v, got %#v", v.In, v.Expected, r)
			continue
		}
		for k, c := range v.Expected {
			if r[k] != c {
				t.Errorf("ComposingDigits(%d) should be %#v, got %#v", v.In, v.Expected, r)
			}
		}
	}
}
