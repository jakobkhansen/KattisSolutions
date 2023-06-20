package main

import "fmt"

func main() {
	var num_names int
	fmt.Scanf("%d\n", &num_names)
	fmt.Println(num_names)
	var names []string = make([]string, num_names)
	for i := 0; i < num_names; i++ {
		fmt.Scanln(&names[i])
	}
	fmt.Printf("%v\n", names)
	var num_nicks int

	fmt.Scanf("%d\n", &num_nicks)
	var nicks []string = make([]string, num_nicks)
	for i := 0; i < num_nicks; i++ {
		fmt.Scanln(&nicks[i])
	}
	fmt.Printf("%v\n", nicks)
	build_trie(names)
}

type node struct {
	children     map[byte]*node
	num_finished int
}

func (n node) String() string {
	out := "node{map{"
	for char, elem := range n.children {
		out += string(char)
		out += ": " + elem.String()
	}

	out += "}, " + fmt.Sprint(n.num_finished) + "}"

	return out
}

func build_trie(names []string) {
	root := node{children: map[byte]*node{}, num_finished: 0}
	for _, name := range names {
		recurse(&root, name)
	}
	fmt.Printf("%v\n", root)
}

func recurse(curr *node, name string) {

	fmt.Println(name)
	if len(name) == 0 {
		return
	}

	var prefix = name[0]
	if _, ok := curr.children[prefix]; !ok {
		fmt.Println("Creating child")
		new_child := node{children: map[byte]*node{}, num_finished: 0}
		curr.children[prefix] = &new_child
	}
	child := curr.children[prefix]
	child.num_finished += 1
	fmt.Printf("%v\n", child)
	recurse(child, name[1:])
}
