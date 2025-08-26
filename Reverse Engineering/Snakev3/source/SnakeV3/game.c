// clang --target=wasm32 -O3 -flto -nostdlib -o game.wasm -Wl,--no-entry -Wl,--export-all -Wl,--lto-O3 game.c

int score = 0;
unsigned int integrity = 0;
unsigned int seed = 0;

char encrypted_flag[] = {
    0x3f, 0x26, 0x3f, 0x18, 0x0d, 0x0c, 0x07, 0x26, 0x2b, 0x1c, 0x00, 0x12, 
    0x01, 0x17, 0x2c, 0x26, 0x1a, 0x28, 0x02, 0x1f, 0x18, 0x1f, 0x00
};

char key[] = "welcome_to_the_RE_club";

void init(unsigned int js_seed) {
  score = 0;
  seed = js_seed;
  integrity = seed;
}

void update_on_eat() {
  score += 9;
  integrity = ((integrity << 5) | (integrity >> 27)) ^ (seed + score);
}

void get_flag(char* buffer) {
  if (score == 999999 && integrity == 0x71800FC4) {
    for (int i = 0; i < sizeof(encrypted_flag); i++) {
      buffer[i] = encrypted_flag[i] ^ key[i];
    }
  } else {
    char fail[] = "hey, no ☝️ no ☝️ no ☝️ yah";
    for (int i = 0; i < sizeof(fail); i++) {
      buffer[i] = fail[i];
    }
  }
}
