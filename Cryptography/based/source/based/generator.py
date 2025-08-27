import base64

def encode_custom(text: str) -> str:
    encoded_letters = []
    for char in text:
        b64_char = base64.b64encode(char.encode()).decode()
        encoded_letters.append(b64_char)
    
    concatenated = "".join(encoded_letters)
    
    for i in range(10):
	    concatenated = base64.b64encode(concatenated.encode()).decode()
    
    final_encoded = concatenated
    
    return final_encoded

if __name__ == "__main__":
    flag = "HCS{ju5t_b4s3_64_l0l}"
    encoded = encode_custom(flag)
    print(encoded)
