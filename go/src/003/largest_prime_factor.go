package main

// https://projecteuler.net/problem=3
//
// The prime factors of 13195 are 5, 7, 13 and 29. What is the largest
// prime factor of the number 600851475143 ?
//
// Answer: 6857

import (
	"fmt"
	u "utils"
)

func main() {
	N := 600851475143
	limit := u.SqrtInt(N) + 1

Outer:
	for i := 2; i < limit; i++ {
		for u.ModInt(N, i) == 0 {
			N /= i

			if N == 1 || N == i {
				fmt.Println(i)
				break Outer
			}
		}
	}
}
