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

          ' ':'/', '.':'.-.-.-', ',':'--..--',
          ':':'---...', '?':'..--..', "'":'.----.',
          '-':'-....-', '/':'-..-.', '@': '.--.-.',
          '=':'-...-', '(':'-.--.', ')':'-.--.-',
          '+':'.-.-.'
    }
    
msg = input("input message: ")
msg = msg.replace(' ','')
msg = msg.upper()
#n = len(msg) - get string length/ not implemented

for letter in msg:
  print(CODE[letter])
