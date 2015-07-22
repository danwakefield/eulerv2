package main

// https://projecteuler.net/problem=5

// 2520 is the smallest number that can be divided by each of the numbers
// from 1 to 10 without any remainder. What is the smallest positive
// number that is evenly divisible by all of the numbers from 1 to 20?

// Answer: 232792560

import (
	"fmt"
	u "utils"
)

var Answer = 232792560

func main() {
	fmt.Println(Main())
}

func Main() int {
	var failed bool

	divisors := []int{}
	for i := 11; i < 21; i++ {
		divisors = append(divisors, i)
	}

	for i := 2520; i < u.Bill*10; i += 2520 {
		failed = false
		for _, d := range divisors {
			if u.ModInt(i, d) != 0 {
				failed = true
				break
			}
		}

		if !failed {
			return i
			break
		}
	}

	return 0
}
