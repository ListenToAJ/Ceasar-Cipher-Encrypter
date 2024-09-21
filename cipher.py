import sys

#~ USE: Python3 cipher.py {input_file} {shift_amount}
#~ EX:  Python3 cipher.py password.txt -3

input_file = sys.argv[1]
shift = int(sys.argv[2])

textIn = open(input_file, "r")
lines = textIn.read().splitlines()
textOut = open(input_file, "w")

#~ Actual character shifting
def caesar_cipher(letter, shift):
  
    if letter.isalpha():
        index = ord(letter.lower()) - ord('a')
        shifted_index = (index + shift) % 26
        shifted_letter = chr(shifted_index + ord('a'))

        if letter != letter.lower():
            shifted_letter = shifted_letter.upper()
        
        return shifted_letter
    elif letter.isdigit():
        index = ord(letter) - ord("0")
        shifted_index = (index + shift) % 10
        shifted_letter = chr(shifted_index + ord("0"))

        return shifted_letter
    else:
        return letter

#- For every line in text file
for i in range(len(lines)):
    encryptedLine = ""
    for c in lines[i]:
        newChar = caesar_cipher(c,shift)
        encryptedLine += newChar
    print(encryptedLine)
    encryptedLine += "\n"
    textOut.write(encryptedLine)