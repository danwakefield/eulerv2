package main

/* https://projecteuler.net/problem=16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000 ?
*/

import (
	"fmt"
	"math/big"
)

var (
	Answer = 1366
)

func Main() int {
	x := big.NewInt(2)
	x.Exp(x, big.NewInt(1000), nil)

	sum := 0
	for _, c := range x.String() {
		sum += int(c - '0')
	}
	return sum
}

func main() {
	fmt.Println(Main())
}
