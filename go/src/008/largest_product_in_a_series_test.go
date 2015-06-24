package main

import "testing"

func Test8(t *testing.T) {
	r := Main()
	if Answer != r {
		t.Errorf("8 Error")
	}
}
