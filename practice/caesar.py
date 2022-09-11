plaintext = input("plaintext:")
key = int(input("key:")) % 26

for c in plaintext:
    ch = (ord(c) + key) % (ord('Z') + 1)

    if ch < ord('A'):
        ch = ch + ord('A')

    print(chr(ch), end = '')