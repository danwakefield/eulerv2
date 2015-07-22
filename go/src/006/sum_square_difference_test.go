package main

import "testing"

func Test6(t *testing.T) {
	r := Main()
	if Answer != r {
		t.Errorf("6 Error, got %d", r)
	}
}
