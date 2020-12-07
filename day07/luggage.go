package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strings"
)

type bag struct {
	name    string
	parents []*bag
}

func (b *bag) countParents() (parents int) {
	found := make(map[string]struct{})
	search(b, found)
	return len(found)
}

func search(b *bag, found map[string]struct{}) {
	for _, p := range b.parents {
		found[p.name] = struct{}{}
		search(p, found)
	}
}

type bagManager map[string]*bag

func (m bagManager) getBag(name string) *bag {
	b, ok := m[name]
	if !ok {
		b = &bag{
			name: name,
		}
		m[name] = b
	}
	return b
}

func main() {
	data, err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	answer := getParents(string(data))
	fmt.Println(answer)
}

func getParents(data string) int {
	bm := make(bagManager)

	for _, b := range strings.Split(data, "\n") {
		pc := strings.SplitN(b, "bags contain", 2)

		parent := strings.Trim(pc[0], " ")
		pb := bm.getBag(parent)

		for _, c := range strings.Split(strings.Trim(pc[1], " "), ", ") {
			c = strings.Trim(c, ".")
			c = strings.Trim(c, "s")
			c = strings.Replace(c, " bag", "", 1)
			c = strings.SplitN(c, " ", 2)[1]

			cb := bm.getBag(c)

			cb.parents = append(cb.parents, pb)
		}
	}

	return bm.getBag("shiny gold").countParents()
}
