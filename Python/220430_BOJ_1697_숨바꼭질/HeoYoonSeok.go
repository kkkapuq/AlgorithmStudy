package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	w := bufio.NewWriter(os.Stdout)
	r := bufio.NewReader(os.Stdin)

	defer w.Flush()

	var N, K int
	var q []int
	answerSlc := make([]int, 100001)

	fmt.Fscan(r, &N, &K)
	q = append(q, N)

	for len(q) > 0 {
		index := q[0]
		q = q[1:]
		if index == K {
			break
		}
		if index-1 >= 0 && answerSlc[index-1] == 0 {
			answerSlc[index-1] = answerSlc[index] + 1
			q = append(q, index-1)
		}
		if index+1 < 100001 && answerSlc[index+1] == 0 {
			answerSlc[index+1] = answerSlc[index] + 1
			q = append(q, index+1)
		}
		if index*2 < 100001 && answerSlc[index*2] == 0 {
			answerSlc[index*2] = answerSlc[index] + 1
			q = append(q, index*2)
		}
	}

	fmt.Fprint(w, answerSlc[K])
}
