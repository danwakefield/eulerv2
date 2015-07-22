package main

/* https://projecteuler.net/problem=20

n! means n × ( n − 1) × ... × 3 × 2 × 1 For example,
10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10!
is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!

*/

import (
	"fmt"
	u "utils"
)

var (
	Answer = 648
	Data   []string
)

func Main() int {
	sum := 0
	for _, c := range u.SwingFactorial(100).String() {
		sum += int(c - '0')
	}
	return sum
}

func main() {
	fmt.Println(Main())
}
