package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

var (
	w = bufio.NewWriter(os.Stdout)
	r = bufio.NewReader(os.Stdin)
)

func main() {

	defer w.Flush()

	var N, M, V int

	fmt.Fscan(r, &N, &M, &V)
	graph := make([][]int, N+1)

	for i := 0; i < M; i++ {
		var s, e int
		fmt.Fscan(r, &s, &e)
		graph[s] = append(graph[s], e)
		graph[e] = append(graph[e], s)

	}
	dfs(graph, V, N)
	fmt.Fprint(w, "\n")
	bfs(graph, V, N)

}

func dfs(graph [][]int, start int, n int) []int {

	answer := make([]int, 0)
	visit := make([]int, n+1)
	s := make([]int, 0)
	s = append(s, start)

	for len(s) > 0 {
		node := s[len(s)-1]
		s = s[:len(s)-1]
		if visit[node] == 1 {
			continue
		}
		fmt.Fprintf(w, "%d ", node)
		answer = append(answer, node)
		visit[node] = 1

		child := make([]int, 0)
		child = graph[node]
		sort.Sort(sort.Reverse(sort.IntSlice(child)))
		for i := 0; i < len(child); i++ {
			if visit[child[i]] == 0 {
				s = append(s, child[i])
			}
		}
	}

	return answer
}

func bfs(graph [][]int, start int, n int) []int {

	answer := make([]int, 0)
	visit := make([]int, n+1)
	q := make([]int, 0)
	q = append(q, start)

	for len(q) > 0 {
		node := q[0]
		q = q[1:]
		if visit[node] == 1 {
			continue
		}
		fmt.Fprintf(w, "%d ", node)
		answer = append(answer, node)
		visit[node] = 1

		child := make([]int, 0)
		child = graph[node]
		sort.Ints(child)
		for i := 0; i < len(child); i++ {
			if visit[child[i]] == 0 {
				q = append(q, child[i])
			}
		}
	}

	return answer
}
