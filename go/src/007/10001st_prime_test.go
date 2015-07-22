package main

import "testing"

func Test7(t *testing.T) {
	r := Main()
	if Answer != r {
		t.Errorf("7 Error, got %d", r)
	}
}
