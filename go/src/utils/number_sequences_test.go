package utils

import "testing"

func TestPrimeGenerator(t *testing.T) {
	ch := PrimeGenerator()
	seq := []int{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37}
	for k, v := range seq {
		r := <-ch
		if v != r {
			t.Errorf("prime %d: expected %d, got %d", k+1, v, r)
		}
	}
}

func BenchmarkPrimeGenerator(b *testing.B) {
	for i := 0; i < b.N; i++ {
		ch := PrimeGenerator()
		for {
			r := <-ch
			// two thousand'th prime
			// Small enough to give a good number of benchmark loops
			// but large enough that tweaking the generator will show a
			// difference
			if r == 17389 {
				break
			}
		}
	}
}

func TestFibonnaciGenerator(t *testing.T) {
	ch := FibonnaciGenerator()
	seq := []int{1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144}
	for k, v := range seq {
		r := <-ch
		if v != r {
			t.Errorf("fib %d: expected %d, got %d", k+1, v, r)
		}
	}
}

func TestSquareNumberGenerator(t *testing.T) {
	ch := SquareNumberGenerator()
	seq := []int{1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121}
	for k, v := range seq {
		r := <-ch
		if v != r {
			t.Errorf("square %d: expected %d, got %d", k+1, v, r)
		}
	}
}

func TestTriangularNumberGenerator(t *testing.T) {
	ch := TriangularNumberGenerator()
	seq := []int{1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105}
	for k, v := range seq {
		r := <-ch
		if v != r {
			t.Errorf("triangular %d: expected %d, got %d", k+1, v, r)
		}
	}
}

func TestPentagonalNumberGenerator(t *testing.T) {
	ch := PentagonalNumberGenerator()
	seq := []int{1, 5, 12, 22, 35, 51, 70, 92, 117, 145, 176, 210, 247, 287}
	for k, v := range seq {
		r := <-ch
		if v != r {
			t.Errorf("pentagonal %d: expected %d, got %d", k+1, v, r)
		}
	}
}

func TestHexagonalNumberGenerator(t *testing.T) {
	ch := HexagonalNumberGenerator()
	seq := []int{1, 6, 15, 28, 45, 66, 91, 120, 153, 190, 231, 276, 325, 378, 435}
	for k, v := range seq {
		r := <-ch
		if v != r {
			t.Errorf("Hexagonal %d: expected %d, got %d", k+1, v, r)
		}
	}
}

func TestHeptagonalNumberGenerator(t *testing.T) {
	ch := HeptagonalNumberGenerator()
	seq := []int{1, 7, 18, 34, 55, 81, 112, 148, 189, 235, 286, 342, 403, 469, 540, 616}
	for k, v := range seq {
		r := <-ch
		if v != r {
			t.Errorf("Heptagonal %d: expected %d, got %d", k+1, v, r)
		}
	}
}

func TestOctagonalNumberGenerator(t *testing.T) {
	ch := OctagonalNumberGenerator()
	seq := []int{1, 8, 21, 40, 65, 96, 133, 176, 225, 280, 341, 408, 481, 560, 645}
	for k, v := range seq {
		r := <-ch
		if v != r {
			t.Errorf("Octagonal %d: expected %d, got %d", k+1, v, r)
		}
	}
}
