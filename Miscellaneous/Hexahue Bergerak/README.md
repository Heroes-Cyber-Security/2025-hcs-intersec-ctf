# Hexahue Bergerak

## Author

erzyyyy

## Difficulty
Easy

## Description

Selamat datang di Hexahue Bergerak!

Kalian akan berhadapan dengan Hexahue, sistem penulisan yang menyusun enam blok warna dalam kisi 2×3 untuk mewakili satu karakter.

Tapi challenge ini agak berbeda. Teks disembunyikan di dalam GIF animasi, di mana setiap frame merepresentasikan satu karakter Hexahue. Menerjemahkan satu per satu frame secara manual bakal makan waktu.

Masukkan teks yang kalian dapatkan ke dalam kurung kurawal dari HCS{...}
Flag terdiri dari huruf kecil, titik, dan angka.

Format flag : `HCS\{[a-z0-9\.]+\}`

### Hint (beri hint jika memang blm ad yg solve)

- Hint 1
  
mapping warna :
```
A: (pink, red,   green, yellow, blue,   sky)
B: (red,  pink,  green, yellow, blue,   sky)
C: (red,  green, pink,  yellow, blue,   sky)
D: (red,  green, yellow,pink,   blue,   sky)
E: (red,  green, yellow,blue,   pink,   sky)
F: (red,  green, yellow,blue,   sky,    pink)
G: (green,red,   yellow,blue,   sky,    pink)
H: (green,yellow,red,   blue,   sky,    pink)
I: (green,yellow,blue,  red,    sky,    pink)
J: (green,yellow,blue,  sky,    red,    pink)
K: (green,yellow,blue,  sky,    pink,   red)
L: (yellow,green,blue,  sky,    pink,   red)
M: (yellow,blue, green, sky,    pink,   red)
N: (yellow,blue, sky,   green,  pink,   red)
O: (yellow,blue, sky,   pink,   green,  red)
P: (yellow,blue, sky,   pink,   red,    green)
Q: (blue,  yellow,sky,  pink,   red,    green)
R: (blue,  sky,   yellow,pink,   red,    green)
S: (blue,  sky,   pink,  yellow, red,    green)
T: (blue,  sky,   pink,  red,    yellow, green)
U: (blue,  sky,   pink,  red,    green,  yellow)
V: (sky,   blue,  pink,  red,    green,  yellow)
W: (sky,   pink,  blue,  red,    green,  yellow)
X: (sky,   pink,  red,   blue,   green,  yellow)
Y: (sky,   pink,  red,   green,  blue,   yellow)
Z: (sky,   pink,  red,   green,  yellow, blue)

'.' : (black, white, white, black, black, white)
',' : (white, black, black, white, white, black)
' ' : (black, black, black, black, black, black) or (white, white, white, white, white, white)

'0': (black, gray,  white, black, gray,  white)
'1': (gray,  black, white, black, gray,  white)
'2': (gray,  white, black, black, gray,  white)
'3': (gray,  white, black, gray,  black, white)
'4': (gray,  white, black, gray,  white, black)
'5': (white, gray,  black, gray,  white, black)
'6': (white, black, gray,  gray,  white, black)
'7': (white, black, gray,  white, gray,  black)
'8': (white, black, gray,  white, black, gray )
'9': (black, white, gray,  white, black, gray )
```

- Hint 2
  
Buat automation pls

- Hint 3
  
pake ini tpi sedikit di tweak untuk support gif
https://github.com/kusuwada/hexahue

---

`HCS{woah.hexahue.adalah.alfabet.berwarna.c0y}`


