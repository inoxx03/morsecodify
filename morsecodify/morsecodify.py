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

def validate_choice(m0):
  if m0 == 'c':
      return True
  elif m0 == 'e':
      return True
  return False

while True:
  try:
      m0 = str(input("Select option and press Enter: "))
      if validate_choice(m0):
        break
  except ValueError:
      print ("Invalid option!")

while True:
# make this go back to taking input if no valid input is given
  if m0 == 'c':
    msg = input("Input Text: ")
    morse = morsecodify(msg)
    print("Your Message in Morse Code:")
    print("/MSG START/ " + morse + "/MSG END/")
    cont = input("Would you like to convert another string? [y/n] ")
  elif m0 == 'e':
    print('Bye!')
    # give option to clear screen
    exit()
# This si redundant , given the while loop above
#else:
#  print(m0 + " is not a valid option!")
#  m0 = input("Select a valid option: ")
  if cont != 'y':
    break
print('Bye!')
exit()



  
# code here to choose if quit or another input

