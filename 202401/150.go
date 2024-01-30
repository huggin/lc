import "strconv"

func operator(s string) bool {
	return s == "+" || s == "-" || s == "*" || s == "/"
}

func evalRPN(tokens []string) int {
	op := make([]int, 0)
	for _, a := range tokens {
		if operator(a) {
			op1 := op[len(op)-1]
			op2 := op[len(op)-2]
			op = op[0 : len(op)-2]
			if a == "+" {
				op = append(op, op1+op2)
			} else if a == "-" {
				op = append(op, op2-op1)
			} else if a == "*" {
				op = append(op, op1*op2)
			} else {
				op = append(op, op2/op1)
			}
		} else {
			num, _ := strconv.Atoi(a)
			op = append(op, num)
		}
	}
	return op[0]
}
