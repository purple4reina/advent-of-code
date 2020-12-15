package main

import (
	"strconv"
	"strings"
	"testing"
)

func TestSolve(t *testing.T) {
	input := strings.Split(`mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1`, "\n")
	answer := Solve(input)
	if answer != 208 {
		t.Errorf("incorrect answer: expect=208, actual=%d", answer)
	}
}

func TestUpdateBit(t *testing.T) {
	testcases := []struct {
		input  string
		place  int64
		digit  int64
		expect string
	}{
		{
			input:  "111",
			place:  0,
			digit:  0,
			expect: "110",
		},
		{
			input:  "111",
			place:  1,
			digit:  0,
			expect: "101",
		},
		{
			input:  "111",
			place:  2,
			digit:  0,
			expect: "11",
		},
		{
			input:  "111",
			place:  3,
			digit:  0,
			expect: "111",
		},
		{
			input:  "111",
			place:  3,
			digit:  1,
			expect: "1111",
		},
		{
			input:  "100",
			place:  0,
			digit:  1,
			expect: "101",
		},
		{
			input:  "111",
			place:  0,
			digit:  1,
			expect: "111",
		},
		{
			input:  "100",
			place:  0,
			digit:  0,
			expect: "100",
		},
	}

	for _, test := range testcases {
		i, err := strconv.ParseInt(test.input, 2, 64)
		if err != nil {
			t.Fatal(err)
		}
		updated := updateBit(i, test.place, test.digit)
		actual := strconv.FormatInt(updated, 2)
		if actual != test.expect {
			t.Errorf("incorrect bits flipped: expected=%s actual=%s", test.expect, actual)
		}
	}
}
