// package main
//
// import (
// 	"fmt"
// 	"sort"
// )
//
// func main() {
//
// 	var num_names int
// 	fmt.Scanf("%d\n", &num_names)
// 	var names []string = make([]string, num_names)
// 	for i := 0; i < num_names; i++ {
// 		fmt.Scanln(&names[i])
// 	}
// 	var num_nicks int
//
// 	fmt.Scanf("%d\n", &num_nicks)
// 	var nicks []string = make([]string, num_nicks)
// 	for i := 0; i < num_nicks; i++ {
// 		fmt.Scanln(&nicks[i])
// 	}
//     sort.Strings(names)
//     lcp := make([]int, num_names)
//     for i := 1; i < num_names; i++ {
//         j := 0
//         for ; len(names[i]) > j && len(names[i-1]) > j && names[i][j] == names[i-1][j]; j++ {
//
//         }
//         lcp[i] = j
//     }
//     fmt.Printf("%v\n", names)
//     fmt.Printf("%v\n", lcp)
//
//     for _,nick := range nicks {
//         bisect_and_count(names, lcp, nick)
//     }
// }
//
// func bisect_and_count(names []string, lcp []int, nick string){
//     l := 0;
//     r := len(names) - 1
//
//
//     for l <= r {
//         m := l + (r - 1) / 2
//         fmt.Printf("Comparing %s with name %s\n", nick, names[m])
//         fmt.Printf("mid: %d\n", m)
//         if len(nick) <= len(names[m]) && nick == names[m][0:len(nick)] {
//             fmt.Printf("%d\n",m)
//             return
//         } else if (nick < names[m][0:len(nick)]) {
//             r = m - 1
//         } else {
//             l = m - 1
//         }
//     }
// }
