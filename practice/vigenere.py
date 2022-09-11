plaintext = input("plaintext:")
key = input("key:")

key_idx = 0

for c in plaintext:
    k = ord(key[key_idx]) - ord('A')
    ch = (ord(c) + k) % (ord('Z') + 1)

    if ch < ord('A'):
        ch = ch + ord('A')

    print(chr(ch), end='')

    key_idx = (key_idx + 1) % len(key)