package main

import "testing"

func Test12(t *testing.T) {
	r := Main()
	if Answer != r {
		t.Errorf("12 Error, got %d", r)
	}
}
