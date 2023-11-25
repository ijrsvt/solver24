package solver24

import (
	"fmt"
	"math"
	"strings"
)

func Solve24(inp []float64) []string {
	errMargin := 0.001
	permutations := Permutations(inp)
	operations := map[string]func(float64, float64) float64{
		"+": add,
		"-": sub,
		"/": divide,
		"*": multiply,
	}

	results := []string{}
	for _, v := range permutations {
		for op1N, op1 := range operations {
			for op2N, op2 := range operations {
				for op3N, op3 := range operations {
					a := v[0]
					b := v[1]
					c := v[2]
					d := v[3]
					resultString := func(str string) string {
						str = strings.ReplaceAll(str, "a", fmt.Sprintf("%v", a))
						str = strings.ReplaceAll(str, "b", fmt.Sprintf("%v", b))
						str = strings.ReplaceAll(str, "c", fmt.Sprintf("%v", c))
						str = strings.ReplaceAll(str, "d", fmt.Sprintf("%v", d))
						str = strings.ReplaceAll(str, "op1", op1N)
						str = strings.ReplaceAll(str, "op2", op2N)
						str = strings.ReplaceAll(str, "op3", op3N)

						return str
					}
					if math.Abs(op3(op2(op1(a, b), c), d)-24) < errMargin {
						results = append(results, resultString("((a op1 b) op2 c) op3 d"))
					}
					if math.Abs(op3(op1(a, b), op2(c, d))-24) < errMargin {
						results = append(results, resultString("(a op1 b) op3 (c op2 d)"))
					}
					if math.Abs(op3(a, op2(b, op1(c, d)))-24) < errMargin {
						results = append(results, resultString("a op3 (b op2 (c op1 d))"))
					}
					// if op3(op2(op1(v[0], v[1]), v[2]), v[3]) == 24 {
					// 	return []string{fmt.Sprintf("(%v %T %v) %v %v %v", v[0], op1, v[1], op2, v[2], v[3])}
					// }
					// if op3(op1(v[0], v[1]), op2(v[2], v[3])) == 24 {
					// 	return []string{fmt.Sprintf("(%v %T %v) %v %v %v", v[0], op1, v[1], op2, v[2], v[3])}
					// }
					// if op2(op1(v[0], v[1]), op3(v[2], v[3])) == 24 {
					// 	return []string{fmt.Sprintf("(%v %T %v) %v %v %v", v[0], op1, v[1], op2, v[2], v[3])}
					// }
					// if op1(op2(v[0], v[1]), op3(v[2], v[3])) == 24 {
					// 	return []string{fmt.Sprintf("(%v %v %v) %v %v %v", v[0], op1, v[1], op2, v[2], v[3])}
					// }
					// if op1(op2(v[0], op3(v[1], v[2])), v[3]) == 24 {
					// 	return []string{fmt.Sprintf("(%v %v %v) %v %v %v", v[0], op1, v[1], op2, v[2], v[3])}
					// }
				}
			}
		}
	}
	return results
}

func add(a, b float64) float64 {
	return a + b
}

func sub(a, b float64) float64 {
	return a - b
}

func divide(a, b float64) float64 {
	return a / b
}

func multiply(a, b float64) float64 {
	return a * b
}
