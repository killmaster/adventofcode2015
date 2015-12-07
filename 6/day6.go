package main

import (
	"bufio"
	"fmt"
	"image"
	"image/color"
	"image/png"
	"log"
	"os"
	"strconv"
	"strings"
)

/* side size of the light grid */
const size int = 1000

func createImage(matrix *[size][size]int, filename string, maxintensity int) {
	var intensity uint8
	oldmin := 0
	oldmax := maxintensity
	oldrange := oldmax - oldmin
	newmin := 0
	newmax := 255
	newrange := newmax - newmin

	/*
	* canvas with the matrix size
	 */
	myimage := image.NewRGBA(image.Rectangle{image.Point{0, 0}, image.Point{size, size}})
	for x := 0; x < size; x++ {
		for y := 0; y < size; y++ {
			/*
			* normalize the values because color is 8bit
			 */
			newvalue := ((((*matrix)[x][y] - oldmin) * newrange) / (oldrange)) + newmin

			intensity = uint8(newvalue)
			c := color.RGBA{intensity, intensity, intensity, 255}
			myimage.Set(x, y, c)
		}
	}
	output, _ := os.Create(filename + ".png")
	png.Encode(output, myimage)
}

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

/*part one*/
func turnPart1(matrix *[size][size]int, status string,
	fromX int, fromY int,
	toX int, toY int) {
	var cell int
	if status == "on" {
		cell = 1
	} else {
		cell = 0
	}
	for x := fromX; x <= toX; x++ {
		for y := fromY; y <= toY; y++ {
			(*matrix)[x][y] = cell
		}
	}
}

func togglePart1(matrix *[size][size]int,
	fromX int, fromY int,
	toX int, toY int) {
	for x := fromX; x <= toX; x++ {
		for y := fromY; y <= toY; y++ {
			if (*matrix)[x][y] == 0 {
				(*matrix)[x][y] = 1
			} else {
				(*matrix)[x][y] = 0
			}
		}
	}
}

/*part2*/
func turnPart2(matrix *[size][size]int, status string,
	fromX int, fromY int,
	toX int, toY int) {
	var cell bool
	if status == "on" {
		cell = true
	} else {
		cell = false
	}
	for x := fromX; x <= toX; x++ {
		for y := fromY; y <= toY; y++ {
			if cell {
				(*matrix)[x][y]++
			} else {
				if (*matrix)[x][y] > 0 {
					(*matrix)[x][y]--
				}
			}
		}
	}
}

func togglePart2(matrix *[size][size]int,
	fromX int, fromY int,
	toX int, toY int) {
	for x := fromX; x <= toX; x++ {
		for y := fromY; y <= toY; y++ {
			(*matrix)[x][y] += 2
		}
	}
}

func main() {
	var matrixPart1 [size][size]int
	var matrixPart2 [size][size]int
	var startX, startY int
	var endX, endY int
	lines, err := readLines("day6input.txt")
	if err != nil {
		log.Fatalf("readLines: %s", err)
	}
	for _, line := range lines {
		command := strings.FieldsFunc(line, func(r rune) bool {
			return r == ' ' || r == ','
		})
		switch command[0] {
		case "turn":
			startX, _ = strconv.Atoi(command[2])
			startY, _ = strconv.Atoi(command[3])
			endX, _ = strconv.Atoi(command[5])
			endY, _ = strconv.Atoi(command[6])
			turnPart1(&matrixPart1, command[1], startX, startY, endX, endY)
			turnPart2(&matrixPart2, command[1], startX, startY, endX, endY)
		case "toggle":
			startX, _ = strconv.Atoi(command[1])
			startY, _ = strconv.Atoi(command[2])
			endX, _ = strconv.Atoi(command[4])
			endY, _ = strconv.Atoi(command[5])
			togglePart1(&matrixPart1, startX, startY, endX, endY)
			togglePart2(&matrixPart2, startX, startY, endX, endY)
		}
	}
	lights := 0
	brightness := 0
	maxintensityPart1 := 0
	maxintensityPart2 := 0

	for _, x := range matrixPart1 {
		for _, y := range x {
			if y == 1 {
				lights++
				if y > maxintensityPart1 {
					maxintensityPart1 = y
				}
			}
		}
	}
	for _, x := range matrixPart2 {
		for _, y := range x {
			brightness += y
			if y > maxintensityPart2 {
				maxintensityPart2 = y
			}
		}
	}

	createImage(&matrixPart1, "out1", maxintensityPart1)
	createImage(&matrixPart2, "out2", maxintensityPart2)
	fmt.Println("Part I result: ", lights)
	fmt.Println("Part II result: ", brightness)
}
