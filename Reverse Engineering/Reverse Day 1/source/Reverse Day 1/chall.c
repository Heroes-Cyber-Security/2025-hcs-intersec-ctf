#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int a(void) {
    char *fake_flag = "HCS{faaakeeeflaaaaaaag}";
    return strlen(fake_flag);
}

void check(char *input) {
    // "HCS{reverse_is_eazyyyy}" encrypted bytes with XOR  
    unsigned char enc[] = {
        0x16, 0x1D, 0x0D, 0x25, 0x2C, 0x3B, 0x28, 0x3B, 
        0x2C, 0x2D, 0x3B, 0x01, 0x37, 0x2D, 0x01, 0x3B,
        0x3F, 0x24, 0x27, 0x27, 0x27, 0x27, 0x23
    };

    char key = 0x5E;  // XOR key "^"
    char flag[a() + 1];

    for (int i = 0; i < a(); i++) {
        flag[i] = enc[i] ^ key;
    }
    flag[a()] = '\0';

    for (int i = 0; i < a(); i++) {
        if (input[i] != flag[i]) {
            printf("Wrong!\n");
            exit(1);
        }
    }

    printf("GG!, dont forget to submit your flag!\n");
}
    
int main(int argc, char **argv) {
    if (argc != 2) {
        printf("Usage: %s <flag>\n", argv[0]);
        return 1;
    }

    if (strlen(argv[1]) != a()) {
        printf("Incorrect length!\n");
        return 1;
    }

    check(argv[1]);
    return 0;
}