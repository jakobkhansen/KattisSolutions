package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type SymbolTable struct {
	scopes      []Scope
	lastDefined map[string]int
}

func NewSymbolTable() *SymbolTable {
	var st SymbolTable
	st.scopes = make([]Scope, 10)
	st.lastDefined = make(map[string]int)
	return &st
}

func (st *SymbolTable) query(variable string) (string, bool) {
	lastDef, defined := st.lastDefined[variable]
	if !defined {
		return "", false
	}
	var startPos int
	if lastDef < len(st.scopes)-1 {
		startPos = lastDef
	} else {
		startPos = len(st.scopes) - 1
	}
	var val string
	var ok bool
	for i := startPos; i >= 0; i-- {
		val, ok = st.scopes[i].symbolTypes[variable]
		if ok {
			return val, ok
		}
	}
	return val, ok
}

func (st *SymbolTable) queryCurrentScope(variable string) (string, bool) {
	val, ok := st.scopes[len(st.scopes)-1].symbolTypes[variable]
	return val, ok
}
func (st *SymbolTable) insert(variable string, tp string) {
	st.lastDefined[variable] = len(st.scopes) - 1
	st.scopes[len(st.scopes)-1].symbolTypes[variable] = tp
}

func (st *SymbolTable) newScope() {
	symTable.scopes = append(symTable.scopes, Scope{symbolTypes: make(map[string]string)})
}

func (st *SymbolTable) popScope() {
	symTable.scopes = symTable.scopes[:len(symTable.scopes)-1]
}

type Scope struct {
	symbolTypes map[string]string
}

var symTable *SymbolTable

func main() {

	reader := bufio.NewReader(os.Stdin)
	s, _ := reader.ReadString('\n')
	n, _ := strconv.Atoi(s[:len(s)-1])
	symTable = NewSymbolTable()
	symTable.newScope()

	for i := 0; i < n; i++ {
		l, _ := reader.ReadString('\n')
		l = l[:len(l)-1]
		line := strings.Split(l, " ")
		cmd := line[0]
		// fmt.Println(cmd)

		switch cmd {
		case "TYPEOF":
			id := line[1]
			query(id)
			break
		case "DECLARE":
			id := line[1]
			tp := line[2]
			declare(id, tp)
			break
		case "{":
			enterScope()
			break
		case "}":
			exitScope()
			break

		}
		// fmt.Printf("%+v\n", symTable)
	}
}

func query(id string) {
	val, ok := symTable.query(id)
	if !ok {
		fmt.Println("UNDECLARED")
	} else {
		fmt.Println(val)
	}
}

func declare(id string, tp string) {
	_, exists := symTable.queryCurrentScope(id)
	if exists {
		fmt.Println("MULTIPLE DECLARATION")
		os.Exit(0)
	}
	symTable.insert(id, tp)
}

func enterScope() {
	symTable.newScope()
}

func exitScope() {
	symTable.popScope()
}
