#include <stdio.h>

int main() {
    int numero;

    printf("Insira um valor entre 0 e 50: ");
    scanf("%d", &numero);
    
    if (numero < 0 || numero > 50) {
        printf("Valor invalido!\n");
        return 0;
    }
    
    for (int i = numero - 1; i > 0; i--) {
        printf("Resto da divisao de %d por %d: %d\n", numero, i, numero % i);
    }

    return 0;
}
