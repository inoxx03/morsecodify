# python 3.4.2
# Morse Code Dictionary
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

          ' ':'  ', '.':'.-.-.-', ',':'--..--',
          ':':'---...', '?':'..--..', "'":'.----.',
          '-':'-....-', '/':'-..-.', '@': '.--.-.',
          '=':'-...-', '(':'-.--.', ')':'-.--.-',
          '+':'.-.-.', '!': '-.-.--'
    }

print ("Welcome to Morsecodify, the simple text to morse code translator")

#function that converts text to morse code    
def morsecodify(msg):
  msg = msg.upper() #convert message to uppercase
  morse = ""
  # convert each character in the message to morse 
  for character in msg:
      morse = morse + CODE[character] + " " # add to converted message + include space after char
  return morse

msg = input("input message: ")
morse = morsecodify(msg)
print("/MSG START/ " + morse + "/MSG END/")

