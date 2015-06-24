package main

/* https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of
all the primes below two million.
*/

import (
	"fmt"
	u "utils"
)

var (
	Answer = 142913828922
)

func Main() int {
	sum := 0
	ch := u.TakeUpto(u.Mill*2, u.PrimeGenerator())
	for v := range ch {
		sum += v
	}

	return sum
}

func main() {
	result := Main()
	fmt.Println(result)
}
