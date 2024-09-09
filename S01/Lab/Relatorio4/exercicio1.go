package main

import (
	"fmt"
	"math"
)

func main() {
	var a, b, c float64

	fmt.Print("Insira o A: ")
	fmt.Scanln(&a)

	fmt.Print("Insira o B: ")
	fmt.Scanln(&b)

	fmt.Print("Insira o C: ")
	fmt.Scanln(&c)

	delta := b*b - 4*a*c

	if delta > 0 {
		raiz1 := (-b + math.Sqrt(delta)) / (2 * a)
		raiz2 := (-b - math.Sqrt(delta)) / (2 * a)
		fmt.Printf("x1 = %.2f, x2 = %.2f\n", raiz1, raiz2)
	} else if delta == 0 {
		raiz := -b / (2 * a)
		fmt.Printf("x1 = x2 = %.2f\n", raiz)
	} else {
		fmt.Println("Nao existe raizes reais")
	}
}
