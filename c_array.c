#include <stdio.h>
#include <stdlib.h>

typedef struct array
{
    int size;
    int* begin;
}array;

array createArray(int size){
    array arr;
    arr.size = size;
    arr.begin = (int*)malloc(sizeof(int)*arr.size);
    return arr;
}

void freeArray(array arr){
    free(arr.begin);
}

int main(){
    array arr;
    arr = createArray(5);
    arr.begin[0] = 1;
    arr.begin[1] = 2;
    printf("%d\n",arr.begin[0]);
    printf("%d\n",arr.begin[1]);
    freeArray(arr);
    printf("%d\n",arr.begin[0]);
    printf("%d",arr.begin[1]);
}