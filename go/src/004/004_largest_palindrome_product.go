package main

// https://projecteuler.net/problem=4

// A palindromic number reads the same both ways. The largest palindrome
// made from the product of two 2-digit numbers is 9009 = 91 × 99. Find
// the largest palindrome made from the product of two 3-digit numbers.

// Answer: 906609

import (
	"fmt"
	"strconv"
	u "utils"
)

func main() {
	var answer int

	for i := 1000; i > 100; i-- {
		for j := i; j > 100; j-- {
			t := i * j
			if u.IsPalindrome(strconv.Itoa(t)) {
				if t > answer {
					answer = t
				}
			}
		}
	}

	fmt.Println(answer)
}
