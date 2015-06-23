package utils

import "testing"

func TestIsPerfectSquare(t *testing.T) {
	tests := map[int]bool{
		4:  true,
		9:  true,
		16: true,
		25: true,
		36: true,

		7:  false,
		10: false,
		15: false,
		37: false,
	}

	for k, v := range tests {
		r := IsPerfectSquare(k)
		if v != r {
			t.Errorf("IsPerfectSquare(%d) should be %v", k, v)
		}
	}
}

func TestIsTriangular(t *testing.T) {
	tests := map[int]bool{
		1:  true,
		3:  true,
		6:  true,
		10: true,
		15: true,

		4:  false,
		5:  false,
		7:  false,
		12: false,
	}

	for k, v := range tests {
		r := IsTriangular(k)
		if v != r {
			t.Errorf("IsTriangular(%d) should be %v", k, v)
		}
	}
}

func TestIsPentagonal(t *testing.T) {
	tests := map[int]bool{
		1:  true,
		5:  true,
		12: true,
		22: true,

		4:  false,
		7:  false,
		9:  false,
		13: false,
	}

	for k, v := range tests {
		r := IsPentagonal(k)
		if v != r {
			t.Errorf("IsPentagonal(%d) should be %v", k, v)
		}
	}
}

func TestIsHexagonal(t *testing.T) {
	tests := map[int]bool{
		1:  true,
		6:  true,
		15: true,
		28: true,

		4:  false,
		7:  false,
		9:  false,
		13: false,
	}

	for k, v := range tests {
		r := IsHexagonal(k)
		if v != r {
			t.Errorf("IsHexagonal(%d) should be %v", k, v)
		}
	}
}

func TestIsHeptagonal(t *testing.T) {
	tests := map[int]bool{
		1:  true,
		7:  true,
		18: true,
		34: true,

		4:  false,
		8:  false,
		20: false,
		30: false,
	}

	for k, v := range tests {
		r := IsHeptagonal(k)
		if v != r {
			t.Errorf("IsHeptagonal(%d) should be %v", k, v)
		}
	}
}

func TestIsOctagonal(t *testing.T) {
	tests := map[int]bool{
		1:  true,
		8:  true,
		21: true,
		40: true,

		4:  false,
		10: false,
		20: false,
		30: false,
	}

	for k, v := range tests {
		r := IsOctagonal(k)
		if v != r {
			t.Errorf("IsOctagonal(%d) should be %v", k, v)
		}
	}
}

func TestIsPrime(t *testing.T) {
	ch := PrimeGenerator()
	for i := 0; i < 100; i++ {
		p := <-ch
		if !IsPrime(p) {
			t.Errorf("IsPrime(%d) should be true", p)
		}
	}
}

func BenchmarkIsPrime(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_ = IsPrime(17389)
	}
}

func TestIsPalindrome(t *testing.T) {
	tests := map[string]bool{
		"abba":        true,
		"abccba":      true,
		"aba":         true,
		"12345 54321": true,

		"abc":       false,
		"123456789": false,
		"aabcccaa":  false,
	}

	for k, v := range tests {
		r := IsPalindrome(k)
		if v != r {
			t.Errorf("IsPalindrome(%s) should be %v", k, v)
		}
	}
}

func TestIsPermutation(t *testing.T) {
	tests := []struct {
		A        string
		B        string
		Expected bool
	}{
		{"aaa", "aaa", true},
		{"baa", "aab", true},
		{"abc12345", "12345abc", true},

		{"ccc", "bbb", false},
		{"cc", "cccc", false},
	}

	for _, v := range tests {
		r := IsPermutation(v.A, v.B)
		if r != v.Expected {
			t.Errorf("IsPermutation(%s, %s) should be %s", v.A, v.B, v.Expected)
		}
	}
}

func TestIsPandigital(t *testing.T) {
	tests := map[int]bool{
		123:        true,
		1234:       true,
		12345:      true,
		123456:     true,
		1234567890: true,

		4444:   false,
		234234: false,
		890:    false,
	}
	for k, v := range tests {
		r := IsPandigital(k)
		if v != r {
			t.Errorf("IsPandigital(%d) should be %s", k, v)
		}
	}

}
