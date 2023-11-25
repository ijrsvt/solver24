//go:build wasm

package main

import (
	"fmt"
	"strconv"
	"strings"
	"syscall/js"

	solver24 "github.com/ijrsvt/solver24/src"
)

func doPermutation(this js.Value, inputs []js.Value) any {
	inp, err := parseNumbers(inputs)
	if err != nil {
		fmt.Println(err)
		return nil
	}

	out := solver24.Solve24(inp)

	jsArray := js.Global().Get("Array").New()
	for _, v := range out {
		jsArray.Call("push", fmt.Sprintf("%v", v))
	}
	fmt.Println("result size: ", len(out))

	return jsArray
}

func main() {
	js.Global().Set("doPermutation", js.FuncOf(doPermutation))

	// Prevent the Golang Program from exiting
	c := make(chan struct{}, 0)
	<-c
}

func parseNumbers(inputs []js.Value) ([]float64, error) {
	if len(inputs) < 4 || len(inputs) > 4 {
		return nil, fmt.Errorf("doPermutation has been called with wrong number of arguments: %v\n", len(inputs))
	}

	inp := []float64{}
	for _, v := range inputs {
		i, err := strconv.Atoi(v.String())
		if err != nil {
			return nil, fmt.Errorf("Argument is not an integer: %v", v)
		}
		inp = append(inp, float64(i))
	}
	return inp, nil
}

func parseStrToNumInput(inputs []js.Value) ([]float64, error) {
	if len(inputs) < 1 || len(inputs) > 1 {
		return nil, fmt.Errorf("doPermutation has been called with wrong number of arguments: %v\n", len(inputs))
	}
	rawString := strings.Split(inputs[0].String(), ",")

	inp := []float64{}
	for _, v := range rawString {
		v = strings.TrimSpace(v)
		i, err := strconv.Atoi(v)
		if err != nil {
			return nil, fmt.Errorf("Argument is not an integer: %v", v)
		}
		inp = append(inp, float64(i))
	}
	return inp, nil
}
