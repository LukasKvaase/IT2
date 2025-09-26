import coder as cd
from random import randint

inputText = str(input("\nWrite text here: "))
randomMax = 9999

randomKey = {
        "x": randint(randomMax*-1,randomMax),
        "y": randint(randomMax*-1,randomMax),
        "z": randint(randomMax*-1,randomMax)
        }

encodedText = cd.encode(inputText, randomKey)

print(f"\nEncoded text: \033[41m{encodedText}\033[0m\n")

print(f"Random key \033[42mx:{randomKey["x"]}, y:{randomKey["y"]}, z:{randomKey["z"]}\033[0m\n")

decodedTextRight = cd.decode(encodedText, randomKey)


print(f"\033[92mGiven right key: \033[42m{decodedTextRight}\033[0m")