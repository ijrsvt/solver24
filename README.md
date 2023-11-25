# solver24
Solving the 24 Card Game!


### Compiling to WASM
To compile the Golang code into WASM, run:
```
GOOS=js GOARCH=wasm go build -o main.wasm
```

See the `wasm_example` directory for how to use the library.