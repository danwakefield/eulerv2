package main

import "testing"

func Test19(t *testing.T) {
	r := Main()
	if Answer != r {
		t.Errorf("19 Error, got %d", r)
	}
}
