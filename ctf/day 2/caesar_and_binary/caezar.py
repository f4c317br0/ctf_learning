
def caesar_encrypt(text):
    for x in range(1, 26):
        result = ""
        for char in text:
            if 'a' <= char <= 'z':
                char_position = ord(char) - ord('a')
                new_char_position = (char_position + x) % 26
                result += chr(new_char_position + ord('a'))
            elif 'A' <= char <= 'Z':
                char_position = ord(char) - ord('A')
                new_char_position = (char_position + x) % 26
                result += chr(new_char_position + ord('A'))
            else:
                result += char

        print(f"Сдвиг {x}: {result}")


def caesar_decrypt(cipher_text):
    for x in range(1, 26):
        result = ""
        for char in cipher_text:
            if 'a' <= char <= 'z':
                char_position = ord(char) - ord('a')
                new_char_position = (char_position - x) % 26
                result += chr(new_char_position + ord('a'))
            elif 'A' <= char <= 'Z':
                char_position = ord(char) - ord('A')
                new_char_position = (char_position - x) % 26
                result += chr(new_char_position + ord('A'))
            else:
                result += char

        print(f"Сдвиг {x}: {result}")


text = 'YidhR3BvYTJ4MFpudHFhR3g2YUhsZmF6TnFlVGwzWVROclh6bHJiVEJxYld4b2ZRPT0nCg=='
time1 = b'aGpoa2x0ZntqaGx6aHlfazNqeTl3YTNrXzlrbTBqbWxofQ=='
time2 = 'hjhkltf{jhlzhy_k3jy9wa3k_9km0jmlh}'
caesar_decrypt(time2)