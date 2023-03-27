# For longer binary numbers we XOR bit by bit: 0110 ^ 1010 = 1100. 
# We can XOR integers by first converting the integer from decimal to binary. 
# We can XOR strings by first converting each character to the integer representing the Unicode character.

# Given the string label, XOR each character with the integer 13. 
# Convert these integers back to a string and submit the flag as crypto{new_string}.
from Crypto.Util.number import *
st = "label"

a = [ord(i) for i in st]
b = [13^i for i in a] # XORing using the ^ operator
c = [chr(i) for i in b]
d = "crypto{" + ''.join(c) + "}"
print(d)


