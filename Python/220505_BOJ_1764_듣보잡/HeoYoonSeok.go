package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

var (
	N = 0
	M = 0
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
)

func main() {

	defer w.Flush()

	hearMap := make(map[string]int)

	answer := make([]string, 0)

	fmt.Fscan(r, &N, &M)

	var name string
	for i := 0; i < N; i++ {
		fmt.Fscan(r, &name)
		hearMap[name] = 0
	}
	for i := 0; i < M; i++ {
		fmt.Fscan(r, &name)
		_, exists := hearMap[name]
		if exists {
			answer = append(answer, name)
		}
	}

	sort.Strings(answer)
	fmt.Fprintln(w, len(answer))
	for i := 0; i < len(answer); i++ {
		fmt.Fprintln(w, answer[i])
	}
}
