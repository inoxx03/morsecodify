# python 3.4.2
# Morse Code Dictionary
# make this able to process a dictionary from separate txt file
# TODO: add support for US, Continental (requires non-latin chars) and ITU MC varieties
CODE = {'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..', 'E': '.',
          'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',  'J': '.---', 
          'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',  'O': '---', 
          'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...', 'T': '-',
          'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--', 
          'Z': '--..',

          '0': '-----',  '1': '.----',  '2': '..---',
          '3': '...--',  '4': '....-',  '5': '.....',
          '6': '-....',  '7': '--...',  '8': '---..',
          '9': '----.',

          ' ':' ', '.':'.-.-.-', ',':'--..--',
          ':':'---...', '?':'..--..', "'":'.----.',
          '-':'-....-', '/':'-..-.', '@': '.--.-.',
          '=':'-...-', '(':'-.--.', ')':'-.--.-',
          '+':'.-.-.', '!': '-.-.--'
    }

print ("Welcome to Morsecodify v0.1 - the simple text-to-morse code translator powered by Python v3")

#function that converts text to morse code    
def morsecodify(msg):
  msg = msg.upper() #convert message to uppercase
  morse = ""
  # convert each character in the message to morse 
  for character in msg:
      morse = morse + CODE[character] + " " # add to converted message + include space after char
  return morse

msg = input("Input Text: ")
morse = morsecodify(msg)
print("Your Message in Morse Code:")
print("/MSG START/ " + morse + "/MSG END/")

# code here to choose if quit or another input

