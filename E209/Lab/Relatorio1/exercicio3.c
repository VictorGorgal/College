#include <stdio.h>

void analisar_numeros(int numeros[5]) {
    int pares = 0;
    int impares = 0;
    int positivos = 0;
    int negativos = 0;

    for (int i = 0; i < 5; i++) {
        if (numeros[i] % 2 == 0) {
            pares++;
        } else {
            impares++;
        }

        if (numeros[i] > 0) {
            positivos++;
        } else if (numeros[i] < 0) {
            negativos++;
        }
    }

    printf("Quantidade de numeros pares: %d\n", pares);
    printf("Quantidade de numeros impares: %d\n", impares);
    printf("Quantidade de numeros positivos: %d\n", positivos);
    printf("Quantidade de numeros negativos: %d\n", negativos);
}

int main() {
    int n;

    printf("Insira a quantidade de testes: ");
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        int numeros[5];

        printf("Insira 5 numeros para o teste %d: ", i + 1);
        for (int j = 0; j < 5; j++) {
            scanf("%d", &numeros[j]);
        }

        analisar_numeros(numeros);
    }

    return 0;
}
