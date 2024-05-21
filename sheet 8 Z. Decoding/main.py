def decode_polycarp_encoding(size, word):
    result = ""
    i = 0
    while size > 0:
        if size % 2 == 0:
            result = word[i] + result
        else:
            result = result + word[i]
        i += 1
        size -= 1
    return result

# Read input
size = int(input())
word = input().strip()

# Decode the encoded message
decoded_word = decode_polycarp_encoding(size, word)
print(decoded_word)
