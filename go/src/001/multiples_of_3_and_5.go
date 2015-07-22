package main

// https://projecteuler.net/problem=1
//
// If we list all the natural numbers below 10 that are multiples of 3 or 5,
// we get 3, 5, 6 and 9. The sum of these multiples is 23.
//
// Find the sum of all the multiples of 3 or 5 below 1000.

import (
	"fmt"
	u "utils"
)

var Answer = 233168

func Main() int {
	var sum int
	for i := 0; i < u.Thou; i++ {
		if u.ModInt(i, 3) == 0 || u.ModInt(i, 5) == 0 {
			sum += i
		}
	}
	return sum
}

func main() {
	fmt.Println(Main())
}
