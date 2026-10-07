from vigenere import vigenere

assert vigenere("HELLO", "KEY") == "RIJVS"
assert vigenere("ATTACKATDAWN", "LEMON") == "LXFOPVEFRNHR"
assert vigenere("RIJVS", "KEY", decrypt=True) == "HELLO"
assert vigenere("Hi, there!", "abc") == "HJ, VHFTE!"
print("All tests passed")