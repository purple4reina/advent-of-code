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

	orMaskStr := strings.Replace(line, "X", "0", -1)
	orMask, err := strconv.ParseInt(orMaskStr, 2, 64)
	if err != nil {
		log.Fatal(err)
	}

	chaosMaskStr := strings.Replace(line, "1", "0", -1)
	chaosMaskStr = strings.Replace(chaosMaskStr, "X", "1", -1)
	chaosMask, err := strconv.ParseInt(chaosMaskStr, 2, 64)
	if err != nil {
		log.Fatal(err)
	}

	return orMask, chaosMask
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

func updateBit(i, p, d int64) int64 {
	var mask int64 = 1 << p
	return (i & ^mask) | ((d << p) & mask)
}

func applyChaos(i, mask, val int64, mem map[int64]int64) {
	indexes := []int64{i}
	var p int64
	for mask > 0 {
		bit := mask & 1
		p++

		if bit == 1 {
			var newIndexes []int64
			for _, i := range indexes {
				newIndexes = append(newIndexes, updateBit(i, p, 0))
				newIndexes = append(newIndexes, updateBit(i, p, 1))
			}
			indexes = newIndexes
		}
		mask >>= 1
	}
	for _, i := range indexes {
		mem[i] = val
	}
}

func Solve(input []string) int64 {
	mem := make(map[int64]int64)
	var orMask, chaosMask int64
	for _, line := range input {
		if strings.HasPrefix(line, "mask") {
			orMask, chaosMask = ParseMask(line)
		} else {
			i, val := ParseAssignment(line)
			i |= orMask
			applyChaos(i, chaosMask, val, mem)
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
