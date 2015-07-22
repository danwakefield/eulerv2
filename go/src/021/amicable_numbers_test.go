package main

import "testing"

func Test21(t *testing.T) {
	r := Main()
	if Answer != r {
		t.Errorf("21 Error, got %d", r)
	}
}
