package main

import (
	"crypto/md5"
	"fmt"
	"strconv"
)

var key = "yzbqklnj"

func main() {
	count := 0
	for {
		count++
		countString := strconv.Itoa(count)
		keyAnswer := key + countString
		hash := md5.Sum([]byte(keyAnswer))
		answer := fmt.Sprintf("%x", hash)
		if answer[0:6] == "000000" {
			break
		}
	}
	fmt.Println("Result: ", count)
}
