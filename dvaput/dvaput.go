package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scanf("%d\n", &n)

	// fmt.Printf("%v\n", n)

	var in string
	fmt.Scanf("%s\n", &in)
	in += "$"

	// fmt.Printf("%v\n", in)

	bytes := []byte(in)
	sa := buildSA(bytes)
	isa := buildISA(sa)

	lcp := buildLCP(bytes, sa, isa)
	// fmt.Printf("SA: %v\n", sa)
	// fmt.Printf("ISA: %v\n", isa)
	// fmt.Printf("LCP: %v\n", lcp)

	max := 0
	for _, val := range lcp {
		if val > max {
			max = val
		}
	}

	fmt.Printf("%d\n", max)
}
