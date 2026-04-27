#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define EXECUCOES 13

void FazAlgoMelhor(int n){
    
    volatile long soma = 0;

    int i,j;

    

    for(int i = 1; i < n-1; i++){
        for(int j = i+1; j <= n; j++){
            soma += j;
        }
    }
}

long long calculaTempoNano(int n){

    struct timespec inicio,fim;

    clock_gettime(CLOCK_MONOTONIC,&inicio);

    FazAlgoMelhor(n);

    clock_gettime(CLOCK_MONOTONIC,&fim);

    long long tempo;

    tempo =
      (fim.tv_sec - inicio.tv_sec)*1000000000LL
      +
      (fim.tv_nsec - inicio.tv_nsec);

    return tempo;
}

double media11Valores(long long tempos[]){

    long long maior=tempos[0];
    long long menor=tempos[0];

    long long soma=0;

    for(int i=0;i<EXECUCOES;i++){

        if(tempos[i] > maior)
            maior = tempos[i];

        if(tempos[i] < menor)
            menor = tempos[i];

        soma += tempos[i];
    }

    soma = soma - maior - menor;

    return (double)soma/11.0;
}


int main(){

    FILE *entrada;
    FILE *saida;

    int n;

    long long tempos[EXECUCOES];

    entrada = fopen("entrada.txt","r");

    if(entrada==NULL){
        printf("Erro ao abrir entrada.txt\n");
        return 1;
    }

    saida = fopen("resultadosM.txt","w");

    if(saida==NULL){
        printf("Erro ao criar resultados.txt\n");
        return 1;
    }

    fprintf(saida,"n,media_ns\n");

    while(fscanf(entrada,"%d",&n)==1){

        printf("Executando n=%d\n",n);

        for(int i=0;i<EXECUCOES;i++){

            tempos[i]=calculaTempoNano(n);

        }

        double media = media11Valores(tempos);

        fprintf(saida,"%d,%.2f\n",n,media);

    }

    fclose(entrada);
    fclose(saida);

    printf("Resultados gravados em resultados.txt\n");

    return 0;
}
