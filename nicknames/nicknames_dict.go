// package main
//
// import (
// 	"bufio"
// 	"fmt"
// 	"os"
// 	"strconv"
// )
//
// func main() {
//
// 	reader := bufio.NewReader(os.Stdin)
// 	s, _ := reader.ReadString('\n')
//
// 	num_names, _ := strconv.Atoi(s[:len(s)-1])
//
// 	var names []string = make([]string, num_names)
// 	for i := 0; i < num_names; i++ {
//
// 		names[i], _ = reader.ReadString('\n')
// 		names[i] = names[i][:len(names[i])-1]
// 	}
//
// 	t, _ := reader.ReadString('\n')
// 	num_nicks, _ := strconv.Atoi(t[:len(t)-1])
//
// 	var nicks []string = make([]string, num_nicks)
// 	for i := 0; i < num_nicks; i++ {
// 		nicks[i], _ = reader.ReadString('\n')
// 		nicks[i] = nicks[i][:len(nicks[i])-1]
// 	}
//
// 	prefixes := map[string]int{}
//
// 	for _, name := range names {
// 		for i := 1; i <= len(name); i++ {
// 			prefixes[name[0:i]]++
// 		}
// 	}
//
// 	for _, nick := range nicks {
// 		fmt.Printf("%d\n", prefixes[nick])
//
// 	}
//
// }
