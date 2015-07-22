package main

import "testing"

func Test5(t *testing.T) {
	r := Main()
	if Answer != r {
		t.Errorf("5 Error, got %d", r)
	}
}
