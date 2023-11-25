#!/bin/bash
set -euxo pipefail

# Re-Compile the Go code
pushd ..
GOOS=js GOARCH=wasm go build -o main.wasm
popd
cp ../main.wasm .

# Download the wasm_exec.js file. It may skew with the Go version installed and cause problems, but ¯\_(ツ)_/¯
if [[ ! -e wasm_exec.js ]]; then
    curl https://raw.githubusercontent.com/golang/go/master/misc/wasm/wasm_exec.js -o wasm_exec.js
fi

python -m http.server
