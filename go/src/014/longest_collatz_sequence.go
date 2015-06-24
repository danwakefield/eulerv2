package main

/* https://projecteuler.net/problem=14

The following iterative sequence is defined for the set of positive
integers:
    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this
sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1. Which starting number, under
one million, produces the longest chain? NOTE: Once the chain starts
the terms are allowed to go above one million.

Answer: 837799
*/

import (
	"fmt"
	u "utils"
)

var (
	Answer       = u.Zero
	Data         []string
	CollatzCache = map[int]int{}
)

func collatz(n int) int {
	chainLength := 0
	for n > 1 {
		l, ok := CollatzCache[n]
		if ok {
			chainLength += l
			break
		}

		if u.ModInt(n, 2) == 0 {
			n = n / 2
		} else {
			n = n*3 + 1
		}
		chainLength++
	}

	return chainLength
}

func Main() int {
	highRunLength := 0
	highRun := 0
	for i := 1; i < u.Mill; i++ {
		runLength := collatz(i)
		if runLength > highRunLength {
			highRun = i
			highRunLength = runLength
		}
		if _, ok := CollatzCache[i]; !ok {
			CollatzCache[i] = runLength
		}
	}

	return highRun
}

func main() {
	fmt.Println(Main())
}
