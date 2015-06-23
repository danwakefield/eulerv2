package utils

func PrimeGenerator() <-chan int {
	// http://stackoverflow.com/a/3796442
	ch := make(chan int)
	seen := map[int]int{}
	go func() {
		ch <- 2
		for q := 3; ; q += 2 {
			p, ok := seen[q]
			if !ok {
				seen[q*q] = q
				ch <- q
			} else {
				x := q + 2*p
				for {
					_, ok := seen[x]
					if !ok {
						break
					}
					x += 2 * p
				}
				seen[x] = p
			}
		}
	}()
	return ch
}

func FibonnaciGenerator() <-chan int {
	ch := make(chan int)
	go func() {
		a := 1
		b := 1

		ch <- 1
		ch <- 1

		for {
			f := a + b
			a = b
			b = f
			ch <- f
		}
	}()
	return ch
}

func MakeNumberSequence(next func(n int) int) chan int {
	out := make(chan int)
	go func() {
		n := 1
		for {
			v := next(n)
			out <- v
			n++
		}
	}()
	return out
}

func SquareNumberGenerator() <-chan int {
	// https://oeis.org/A000290
	return MakeNumberSequence(func(i int) int { return i * i })
}

func TriangularNumberGenerator() <-chan int {
	return MakeNumberSequence(func(i int) int { return int((i * (i + 1)) / 2) })
}

func PentagonalNumberGenerator() <-chan int {
	return MakeNumberSequence(func(i int) int { return int(((3 * (i * i)) - i) / 2) })
}

func HexagonalNumberGenerator() <-chan int {
	return MakeNumberSequence(func(i int) int { return int((2 * (i * i)) - i) })
}

func HeptagonalNumberGenerator() <-chan int {
	return MakeNumberSequence(func(i int) int { return int(((5 * (i * i)) - (3 * i)) / 2) })
}

func OctagonalNumberGenerator() <-chan int {
	return MakeNumberSequence(func(i int) int { return int((3 * (i * i)) - (2 * i)) })
}
