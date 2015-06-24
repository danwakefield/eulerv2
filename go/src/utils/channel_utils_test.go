package utils

import "testing"

func TestTakeN(t *testing.T) {
	N := 10
	sqChan := SquareNumberGenerator()
	limitedChan := TakeN(N, sqChan)
	seq := []int{1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121}
	k := 0
	for v := range limitedChan {
		if v != seq[k] {
			t.Errorf("output of the generator has changed element %d should be %d but got %d", k, seq[k], v)
		}
		k++
	}

	if k != N {
		t.Errorf("Expected %d items, recieved %d", N, k)
	}
}

func TestDropN(t *testing.T) {
	N := 3
	sqChan := SquareNumberGenerator()
	limitedChan := DropN(N, sqChan)
	seq := []int{1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121}
	for i := 0; i < 6; i++ {
		v := <-limitedChan
		if v != seq[N+i] {
			t.Errorf("Dropped to many/few items, element %d (%d) should be seq %d (%d)", i, v, N+i, seq[N+i])
		}
	}
}

func TestTakeFrom(t *testing.T) {
	N := 20
	sqChan := SquareNumberGenerator()
	limitedChan := TakeFrom(N, sqChan)
	for i := 0; i < 10; i++ {
		v := <-limitedChan
		if v < N {
			t.Errorf("TakeFrom(%d, ch) is not limiting low values correctly, got %d", N, v)
		}
	}
}

func TestTakeUpto(t *testing.T) {
	N := 20
	sqChan := SquareNumberGenerator()
	limitedChan := TakeUpto(N, sqChan)
	for v := range limitedChan {
		if v > N {
			t.Errorf("TakeFrom(%d, ch) is not limiting high values correctly, got %d", N, v)
		}
	}
}

func TestChanLen(t *testing.T) {
	N := 10
	sqChan := SquareNumberGenerator()
	limitedChan := TakeN(N, sqChan)
	l := ChanLen(limitedChan)

	if N != l {
		t.Errorf("ChanLen should be %d, got %d", N, l)
	}
}
