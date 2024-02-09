def encrypt(text, s):
    result =""
    # transverse the plain
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        if (char.isupper()):
            # Encrypt lowercase characters in plain text
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result
text = input("Enter plain text: ")
s = int(input("Enter key: "))
print("Additive Cipher Text: "+encrypt(text, s))
enc = [[" " for i in range(len(encrypt(text, s)))] for j in range(s)]
flag = 0
row = 0
for i in range(len(encrypt(text, s))):
    enc[row][i] = encrypt(text, s)[i]
if row == 0:
    flag = 0
elif row == s-1:
    flag = 1
if flag == 0:
    row += 1
else:
    row -= 1
ct = []
for i in range(s):
    for j in range(len(encrypt(text, s))):
        if enc[i][j] != ' ':
            ct.append(enc[i][j])
cipher = "".join(ct)
print("Cipher Text: ", cipher)
