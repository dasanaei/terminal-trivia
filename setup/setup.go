package main

import (
	"fmt"
	"io"
	"os"
	"os/exec"
	"path/filepath"
	"strings"
)

func main() {
	winSetup()
}

func winSetup() {
	homeDir, _ := os.UserHomeDir()
	triviaDir := homeDir + "/astral-kuarry/trivia"
	dataDir := triviaDir + "/data"
	ex, err := os.Executable()
	if err != nil {
		panic(err)
	}
	exPath := filepath.Dir(ex)
	dist := strings.Replace(exPath, "setup", "dist", -1)
	data := strings.Replace(exPath, "setup", "data", -1)
	CreateDirIfNotExist(triviaDir)
	CreateDirIfNotExist(dataDir)
	CopyDir(dist, triviaDir)
	CopyDir(data, dataDir)
	oldLocation := dist + "/terminal-trivia.exe"
	newLocation := homeDir + "/trivia.exe"
	desktop := homeDir + "/Desktop/terminal-trivia.exe"
	CopyFile(oldLocation, newLocation)
	CopyFile(oldLocation, desktop)
}

func getCommandOutput(cmd *exec.Cmd) string {
	out, err := cmd.CombinedOutput()
	result := string(out)
	if err != nil {
		result += err.Error()
	}
	return result
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

func CopyFile(source string, dest string) (err error) {
	sourcefile, err := os.Open(source)
	if err != nil {
		return err
	}

	defer sourcefile.Close()

	destfile, err := os.Create(dest)
	if err != nil {
		return err
	}

	defer destfile.Close()

	_, err = io.Copy(destfile, sourcefile)
	if err == nil {
		sourceinfo, err := os.Stat(source)
		if err != nil {
			err = os.Chmod(dest, sourceinfo.Mode())
		}

	}

	return
}

func CopyDir(source string, dest string) (err error) {

	// get properties of source dir
	sourceinfo, err := os.Stat(source)
	if err != nil {
		return err
	}

	// create dest dir

	err = os.MkdirAll(dest, sourceinfo.Mode())
	if err != nil {
		return err
	}

	directory, _ := os.Open(source)

	objects, err := directory.Readdir(-1)

	for _, obj := range objects {

		sourcefilepointer := source + "/" + obj.Name()

		destinationfilepointer := dest + "/" + obj.Name()

		if obj.IsDir() {
			// create sub-directories - recursively
			err = CopyDir(sourcefilepointer, destinationfilepointer)
			if err != nil {
				fmt.Println(err)
			}
		} else {
			// perform copy
			CopyFile(sourcefilepointer, destinationfilepointer)
			if err != nil {
				fmt.Println(err)
			}
		}

	}
	return
}
