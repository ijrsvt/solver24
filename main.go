//go:build !wasm

package main

import (
	"fmt"

	solver24 "github.com/ijrsvt/solver24/src"
)

func main() {
	out := solver24.Solve24([]float64{1, 2, 3, 4})
	fmt.Println(len(out))
	out = solver24.Solve24([]float64{4, 1, 3, 2})
	fmt.Println(len(out))

	out = solver24.Solve24([]float64{6, 3, 1, 4})
	fmt.Println(len(out))
	for _, v := range out {
		fmt.Println(v)
	}
	out = solver24.Solve24([]float64{1000, 40, 2, 3})
	fmt.Println(len(out))
	for _, v := range out {
		fmt.Println(v)
	}
}
