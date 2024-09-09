package main

import (
	"fmt"
	"math/rand"
)

func main() {
	numero := rand.Intn(10)

	fatorial := 1
	for i := 2; i <= numero; i++ {
		fatorial *= i
	}

	fmt.Printf("Numero gerado: %d\n", numero)
	fmt.Printf("Fatorial: %d\n", fatorial)
}
