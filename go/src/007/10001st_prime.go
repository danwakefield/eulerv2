package main

import (
	"fmt"
	u "utils"
)

// https://projecteuler.net/problem=7
//
// By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
// see that the 6th prime is 13. What is the 10001st prime number?
//
// Answer: 104743

var Answer = 104743

func Main() int {
	v := <-u.DropN(u.TThou, u.PrimeGenerator())
	return v
}

func main() {
	fmt.Println(Main())
}
