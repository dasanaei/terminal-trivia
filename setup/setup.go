package main

import "os"

func main() {
	dir := "C:/%ProgramFiles%/trivia"
	CreateDirIfNotExist(dir)
}

func winSetup() {
	dir := "C:/%ProgramFiles%/trivia"
	if CreateDirIfNotExist(dir) {

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
