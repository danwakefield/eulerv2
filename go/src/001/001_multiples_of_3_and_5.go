package main

// https://projecteuler.net/problem=1
//
// If we list all the natural numbers below 10 that are multiples of 3 or 5,
// we get 3, 5, 6 and 9. The sum of these multiples is 23.
//
// Find the sum of all the multiples of 3 or 5 below 1000.

import (
	"fmt"
	"os"
	"time"
	"utils"
)

func main() {
	timerChan := make(chan struct{})
	go utils.Timer(timerChan)
	defer func() {
		close(timerChan)
		time.Sleep(20)
	}()

	var sum int
	for i := 0; i < utils.Thou; i++ {
		if utils.ModInt(i, 3) == 0 || utils.ModInt(i, 5) == 0 {
			sum += i
		}
	}

	fmt.Printf("%s: %d\n", os.Args[0], sum)
}
