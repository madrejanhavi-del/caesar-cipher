text = input("Enter your message: ")
shift = int(input("Enter shift value: "))
encrypted = ""

for char in text:
    if char.isalpha():
        start = ord('A') if char.isupper() else ord('a')
        new_char = chr((ord(char) - start + shift) % 26 + start)
        encrypted += new_char
    else:
        encrypted += char

print("\n---------- CAESAR CIPHER ----------")
print("Original message:", text)
print("Encrypted message:", encrypted)
decrypted = ""

for char in encrypted:
    if char.isalpha():
        start = ord('A') if char.isupper() else ord('a')
        new_char = chr((ord(char) - start - shift) % 26 + start)
        decrypted += new_char
    else:
        decrypted += char

print("Decrypted message:", decrypted)