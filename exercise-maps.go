package main

import (
	"fmt"
	"strings"
)

func WordCount(s string) {
	word := make(map[string]int)
	name := strings.Fields(s)
	for i := range name {
		if elem, ok := word[name[i]]; ok {
			word[name[i]] = elem + 1
		} else {
			word[name[i]] = 1
		}
	}
	fmt.Println(word)
}
func main() {
	WordCount("I ate a donut. Then I ate another donut.")
}
