package main

import "testing"

func Test15(t *testing.T) {
	r := Main()
	if Answer != r {
		t.Errorf("15 Error, got %d", r)
	}
}
