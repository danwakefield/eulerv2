package main

import "testing"

func Test17(t *testing.T) {
	r := Main()
	if Answer != r {
		t.Errorf("17 Error, got %d", r)
	}
}
