# python 3.4.2
# Morse Code Dictionary
# make this able to process a dictionary from separate txt file
# TODO: add support for US, Continental (requires non-latin chars) and ITU MC varieties

#!usr/bin/python
# imported modules:
#import sys


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

# make entries keyError proof
#function that converts text to morse code    
def morsecodify(msg):
  msg = msg.upper() #convert message to uppercase
  morse = "" # dump characters here before print
  # convert each character in the message to morse 
  for character in msg:
      morse = morse + CODE[character] + " " # add to converted message + include space after char
  return morse

print ("Welcome to Morsecodify v0.1 - the simple text-to-morse code translator powered by Python v3")

print ('What would you like to do?\nType:\n(c) - Convert text to Morse code\n(e) - Exit')

# main menu
# m0 = input('Select option and press ENTER: ')
# add 3rd option - 'n' - display notes, info

"""
def validate_exit():
  if cont not in ('y', 'n'):
    cont = str(input("Would you like to convert another string? [y/n] ")
  return;
"""

def validate_choice(m0):
  if m0 == 'c':
      return True
  elif m0 == 'e':
      return True
  elif m0 != 'e' != 'c':
      print("Invalid Option! Press (c) to convert or (e) to exit.")
      return False

while True:
  try:
      m0 = str(input("Select option and press Enter: "))
      if validate_choice(m0):
        break
  except ValueError:
      print ("Invalid option!")

while True:
# add method to handle KeyError exceptions
  if m0 == 'c':
    msg = input("Input Text: ")
    morse = morsecodify(msg)
    print("Your Message in Morse Code:")
    print("\n" + morse + "\n")
    cont = str(input("Would you like to convert another string? [y/n] "))
#    validate_exit(cont)
  elif m0 == 'e':
    print('Bye!')
    exit()
  if cont == 'n':
    break
print('Bye!')
# sys.exit()
exit()

"""
comment out a block
"""

  
# add support for message-to-textfile exporting

