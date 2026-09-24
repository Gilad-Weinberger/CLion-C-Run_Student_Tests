#include <stdio.h>

int main() {
    int a, b;
    
    // Read two integers from standard input
    if (scanf("%d %d", &a, &b) == 2) {
        // Print the expected output format
        printf("Result: %d\n", a + b);
    }
    
    return 0;
}
