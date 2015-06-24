package main

import "testing"

func Test13(t *testing.T) {
	r := Main()
	if Answer != r {
		t.Errorf("13 Error, got %d", r)
	}
}
