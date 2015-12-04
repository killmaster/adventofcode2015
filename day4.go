package main

import (
	"crypto/md5"
	"fmt"
	"strconv"
)

var key = "yzbqklnj"

func main() {
	count := 1
	countString := strconv.Itoa(count)
	keyAnswer := key + countString
	hash := md5.Sum([]byte(keyAnswer))
	answer := fmt.Sprintf("%x", hash)

	for answer[0:6] != "000000" {
		count++
		countString := strconv.Itoa(count)
		keyAnswer = key + countString
		hash = md5.Sum([]byte(keyAnswer))
		answer = fmt.Sprintf("%x", hash)
	}

	fmt.Println("Result: ", count)
}
