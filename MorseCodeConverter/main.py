import winsound
import time

morseCode = {
    "A": ".#_",
    "B": "_#.#.#.",
    "C": "_#.#_#.",
    "D": "_#.#.",
    "E": ".",
    "F": ".#.#_#.",
    "G": "_#_.",
    "H": ".#.#.#.",
    "I": ".#.",
    "J": ".#_#_#_",
    "K": "_#.#_",
    "L": ".#_#.#.",
    "M": "_#_",
    "N": "_#.",
    "O": "_#_#_",
    "P": ".#_#_#.",
    "Q": "_#_#.#_",
    "R": ".#_#.",
    "S": ".#.#.",
    "T": "_",
    "U": ".#.#_",
    "V": ".#.#.#_",
    "W": ".#_#_",
    "X": "_#.#.#_",
    "Y": "_#.#_#_",
    "Z": "_#_#.#.",
    "0": "_#_#_#_#_",
    "1": ".#_#_#_#_",
    "2": ".#.#_#_#_",
    "3": ".#.#.#_#_",
    "4": ".#.#.#.#_",
    "5": ".#.#.#.#.",
    "6": "_#.#.#.#.",
    "7": "_#_#.#.#.",
    "8": "_#_#_#.#.",
    "9": "_#_#_#_#.",
    ".": ".#_#.#_#.#_",
    ",": "_#_#.#.#_#_",
    "?": ".#.#_#_#.#."
}



entrada = input('Deixe sua mensagem: ')
strList = list(entrada.upper())
print(strList)
strMorse = ""
for i in range(len(strList)):
    if strList[i] == " ":
        strMorse += "%"
    elif strList[i] in morseCode:
        strMorse += morseCode.get(strList[i])
        if i == len(strList) - 1:
            strMorse += "@"
        else:
            strMorse += "&"
    else:
        raise AttributeError(f"Não foi possível converter a string para morse, caracter: {i}")
strSound = list(strMorse)
print(strSound)
DIT = 100

for sound in strSound:
        if sound == ".":
            winsound.Beep(500, DIT)
        elif sound == "_":
            winsound.Beep(500, DIT * 3)
        elif sound == "#":
           time.sleep((DIT/1000))
        elif sound == '&':
            time.sleep((DIT/1000) * 3)
        elif sound == '%':
            time.sleep((DIT/1000) * 7)

