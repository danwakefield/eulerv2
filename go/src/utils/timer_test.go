package utils

import "testing"

func TestTimer(t *testing.T) {
	killChan := make(chan struct{})
	go Timer(killChan)

	close(killChan)
}
