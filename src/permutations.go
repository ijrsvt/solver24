package solver24

func Permutations[T any](inp []T) [][]T {
	return permutationsRecursive([][]T{{}}, inp)
}

func permutationsRecursive[T any](gen [][]T, inp []T) [][]T {
	if len(inp) == 0 {
		return gen
	}

	result := [][]T{}
	for i, v := range inp {
		inpTemp := make([]T, len(inp))
		copy(inpTemp, inp)
		inpTemp = append(inpTemp[:i], inpTemp[i+1:]...)

		gen2 := make([][]T, len(gen))
		copy(gen2, gen)
		for i2, v2 := range gen2 {
			gen2[i2] = append(v2, v)
		}
		result = append(result, permutationsRecursive(gen2, inpTemp)...)
	}
	return result
}
