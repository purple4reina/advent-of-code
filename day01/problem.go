package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

const max = 2020

func main() {
	report, err := ioutil.ReadFile("expenses.txt")
	if err != nil {
		log.Fatal(err)
	}
	expenses := strings.Split(string(report), "\n")
	processed := make(map[int]bool, len(expenses))
	var twoFound, threeFound bool
	for _, expense := range expenses {
		if cost1, err := strconv.Atoi(expense); err == nil {
			if !twoFound {
				left := max - cost1
				if paid := processed[left]; paid {
					fmt.Println("two add to 2020:", left*cost1)
					twoFound = true
				}
			}
			if !threeFound {
				for cost2 := range processed {
					left := max - cost1 - cost2
					if paid := processed[left]; paid {
						fmt.Println("three add to 2020:", left*cost1*cost2)
						threeFound = true
						break
					}
				}
			}
			processed[cost1] = true
		}
	}
}
