#include <stdio.h>

int calcIterations(int n);

int main() {

    int n = getchar() - '0';

    printf("%d\n", calcIterations(n));
}

int calcIterations(int n) {
    return (n+n+1)*(n+n+1);
}
