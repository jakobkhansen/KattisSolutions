package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	s, _ := reader.ReadString('\n')

	num_names, _ := strconv.Atoi(s[:len(s)-1])

	var names []string = make([]string, num_names)
	for i := 0; i < num_names; i++ {
		names[i], _ = reader.ReadString('\n')
		names[i] = names[i][:len(names[i])-1]
	}

	t, _ := reader.ReadString('\n')
	num_nicks, _ := strconv.Atoi(t[:len(t)-1])

	var nicks []string = make([]string, num_nicks)
	for i := 0; i < num_nicks; i++ {
		nicks[i], _ = reader.ReadString('\n')
		nicks[i] = nicks[i][:len(nicks[i])-1]
	}
	root := build_trie(names)

	for _, nick := range nicks {
		result := access_trie(root, nick)
		if result == nil {
			fmt.Printf("0\n")
		} else {
			fmt.Printf("%d\n", result.num_finished)
		}
	}
}

type node struct {
	children     map[byte]*node
	num_finished int
}

func build_trie(names []string) *node {
	root := node{children: map[byte]*node{}, num_finished: 0}
	for _, name := range names {
		recurse(&root, name)
	}
	return &root
}

func recurse(curr *node, name string) {

	if len(name) == 0 {
		return
	}

	var prefix = name[0]
	if _, ok := curr.children[prefix]; !ok {
		new_child := node{children: map[byte]*node{}, num_finished: 0}
		curr.children[prefix] = &new_child
	}
	child := curr.children[prefix]
	child.num_finished += 1
	recurse(child, name[1:])
}

func access_trie(root *node, name string) *node {
	curr := root
	index := 0
	for index < len(name) {
		child, ok := curr.children[name[index]]
		if !ok {
			return nil
		}
		curr = child
		index++
	}

	return curr
}
