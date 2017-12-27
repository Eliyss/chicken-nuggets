#include <stdio.h>
#include <stdlib.h>

struct value {
    int len;
    int createdNuggets[0][0];
};

struct multiples {
    int len;
    int mods[0];
};

int main(void) {
    struct multiples *zero = malloc(sizeof(*zero) + 4*sizeof(int));
    zero->mods[0] = 0;
    zero->mods[1] = 1;
    zero->mods[2] = 2;
    zero->mods[3] = 3;
    struct multiples *one = malloc(sizeof(*one) + 3*sizeof(int));
    one->mods[0] = 10;
    one->mods[1] = 11;
    one->mods[2] = 12;
    struct value *nuggets = malloc(sizeof(*nuggets) + 2*sizeof(int));
    nuggets->len = 2;
    nuggets->createdNuggets[0] = zero->mods;
    nuggets->createdNuggets[1] = one->mods;
    printf("%i ", nuggets->createdNuggets[0][1]);


    
}