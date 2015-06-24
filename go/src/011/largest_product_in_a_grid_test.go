package main

import "testing"

func Test11(t *testing.T) {
	r := Main()
	if Answer != r {
		t.Errorf("11 Error, got %d", r)
	}
}
