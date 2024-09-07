#include <stdio.h>

int main() {
    int quantidade;
    float preco_unitario, total;

    printf("Insira a quantidade de laranjas que deseja comprar: ");
    scanf("%d", &quantidade);

    if (quantidade >= 12) {
        preco_unitario = 0.65;
    } else {
        preco_unitario = 0.80;
    }

    total = quantidade * preco_unitario;

    printf("Preco da unidade: R$%.2f\n", preco_unitario);
    printf("Preco total: R$%.2f\n", total);

    return 0;
}
