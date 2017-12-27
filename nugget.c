#include <stdio.h>
#include <stdlib.h>

int nuggets(int *a, int n);

struct value {
    int len;
    int createdNuggets[][];
};

struct multiples {
    int len;
    int mods[];
}

int main(void) {
    int a = 7;
    int *p = &a;
    nuggets(p, 4);
}

int nuggets(int *a, int n) {
    int mod = *a;
    int *list = malloc(sizeof(int) * mod);
    for (int i = 0; i < mod; i++) {
        *(list + i) = 0;
    }

    for (int i = 0; i < n; i++) {
        int current = [a[i] % mod;
        if (list[current] == 0) {
            list[current] = a[i] / mod;
        }
    }

    int

    struct value modNum;
    modNum.createdNuggets = realloc(modNum.createdNuggets, size + 1);
    modNum.createdNuggets[modNum.size] = 










    for (int i = 0; i < n; i++) {
        printf("%i ", list[i]);
    }
    


    free(list);

}

int min(int a, int b) {
    if (a > b) {
        return b;
    }
    return a;
}