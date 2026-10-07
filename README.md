# Vigenere Cipher (Python)

A command-line tool that encrypts and decrypts text using the Vigenere cipher, a classical polyalphabetic substitution cipher. Built as a beginner Python project.

## Features
- Encrypt or decrypt a message using a keyword
- The keyword repeats along the message
- Spaces, numbers and punctuation stay unchanged
- Input is case-insensitive; output is in uppercase
- Shows an error if the key contains anything other than letters
- Includes tests using `assert`

## How it works
Each letter is converted to a number (A=0, B=1, ... Z=25). To encrypt, the number of each message letter is added to the number of the matching key letter, then wrapped around with `% 26`. To decrypt, the key number is subtracted instead.

Example with the key `KEY`:

```
Message:  H  E  L  L  O
Key:      K  E  Y  K  E
Result:   R  I  J  V  S
```

The key only moves forward on letters, so spaces and punctuation don't use up key letters.

## Requirements
- Python 3.6 or newer (no extra libraries needed)

## How to run
```
python vigenere.py
```

Choose `e` to encrypt, `d` to decrypt or `q` to quit, then enter a message and a key.

## Example
```
(e)ncrypt, (d)ecrypt, or (q)uit: e
Message: HELLO
Key (letters only): KEY
Result: RIJVS

(e)ncrypt, (d)ecrypt, or (q)uit: d
Message: RIJVS
Key (letters only): KEY
Result: HELLO
```

Invalid key:
```
Key (letters only): K3Y
Error: the key must contain only letters A-Z.
```

## Run the tests
```
python test_vigenere.py
```
If everything works, it prints `All tests passed`.

## Project structure
```
VigenereCipher/
├── vigenere.py        # cipher logic and command-line menu
├── test_vigenere.py   # tests using assert
├── .gitignore         # ignores __pycache__
└── README.md
```

## What I learned
- `ord()` and `chr()` convert between letters and numbers, so I can do math on letters.
- `% 26` wraps the alphabet around, so Z followed by a shift of 1 goes back to A.
- `enumerate`-style thinking and a `key_index` counter help repeat the key along the message.
- A wrongly indented `return` inside a loop can stop a function after one letter. Testing helped me find and fix it.
- Splitting the code into functions (`shift_letter`, `vigenere`, `main`) keeps the logic separate from input and output and makes it easy to test.

## Limitations
The Vigenere cipher is a historical cipher and is **not secure** for real-world use. It can be broken with frequency analysis. This project is for learning how classical encryption works.