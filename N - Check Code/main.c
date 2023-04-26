#include <stdio.h>
#include <string.h>

int main() {
    int A, B;
    char S[100];
    scanf("%d %d %s", &A, &B, S);
    if (strlen(S) != A + B + 1 || S[A] != '-') {
        printf("No\n");
        return 0;
    }
    for (int i = 0; i < A + B + 1; i++) {
        if (i == A) continue;
        if (S[i] < '0' || S[i] > '9') {
            printf("No\n");
            return 0;
        }
    }
    printf("Yes\n");
    return 0;
}