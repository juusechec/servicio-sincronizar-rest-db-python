package main

import (
	"bytes"
	"fmt"
	"github.com/robfig/cron"
	"log"
	"os"
	"os/exec"
	"strings"
	"time"
)

func execScript() {
	os.Chdir("C:\\Python27\\ArcGIS10.4")
	cmd := exec.Command(".\\python.exe", "E:\\Users\\jorge\\Documents\\acueducto\\servicio\\sincronizar.py")
	cmd.Stdin = strings.NewReader("some input")
	var out bytes.Buffer
	cmd.Stdout = &out
	err := cmd.Start()
	if err != nil {
		log.Fatal(err)
	}
	//fmt.Printf("in all caps: %q\n", out.String())
	go func() {
		fmt.Println("Se inicia comando...")
		for {
			fmt.Print(out.String())
			out.Reset() // clean out
			time.Sleep(1 * time.Second)
		}
	}()
	err = cmd.Wait()
	if err != nil {
		log.Printf("Command finished with error: %v", err)
	}
  fmt.Println(out.String())
  time.Sleep(10 * time.Second)
	fmt.Println("\n\nTerminó...\n\n")
}

func main() {
  //execScript()
  fmt.Println("Se carga servicio CRON... https://godoc.org/github.com/robfig/cron")
	c := cron.New()
	c.AddFunc("0 0 12 * * *", execScript)
	c.Start()
  for {
  }
}
