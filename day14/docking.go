package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

func ParseMask(line string) (int64, int64) {
	line = strings.Split(line, " = ")[1]

	andMaskStr := strings.Replace(line, "X", "1", -1)
	andMask, err := strconv.ParseInt(andMaskStr, 2, 64)
	if err != nil {
		log.Fatal(err)
	}

	orMaskStr := strings.Replace(line, "X", "0", -1)
	orMask, err := strconv.ParseInt(orMaskStr, 2, 64)
	if err != nil {
		log.Fatal(err)
	}
	return andMask, orMask
}

func ParseAssignment(line string) (int64, int64) {
	split := strings.Split(line, " = ")
	numStr := split[1]
	memStr := split[0]
	memStr = strings.Trim(memStr, "mem[]")

	mem, err := strconv.ParseInt(memStr, 10, 64)
	if err != nil {
		log.Fatal(err)
	}

	num, err := strconv.ParseInt(numStr, 10, 64)
	if err != nil {
		log.Fatal(err)
	}
	return mem, num
}

func Solve(input []string) int64 {
	mem := make([]int64, 1000000)
	var andMask, orMask int64
	for _, line := range input {
		if strings.HasPrefix(line, "mask") {
			andMask, orMask = ParseMask(line)
		} else {
			i, val := ParseAssignment(line)
			mem[i] = val&andMask | orMask
		}
	}
	var sum int64
	for _, val := range mem {
		sum += val
	}
	return sum
}

func main() {
	data, err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	answer := Solve(strings.Split(string(data), "\n"))
	fmt.Println(answer)
}
