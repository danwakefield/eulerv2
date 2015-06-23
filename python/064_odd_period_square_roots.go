package main

// https://projecteuler.net/problem=64

// All square roots are periodic when written as continued fractions and
// can be written in the form:
//     SEE URL, COMPLEX MATH TEMPLATING

import (
	"fmt"
	"math"
	"runtime"
	"sync"
)

var (
	SquareBitPatterns = map[int]struct{}{
		0x00: {},
		0x01: {},
		0x04: {},
		0x09: {},
		0x10: {},
		0x11: {},
		0x19: {},
		0x21: {},
		0x24: {},
		0x29: {},
		0x31: {},
		0x39: {},
	}
)

func init() {
	runtime.GOMAXPROCS(runtime.NumCPU())
}

func main() {
	var squares = make(map[int]int)
	for i := 1; i < 12000; i++ {
		squares[i] = i * i
	}

	var results = make(map[int]int)
	var resultsMutex sync.Mutex
	var wg sync.WaitGroup

	for d := 2; d < 10; d++ {
		wg.Add(1)
		go func(dVal int, sqs map[int]int) {
			defer wg.Done()
			if isPerfectSquare(dVal) {
				return
			}
			// x^2 - (d*y^2) = 1
			// flip it around so
			// x^2 = 1 + (d*y^2)
			for y, yVal := range squares {
				t := (dVal * yVal) + 1
				for x, xVal := range squares {
					if xVal > t {
						break
					}
					if t == xVal {
						fmt.Printf("%d^2 - (%d * %d^2) = 1\n", x, dVal, y)
						resultsMutex.Lock()
						results[dVal] = x
						resultsMutex.Unlock()
						return
					}
				}
			}
			return
		}(d)
	}

	wg.Wait()

	highest := 0
	highestD := 0
	// find the value of d(key) that has the largest x(val)
	for k, v := range results {
		if v > highest {
			highest = v
			highestD = k
		}
	}

	fmt.Printf("%d\n", highestD)
	fmt.Printf("%#v\n", results)
}

func isPerfectSquare(n int) bool {
	if n < 0 {
		return false
	}

	x := n & 0x0F
	_, ok := SquareBitPatterns[x]
	if !ok {
		return false
	}

	sq := int(math.Sqrt(float64(n)))
	return sq*sq == n
}
