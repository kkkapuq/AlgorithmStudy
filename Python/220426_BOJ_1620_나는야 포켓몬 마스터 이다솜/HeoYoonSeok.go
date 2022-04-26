package main
import (
	"fmt"
	"bufio"
	"os"
	"strconv"

)


func main(){
	r := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)

	defer w.Flush()
	
	numMap := make(map[string]string)
	nameMap := make(map[string]string)
	
	var n, m int
	fmt.Fscan(r, &n, &m)
	
	var name string
	
	for i := 1; i < n + 1; i++{
		fmt.Fscan(r, &name)
		numMap[strconv.Itoa(i)] = name
		nameMap[name] = strconv.Itoa(i)
	}
	
	//fmt.Fprint(w, numMap)
	//fmt.Fprint(w, nameMap)
	
	
	for i := 0; i < m; i++{
		fmt.Fscan(r, &name)

		if name[0] == '0'|| name[0] == '1' || name[0] == '2' || name[0] == '3' || name[0] == '4' || name[0] == '5' || name[0] == '6' || name[0] == '7' || name[0] == '8' || name[0] == '9' {
			fmt.Fprintln(w, numMap[name])
		} else{
			fmt.Fprintln(w, nameMap[name])
		}
	}
	
}
