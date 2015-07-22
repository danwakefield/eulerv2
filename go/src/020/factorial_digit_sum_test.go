package main

import "testing"

func Test20(t *testing.T) {
	r := Main()
	if Answer != r {
		t.Errorf("20 Error, got %d", r)
	}
}
