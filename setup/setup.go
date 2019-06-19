package main

import (
	"fmt"
	"os"
)

func main() {
	winSetup()
	fmt.Printf("TEST")
}

func winSetup() {
	dir, _ := os.UserHomeDir()
	dir = dir + "\\astral-kuarry"
	fmt.Println(dir)
	if CreateDirIfNotExist(dir) {
		fmt.Print("sucess")
	}
}

//CreateDirIfNotExist does exactly what it says
func CreateDirIfNotExist(dir string) bool {
	if _, err := os.Stat(dir); os.IsNotExist(err) {
		err = os.MkdirAll(dir, 0755)
		if err != nil {
			panic(err)
		}
		return true
	}
	return false
}
