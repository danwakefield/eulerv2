package utils

func TakeN(n int, in <-chan int) chan int {
	out := make(chan int)
	go func() {
		defer close(out)
		for i := 0; i < n; i++ {
			v := <-in
			out <- v
		}
	}()
	return out
}

func DropN(n int, in <-chan int) chan int {
	out := make(chan int)
	for i := 0; i < n; i++ {
		<-in
	}
	go func() {
		for {
			v := <-in
			out <- v
		}
	}()
	return out
}

func TakeFrom(low int, in <-chan int) chan int {
	out := make(chan int)
	go func() {
		v := <-in
		for v < low {
			v = <-in
		}
		out <- v
		for {
			v = <-in
			out <- v
		}
	}()
	return out
}

func TakeUpto(high int, in <-chan int) chan int {
	out := make(chan int)
	go func() {
		defer close(out)
		for {
			v := <-in
			if v > high {
				break
			}
			out <- v
		}
	}()
	return out
}

func TakeBetween(low, high int, in chan int) chan int {
	return TakeUpto(high, TakeFrom(low, in))
}

func ChanLen(in <-chan int) int {
	l := 0
	for _ = range in {
		l++
	}
	return l
}
