package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

var logic = map[string]func() uint16{}
var cache = map[string]uint16{}

func readLines(path string) ([]string, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines, scanner.Err()
}

func lookup(s string) uint16 {
	if n, ok := cache[s]; ok {
		return n
	}

	if n, err := strconv.Atoi(s); err == nil {
		cache[s] = uint16(n)
		return uint16(n)
	}

	n := logic[s]()
	cache[s] = n
	return n
}

func main() {
	lines, err := readLines("day7input.txt")
	if err != nil {
		log.Fatalf("readLines: %s", err)
	}
	for _, line := range lines {
		command := strings.FieldsFunc(line, func(r rune) bool {
			return r == ' ' || r == '-' || r == '>'
		})
		switch command[1] {
		case "AND":
			logic[command[3]] = func() uint16 { return lookup(command[0]) & lookup(command[2]) }
		case "OR":
			logic[command[3]] = func() uint16 { return lookup(command[0]) | lookup(command[2]) }
		case "LSHIFT":
			logic[command[3]] = func() uint16 { return lookup(command[0]) << lookup(command[2]) }
		case "RSHIFT":
			logic[command[3]] = func() uint16 { return lookup(command[0]) >> lookup(command[2]) }
		default:
			switch command[0] {
			case "NOT":
				logic[command[2]] = func() uint16 { return ^lookup(command[1]) }
			default:
				logic[command[1]] = func() uint16 { return lookup(command[0]) }
			}
		}
	}
	a := lookup("a")
	fmt.Println("Part 1 result:", a)

	logic["b"] = func() uint16 { return a }
	cache = map[string]uint16{}
	a = lookup("a")
	fmt.Println("Part 2 result:", a)
}
