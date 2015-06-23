package utils

import (
	"math"
	"strconv"
)

var Log10 = math.Log(10)

func RotateDigits(n int) int {
	fn := float64(n)
	return (n / 10) + int(math.Mod(fn, 10))*int(math.Pow(10, math.Floor(math.Log(fn)/Log10)))
}

func DigitLength(n int) int {
	// http://stackoverflow.com/a/1489873
	// Binary search is achieved by the nesting of the ifs.
	// only works on integers 0 to 1e10-1
	if n >= TThou {
		if n >= TMill {
			if n >= HMill {
				if n >= Bill {
					return 10
				} else {
					return 9
				}
			} else {
				return 8
			}
		} else if n >= HThou {
			if n >= Mill {
				return 7
			} else {
				return 6
			}
		} else {
			return 5
		}
	} else if n >= 100 {
		if n >= Thou {
			return 4
		} else {
			return 3
		}
	} else if n >= 10 {
		return 2
	} else {
		return 1
	}
}

func GCD(a, b int) int {
	for a != b {
		if a > b {
			a -= b
		} else {
			b -= a
		}
	}

	return a
}

func ComposingDigits(n int) []rune {
	s := strconv.Itoa(n)
	sl := make([]rune, len(s))
	for i, c := range s {
		sl[i] = c
	}
	return sl
}
