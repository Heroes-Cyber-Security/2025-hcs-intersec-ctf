from PIL import Image, ImageSequence

# === Warna Standar ===
magenta = (255, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
blu = (0, 0, 255)
light_blue = (0, 255, 255)
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)

# === Kamus Hexahue ===
hexahue = {
    (magenta, red, green, yellow, blu, light_blue): 'a',
    (red, magenta, green, yellow, blu, light_blue): 'b',
    (red, green, magenta, yellow, blu, light_blue): 'c',
    (red, green, yellow, magenta, blu, light_blue): 'd',
    (red, green, yellow, blu, magenta, light_blue): 'e',
    (red, green, yellow, blu, light_blue, magenta): 'f',
    (green, red, yellow, blu, light_blue, magenta): 'g',
    (green, yellow, red, blu, light_blue, magenta): 'h',
    (green, yellow, blu, red, light_blue, magenta): 'i',
    (green, yellow, blu, light_blue, red, magenta): 'j',
    (green, yellow, blu, light_blue, magenta, red): 'k',
    (yellow, green, blu, light_blue, magenta, red): 'l',
    (yellow, blu, green, light_blue, magenta, red): 'm',
    (yellow, blu, light_blue, green, magenta, red): 'n',
    (yellow, blu, light_blue, magenta, green, red): 'o',
    (yellow, blu, light_blue, magenta, red, green): 'p',
    (blu, yellow, light_blue, magenta, red, green): 'q',
    (blu, light_blue, yellow, magenta, red, green): 'r',
    (blu, light_blue, magenta, yellow, red, green): 's',
    (blu, light_blue, magenta, red, yellow, green): 't',
    (blu, light_blue, magenta, red, green, yellow): 'u',
    (light_blue, blu, magenta, red, green, yellow): 'v',
    (light_blue, magenta, blu, red, green, yellow): 'w',
    (light_blue, magenta, red, blu, green, yellow): 'x',
    (light_blue, magenta, red, green, blu, yellow): 'y',
    (light_blue, magenta, red, green, yellow, blu): 'z',
    (black, white, white, black, black, white): '.',
    (white, black, black, white, white, black): ',',
    (white, white, white, white, white, white): ' ',
    (black, black, black, black, black, black): ' ',
    (black, gray, white, black, gray, white): '0',
    (gray, black, white, black, gray, white): '1',
    (gray, white, black, black, gray, white): '2',
    (gray, white, black, gray, black, white): '3',
    (gray, white, black, gray, white, black): '4',
    (white, gray, black, gray, white, black): '5',
    (white, black, gray, gray, white, black): '6',
    (white, black, gray, white, gray, black): '7',
    (white, black, gray, white, black, gray): '8',
    (black, white, gray, white, black, gray): '9',
}

# === Decode satu frame (PIL.Image object) ===
def decode_frame(img):
    try:
        img = img.convert("RGB")
        w, h = img.size
        block_w = w // 2
        block_h = h // 3
        colors = []

        for row in range(3):
            for col in range(2):
                x = col * block_w + block_w // 2
                y = row * block_h + block_h // 2
                rgb = img.getpixel((x, y))
                colors.append(rgb)

        return hexahue.get(tuple(colors), '?')
    except Exception as e:
        print(f"[!] Error decoding frame: {e}")
        return '?'

# === Decode semua frame dari GIF ===
def decode_gif(gif_path):
    try:
        img = Image.open(gif_path)
        result = ''
        for frame in ImageSequence.Iterator(img):
            char = decode_frame(frame)
            result += char
        return result
    except Exception as e:
        print(f"[!] Error reading GIF: {e}")
        return ''

# === Main ===
if __name__ == "__main__":
    gif_file = "HCS.gif"
    print("\n[+] Decoded Text:")
    print(decode_gif(gif_file))

