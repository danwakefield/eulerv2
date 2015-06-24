package main

import "testing"

func Test10(t *testing.T) {
	r := Main()
	if Answer != r {
		t.Errorf("10 Error, got %d", r)
	}
}
