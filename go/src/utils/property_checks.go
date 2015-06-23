package utils

import (
	"math"
	"sort"
	"strconv"
)

var squareBitPatterns = map[int]bool{
	0x00: true, 0x39: true, 0x24: true, 0x09: true,
	0x19: true, 0x01: true, 0x29: true, 0x10: true,
	0x21: true, 0x04: true, 0x31: true, 0x11: true,
}

func SqrtInt(n int) int {
	return int(math.Sqrt(float64(n)))
}

func IsPerfectSquare(n int) bool {
	if n < 0 {
		return false
	}
	x := n & 0x0F
	// Uses Go's default map fill behaviour here,
	// Anything not in BitPatterns will give a false
	// as a result so no need to do a two item map check.
	if !squareBitPatterns[x] {
		return false
	}

	sq := SqrtInt(n)
	return sq*sq == n
}

func IsTriangular(n int) bool {
	return IsPerfectSquare(8*n + 1)
}

func IsPentagonal(n int) bool {
	x := (math.Sqrt(float64(24*n+1)) + 1) / 6
	return x == math.Floor(x)
}

func IsHexagonal(n int) bool {
	x := (math.Sqrt(float64(8*n+1)) + 1) / 4
	return x == math.Floor(x)
}

func IsHeptagonal(n int) bool {
	x := (math.Sqrt(float64(40*n+9)) + 3) / 10
	return x == math.Floor(x)
}

func IsOctagonal(n int) bool {
	x := (math.Sqrt(float64(3*n+1)) + 1) / 3
	return x == math.Floor(x)
}

func IsPrime(n int) bool {
	if n <= 3 {
		return n >= 2
	}
	if ModInt(n, 2) == 0 || ModInt(n, 3) == 0 {
		return false
	}
	for i := 5; i < int(math.Sqrt(float64(n)))+1; i += 6 {
		if ModInt(n, i) == 0 || ModInt(n, i+2) == 0 {
			return false
		}
	}
	return true
}

func ModInt(a, b int) int {
	l := 0
	r := a
	for l < r {
		m := (l + r) / 2
		if (a - m*b) >= b {
			l = m + 1
		} else {
			r = m
		}
	}

	return a - l*b
}

func IsPalindrome(s string) bool {
	n := len(s)
	r := []rune(s)

	for i := 0; i < n/2; i++ {
		if r[i] != r[n-i-1] {
			return false
		}
	}
	return true
}

type runeSlice []rune

func (p runeSlice) Len() int           { return len(p) }
func (p runeSlice) Swap(i, j int)      { p[i], p[j] = p[j], p[i] }
func (p runeSlice) Less(i, j int) bool { return p[i] < p[j] }

func IsPermutation(a, b string) bool {
	if len(a) != len(b) {
		return false
	}
	r1 := runeSlice(a)
	r2 := runeSlice(b)
	sort.Sort(r1)
	sort.Sort(r2)
	for k, v := range r1 {
		if v != r2[k] {
			return false
		}
	}
	return true
}

func IsPandigital(n int) bool {
	r := runeSlice(strconv.Itoa(n))
	sort.Sort(r)
	start := 0
	if r[0] == '0' {
		if len(r) != 10 {
			return false
		}
		start = 48
	} else if r[0] == '1' {
		start = 49
	} else {
		return false
	}
	for k, v := range r {
		// Does not support 0 in pandigitals
		if v != rune(start+k) {
			return false
		}
	}
	return true
}
