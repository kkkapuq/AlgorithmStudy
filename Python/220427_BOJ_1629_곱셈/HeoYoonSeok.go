package main

import (
	"bufio"
	"fmt"
	"os"
)

func power(a int64, b int64, c int64) int64 {
	if b == 1 {
		return a % c
	} else if b%2 == 1 {
		return a * power(a, b-1, c) % c
	} else {
		tmp := power(a, b/2, c)
		return (tmp * tmp) % c
	}
}
func main() {

	w := bufio.NewWriter(os.Stdout)
	r := bufio.NewReader(os.Stdin)
	defer w.Flush()

	var A, B, C int64

	fmt.Fscan(r, &A, &B, &C)

	var answer int64
	answer = power(A, B, C)

	fmt.Fprint(w, answer)

}
