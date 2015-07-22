package fast

import "math/big"

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
	lenSmallOddSwing          = uint(len(smallOddSwing))
	smallOddFactorial []int64 = []int64{1, 1, 1, 3, 3,
		15, 45, 315, 315, 2835, 14175, 155925, 467775,
		6081075, 42567525, 638512875, 638512875, 10854718875,
		97692469875, 1856156927625, 9280784638125, 194896477400625,
		2143861251406875, 49308808782358125, 147926426347074375,
		3698160658676859375}
	lenSmallOddFactorial            = uint(len(smallOddFactorial))
	smallOddDoubleFactorial []int64 = []int64{1, 1, 1, 3, 1,
		15, 3, 105, 3, 945, 15, 10395, 45, 135135, 315, 2027025, 315,
		34459425, 2835, 654729075, 14175, 13749310575, 155925,
		316234143225, 467775, 7905853580625, 6081075, 213458046676875,
		42567525, 6190283353629375, 638512875, 191898783962510625,
		638512875, 6332659870762850625, 10854718875}
	lenSmallOddDoubleFactorial = uint(len(smallOddDoubleFactorial))
)

type swing struct {
	primes  *primes
	factors []uint64
}

func makeSwing(n uint) (ps *swing) {
	ps = new(swing)
	ps.primes = makePrimes(uint64(n))
	if n >= lenSmallOddSwing {
		ps.factors = make([]uint64, n)
	}
	return
}

func (ps *swing) swing(m uint) *big.Int {
	if uint64(m) > ps.primes.sieveLen {
		return nil
	}
	r := ps.oddSwing(m)
	return r.Lsh(r, bitCount(uint64(m)))
}

func (ps *swing) oddSwing(k uint) *big.Int {
	if k < lenSmallOddSwing {
		return big.NewInt(smallOddSwing[k])
	}
	rootK := floorSqrt(k)
	var i int

	ps.primes.iterator(3, uint64(rootK), func(p uint64) {
		q := uint64(k) / p
		for q > 0 {
			if q&1 == 1 {
				ps.factors[i] = p
				i++
			}
			q /= p
		}
	})

	ps.primes.iterator(uint64(rootK+1), uint64(k/3), func(p uint64) {
		if (uint64(k) / p & 1) == 1 {
			ps.factors[i] = p
			i++
		}
	})

	ps.primes.iterator(uint64(k/2+1), uint64(k), func(p uint64) {
		ps.factors[i] = p
		i++
	})
	return product(ps.factors[0:i])
}

func (ps *swing) primeFactorial(k uint) (r *big.Int) {
	if uint64(k) > ps.primes.sieveLen {
		return nil
	}
	r = ps.oddFactorial(k)
	return r.Lsh(r, k-bitCount(uint64(k)))
}

func (ps *swing) oddFactorial(n uint) *big.Int {
	if n < lenSmallOddFactorial {
		return big.NewInt(int64(smallOddFactorial[n]))
	}
	of := ps.oddFactorial(n / 2)
	return of.Mul(of.Mul(of, of), ps.oddSwing(n))
}

func swingFactorial(n uint) (r *big.Int) {
	var oddFactNDiv2, oddFactNDiv4 big.Int

	// closes on oddFactNDiv2, oddFactNDiv4
	oddSwing := func(n uint) (r *big.Int) {
		if n < lenSmallOddSwing {
			return big.NewInt(smallOddSwing[n])
		}

		length := (n - 1) / 4
		if n%4 != 2 {
			length++
		}

		high := n - (n+1)&1
		ndiv4 := n / 4
		var oddFact big.Int

		if ndiv4 < lenSmallOddFactorial {
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
		if n < lenSmallOddFactorial {
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

func (p *primes) binomial(n, k uint) *big.Int {
	if uint64(n) > p.sieveLen {
		return nil
	}
	var r big.Int

	if k > n {
		return &r
	}
	if k > n/2 {
		k = n - k
	}
	if k < 3 {
		switch k {
		case 0:
			return r.SetInt64(1)
		case 1:
			return r.SetInt64(int64(n))
		case 2:
			var n1 big.Int
			return r.Rsh(r.Mul(r.SetInt64(int64(n)), n1.SetInt64(int64(n-1))), 1)
		}
	}

	var i int
	rootN := uint64(floorSqrt(n))
	factors := make([]uint64, n)

	p.iterator(2, rootN, func(p uint64) {
		var r, nn, kk uint64 = 0, uint64(n), uint64(k)
		for nn > 0 {
			if nn%p < kk%p+r {
				r = 1
				factors[i] = p
				i++
			} else {
				r = 0
			}
			nn /= p
			kk /= p
		}
	})

	p.iterator(rootN+1, uint64(n/2), func(p uint64) {
		if uint64(n)%p < uint64(k)%p {
			factors[i] = p
			i++
		}
	})

	p.iterator(uint64(n-k+1), uint64(n), func(p uint64) {
		factors[i] = p
		i++
	})

	return product(factors[0:i])
}

func (p *primes) doubleFactorial(n uint) (r *big.Int) {
	nEven := n&1 == 0
	if n < lenSmallOddDoubleFactorial {
		r = big.NewInt(smallOddDoubleFactorial[n])
	} else {
		var nn uint
		if nEven {
			nn = n / 2
		} else {
			nn = n + 1
		}

		if uint64(nn) > p.sieveLen && nn > lenSmallOddSwing {
			return nil
		}

		r = p.oddDoubleFactorial(nn, n)
	}

	if nEven {
		r.Lsh(r, n-bitCount(uint64(n/2)))
	}

	return
}

func (p *primes) oddDoubleFactorial(n, m uint) *big.Int {
	if n < lenSmallOddFactorial {
		return big.NewInt(smallOddFactorial[n])
	}

	of := p.oddDoubleFactorial(n/2, m)
	if n < m {
		of.Mul(of, of)
	}

	return of.Mul(of, p.oddSwing(n))
}

const (
	bitsPerInt = 32
	mask       = bitsPerInt - 1
	log2Int    = 5
)

// holds completed sieve

type primes struct {
	sieveLen    uint
	isComposite []uint32
}

// constructor, completes sieve.

func makePrimes(n uint) (ps *primes) {
	ps = new(primes)
	ps.sieveLen = n

	if n < 386 {
		ps.isComposite = []uint32{1762821248, 848611808, 3299549660, 2510511646}
		return
	}

	ps.isComposite = make([]uint32, (n/(3*bitsPerInt))+1)
	var (
		d1, d2, p1, p2, s, s2 uint = 8, 8, 3, 7, 7, 3
		l, c, max, inc        uint = 0, 1, n / 3, 0
		toggle                bool
	)

	for s < max { // --  scan the sieve
		// --  if a prime is found ...
		if (ps.isComposite[l>>log2Int] & (1 << (l & mask))) == 0 {
			inc = p1 + p2 // --  ... cancel its multiples
			// --  ... set c as composite
			for c = s; c < max; c += inc {
				ps.isComposite[c>>log2Int] |= 1 << (c & mask)
			}

			for c = s + s2; c < max; c += inc {
				ps.isComposite[c>>log2Int] |= 1 << (c & mask)
			}
		}
		l++
		toggle = !toggle
		if toggle {
			s += d2
			d1 += 16
			p1 += 2
			p2 += 2
			s2 = p2
		} else {
			s += d1
			d2 += 8
			p1 += 2
			p2 += 6
			s2 = p1
		}
	}

	return
}

func (ps *primes) iterator(min, max uint, visitor func(uint)) bool {
	// isComposite[0] ... isComposite[n] includes
	// 5 <= primes numbers <= 96*(n+1) + 1

	if min < 2 {
		min = 2
	}

	if max > ps.sieveLen {
		return false // Max larger than sieve
	}

	if min <= 2 {
		visitor(2)
	}

	if min <= 3 {
		visitor(3)
	}

	absPos := uint((min+(min+1)%2)/3 - 1)
	index := absPos / bitsPerInt
	bitPos := absPos % bitsPerInt
	toggle := (bitPos & 1) == 1
	prime := uint(5 + 3*(bitsPerInt*index+bitPos) - (bitPos & 1))

	for prime <= max {
		bitField := ps.isComposite[index] >> bitPos
		index++

		for ; bitPos < bitsPerInt; bitPos++ {
			if (bitField & 1) == 0 {
				visitor(prime)
			}

			toggle = !toggle
			if toggle {
				prime += 2
			} else {
				prime += 4
			}

			if prime > max {
				return true
			}

			bitField >>= 1
		}

		bitPos = 0
	}

	return true
}

const productSerialThreshold = 24

func product(seq []uint64) *big.Int {
	if len(seq) <= productSerialThreshold {
		var b big.Int
		sprod := big.NewInt(int64(seq[0]))
		for _, s := range seq[1:] {
			b.SetInt64(int64(s))
			sprod.Mul(sprod, &b)
		}
		return sprod
	}

	halfLen := len(seq) / 2
	lprod := product(seq[0:halfLen])
	rprod := product(seq[halfLen:])
	return lprod.Mul(lprod, rprod)
}

const (
	ff    = 1<<64 - 1
	mask1 = ff / 3
	mask3 = ff / 5
	maskf = ff / 17
	maskp = maskf >> 3 & maskf
)

func bitCount(w uint64) uint { // loopfree!
	w -= w >> 1 & mask1
	w = w&mask3 + w>>2&mask3
	w = (w + w>>4) & maskf
	return uint(w * maskp >> 56)
}

func floorSqrt(n uint) uint {
	for b := n; ; {
		a := b
		b = (n/a + a) / 2
		if b >= a {
			return a
		}
	}
	return 0 // unreachable.  required by current compiler.
}
