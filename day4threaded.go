package main

import (
	"crypto/md5"
	"fmt"
	"strconv"
)

var key = "yzbqklnj"
var result = make(chan string, 10)

const max = 10000000
const maxWorkers = 10

func worker(id int, jobs <-chan int, result chan<- string) {
	for answer := range jobs {
		//fmt.Println("worker ", id, "hashing ", answer)
		answerString := strconv.Itoa(answer)
		keyAnswer := key + answerString
		hash := md5.Sum([]byte(keyAnswer))
		hashString := fmt.Sprintf("%x", hash)
		if hashString[0:6] == "000000" {
			result <- answerString
			break
		}
	}
}

func main() {
	jobs := make(chan int, max)
	result := make(chan string)

	for w := 0; w <= maxWorkers; w++ {
		go worker(w, jobs, result)
	}

	for j := 1; j <= max; j++ {
		jobs <- j
	}
	close(jobs)

	select {
	case msg1 := <-result:
		fmt.Println("Result: ", msg1)
	}
}
