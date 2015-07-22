package main

import "testing"

func Test2(t *testing.T) {
	r := Main()
	if Answer != r {
		t.Errorf("2 Error, got %d", r)
	}
}
