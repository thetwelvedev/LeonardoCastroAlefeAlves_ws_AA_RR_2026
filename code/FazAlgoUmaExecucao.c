#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void FazAlgo(int n){

    volatile long soma = 0;

    int i,j,k;

    for(i=1;i<n-1;i++){
        for(j=i+1;j<=n;j++){
            for(k=1;k<=j;k++){

                soma += 1;

            }
        }
    }
}

long long calculaTempoNano(int n){

    struct timespec inicio, fim;

    clock_gettime(CLOCK_MONOTONIC, &inicio);

    FazAlgo(n);

    clock_gettime(CLOCK_MONOTONIC, &fim);

    return
      (fim.tv_sec - inicio.tv_sec) * 1000000000LL
      +
      (fim.tv_nsec - inicio.tv_nsec);
}

int main(){

    FILE *entrada;
    FILE *saida;

    int n;

    entrada = fopen("entrada.txt","r");

    if(entrada == NULL){
        printf("Erro ao abrir entrada.txt\n");
        return 1;
    }

    saida = fopen("resultados.txt","w");

    if(saida == NULL){
        printf("Erro ao criar resultados.txt\n");
        return 1;
    }

    fprintf(saida,"n,tempo_ns\n");

    while(fscanf(entrada,"%d",&n)==1){

        printf("Executando n=%d\n", n);

        long long tempo = calculaTempoNano(n);

        fprintf(saida,"%d,%lld\n", n, tempo);
    }

    fclose(entrada);
    fclose(saida);

    printf("Resultados gravados em resultados.txt\n");

    return 0;
}
