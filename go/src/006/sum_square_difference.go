package main

import "fmt"

// https://projecteuler.net/problem=6

// The sum of the squares of the first ten natural numbers is,
// 1^2 + 2^2 + ... + 10^2 = 385
// The square of the sum of the first ten natural numbers is,
// (1 + 2 + ... + 10)^2 = 55^2 = 3025
// Hence the difference between the sum of the squares of the
// first ten natural numbers and
// the square of the sum is 3025 − 385 = 2640. Find the difference
// between the sum of the squares of the first one hundred natural
// numbers and the square of the sum.

var Answer = 25164150

func squareSums(n int) int {
	lastSquare := 16
	lastPow := 4
	// First 4 squares dont share this additive behaviour. 1,4,6,9,16
	total := 30

	for i := 5; i < n+1; i++ {
		tmp := lastSquare + i + lastPow
		lastSquare = tmp
		lastPow = i
		total += tmp
	}

	return total
}

func Main() int {
	sumOfSquare := squareSums(100)
	squareOfSum := 0
	for i := 1; i < 101; i++ {
		squareOfSum += i
	}
	squareOfSum *= squareOfSum

	if squareOfSum > sumOfSquare {
		return squareOfSum - sumOfSquare
	} else {
		return sumOfSquare - squareOfSum
	}

}

func main() {
	fmt.Println(Main())
}
