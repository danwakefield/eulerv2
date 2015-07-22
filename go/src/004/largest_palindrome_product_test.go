package main

import "testing"

func Test4(t *testing.T) {
	r := Main()
	if Answer != r {
		t.Errorf("4 Error, got %d", r)
	}
}
