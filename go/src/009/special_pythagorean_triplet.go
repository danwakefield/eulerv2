package main

/* https://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c ,
for which, a^2 + b^2 = c^2 For example, 3^2 + 4^2 = 9 + 16 = 25 =
5^2 . There exists exactly one Pythagorean triplet for which a + b +
c = 1000. Find the product abc .
*/

import "fmt"

var Answer = 31875000

func Main() int {
	for a := 1; a < 1001; a++ {
		for b := a + 1; b < 1001-a; b++ {
			c := 1000 - a - b
			if c < b {
				break
			}

			if ((a * a) + (b * b)) == (c * c) {
				return a * b * c
			}
		}
	}
	return -1
}

func main() {
	result := Main()
	fmt.Println(result)
}
