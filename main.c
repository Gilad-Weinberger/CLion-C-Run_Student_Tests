#include <stdio.h>

int main() {
    int num, sum = 0;

    while (scanf("%d", &num) == 1) {
        sum += num;
    }

    printf("%d\n", sum);
    return 0;
}
