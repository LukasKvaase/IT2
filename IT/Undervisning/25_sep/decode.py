import coder as cd
import re


encodedText = input("Encoded text: ")


keyText = input("key: ")

# Use regex to extract numbers
matches = re.findall(r'(-?\d+)', keyText)
x, y, z = map(int, matches)

print(f"x: {x}\ny: {y}\nz: {z}")

solveKey = {"x": x,"y": y,"z": z}


decodedTextRight = cd.decode(encodedText, solveKey)
print(f"Decoded: \033[42m{decodedTextRight}\033[0m")