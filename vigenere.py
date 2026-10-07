def shift_letter(letter, key_letter, direction=1):
    """Shifts a letter by the key letter. direction=1 encrypts, -1 decrypts."""
    base = ord("A")
    shift = ord(key_letter) - base                          # key letter as a number (A=0 ... Z=25)
    number = ord(letter) - base                             # message letter as a number (A=0 ... Z=25)
    return chr((number + direction * shift) % 26 + base)    # % 26 wraps around after Z


def vigenere(text, key, decrypt=False):
    """Encrypts or decrypts text with keyword. Non-letter are kept as they are."""
    key = key.upper()
    direction = -1 if decrypt else 1
    result = ""
    key_index = 0                                       # moves only when we use a letter
    for ch in text.upper():
        if "A" <= ch <= "Z":
            result += shift_letter(ch, key[key_index % len(key)], direction)
            key_index += 1
        else:
            result += ch                                 # spaces, numbers, punctuation
    return result

def main():
    while True:
        choice = input("(e)ncrypt, (d)ecrypt, or (q)uit: ").strip().lower()
        if choice == "q":
            break
        if choice not in ("e", "d"):
            print("Please choose e, d, or q.")
            continue
        text = input("Message: ")
        key = input("Key (letters only): ").strip()
        if not key.isascii() or not key.isalpha():
            print("Error: the key must contain only letters A-Z.")
            continue
        print("Result:", vigenere(text, key, decrypt=(choice == "d")))

if __name__ == "__main__":
    main()