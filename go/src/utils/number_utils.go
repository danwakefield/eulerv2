package utils

import (
	"math"
	"math/big"
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

var (
	smallOddSwing []int64 = []int64{
		1, 1, 1, 3, 3, 15, 5, 35, 35, 315, 63, 693, 231, 3003, 429, 6435, 6435,
		109395, 12155, 230945, 46189, 969969, 88179, 2028117, 676039, 16900975,
		1300075, 35102025, 5014575, 145422675, 9694845, 300540195, 300540195,
		9917826435, 583401555, 20419054425, 2268783825, 83945001525, 4418157975,
		172308161025, 34461632205, 1412926920405, 67282234305, 2893136075115,
		263012370465, 11835556670925, 514589420475, 24185702762325,
		8061900920775, 395033145117975, 15801325804719, 805867616040669,
		61989816618513, 3285460280781189, 121683714103007, 6692604275665385,
		956086325095055, 54496920530418135, 1879204156221315,
		110873045217057585, 7391536347803839, 450883717216034179,
		14544636039226909, 916312070471295267, 916312070471295267}
	smallOddFactorial []int64 = []int64{1, 1, 1, 3, 3,
		15, 45, 315, 315, 2835, 14175, 155925, 467775,
		6081075, 42567525, 638512875, 638512875, 10854718875,
		97692469875, 1856156927625, 9280784638125, 194896477400625,
		2143861251406875, 49308808782358125, 147926426347074375,
		3698160658676859375}
)

func bitCount(w uint64) uint { // loopfree!
	const (
		ff    = 1<<64 - 1
		mask1 = ff / 3
		mask3 = ff / 5
		maskf = ff / 17
		maskp = maskf >> 3 & maskf
	)

	w -= w >> 1 & mask1
	w = w&mask3 + w>>2&mask3
	w = (w + w>>4) & maskf

	return uint(w * maskp >> 56)
}

func SwingFactorial(n uint) (r *big.Int) {
	var oddFactNDiv2, oddFactNDiv4 big.Int

	// closes on oddFactNDiv2, oddFactNDiv4
	oddSwing := func(n uint) (r *big.Int) {
		if n < uint(len(smallOddSwing)) {
			return big.NewInt(smallOddSwing[n])
		}

		length := (n - 1) / 4
		if n%4 != 2 {
			length++
		}

		high := n - (n+1)&1
		ndiv4 := n / 4
		var oddFact big.Int

		if ndiv4 < uint(len(smallOddFactorial)) {
			oddFact.SetInt64(smallOddFactorial[ndiv4])
			r = &oddFact
		} else {
			r = &oddFactNDiv4
		}
		return oddFact.Quo(oddProduct(high, length), r)
	}

	var oddFactorial func(uint) *big.Int
	// closes on oddFactNDiv2, oddFactNDiv4, oddSwing, and itself
	oddFactorial = func(n uint) (oddFact *big.Int) {
		if n < uint(len(smallOddFactorial)) {
			oddFact = big.NewInt(smallOddFactorial[n])
		} else {
			oddFact = oddFactorial(n / 2)
			oddFact.Mul(oddFact.Mul(oddFact, oddFact), oddSwing(n))
		}
		oddFactNDiv4.Set(&oddFactNDiv2)
		oddFactNDiv2.Set(oddFact)
		return oddFact
	}

	oddFactNDiv2.SetInt64(1)
	oddFactNDiv4.SetInt64(1)
	r = oddFactorial(n)

	return r.Lsh(r, n-bitCount(uint64(n)))
}

func oddProduct(m, length uint) *big.Int {
	switch length {
	case 1:
		return big.NewInt(int64(m))
	case 2:
		var mb big.Int
		mb.SetInt64(int64(m))
		mb2 := big.NewInt(int64(m - 2))
		return mb2.Mul(&mb, mb2)
	}
	hlen := length / 2
	h := oddProduct(m-hlen*2, length-hlen)
	return h.Mul(h, oddProduct(m, hlen))
}

func ComposingDigits(n int) []rune {
	s := strconv.Itoa(n)
	sl := make([]rune, len(s))
	for i, c := range s {
		sl[i] = c
	}
	return sl
}
