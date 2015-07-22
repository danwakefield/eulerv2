package main

import "testing"

func Test1(t *testing.T) {
	r := Main()
	if Answer != r {
		t.Errorf("1 Error, got %d", r)
	}
}
