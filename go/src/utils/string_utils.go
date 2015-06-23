package utils

func ReverseString(s string) string {
	n := len(s)
	r := []rune(s)

	for i := 0; i < n/2; i++ {
		r[i], r[n-i-1] = r[n-i-1], r[i]
	}
	return string(r)
}

func ASCIISum(s string) int {
	sum := 0
	for _, v := range s {
		sum += int(v)
	}
	return sum
}

func WordScore(s string) int {
	return ASCIISum(s) - len(s)*64
}
