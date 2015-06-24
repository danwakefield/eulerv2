package main

import "testing"

func Test14(t *testing.T) {
	r := Main()
	if Answer != r {
		t.Errorf("14 Error, got %d", r)
	}
}
