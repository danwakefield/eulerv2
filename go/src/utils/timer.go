package utils

import (
	"fmt"
	"time"
)

func Timer(die <-chan struct{}) {
	start := time.Now()
	<-die
	fmt.Printf("%s\n", time.Since(start))
}
