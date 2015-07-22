package main

import "testing"

func Test3(t *testing.T) {
	r := Main()
	if Answer != r {
		t.Errorf("3 Error, got %d", r)
	}
}
