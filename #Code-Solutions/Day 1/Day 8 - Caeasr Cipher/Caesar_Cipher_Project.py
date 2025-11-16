alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
import os
def old_encrypt(text, shift):

    modified_alphabet= []
    text_indices=[]
    encrypted_text = ""
    for i in range(26):
        modified_alphabet.append(" ")

    ### Creating shifted alphabet ###
    for i in range(26):
        modified_alphabet[(i-shift)%26] = alphabet[i]

    ### Getting original message letters indices###
    for letter in text:
        for index in range(len(alphabet)):
            if letter == alphabet[index]:
                text_indices.append(index)
                break

def old_decrypt(cipher_text, shift):
    decrypted_text = ""
    for letter in cipher_text:
        index = alphabet.index(letter)
        decrypted_letter = alphabet[(index-shift)%26]
        decrypted_text +=(decrypted_letter)
    print(f"The decrypted text is: {decrypted_text}")

def caesar(start_text, shift_amount, cipher_direction):
        
        new_text = ""
        shift_amount %= 26

        if cipher_direction == "decode":
            shift_amount *= -1

        for char in start_text:
            if char not in alphabet:
                new_text += char
            else:
                index = alphabet.index(char)
                decrypted_letter = alphabet[(index+ shift_amount)%26]
                new_text +=(decrypted_letter)

        print(f"The {cipher_direction}d text is: {new_text}")

print(logo)
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(text, shift, direction)

    go_again = input("\nType 'yes' if you want to go again. Otherwise type 'no'. \n")
    if go_again =="no":
        print("Good Bye")
        break
    os.system('cls')




'''
TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    e.g. 
    plain_text = "hello"
    shift = 5
    cipher_text = "mjqqt"
    print output: "The encoded text is mjqqt"

    #HINT: How do you get the index of an item in a list:
    https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    #🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
'''


'''
TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  e.g. 
  cipher_text = "mjqqt"
  shift = 5
  plain_text = "hello"
  print output: "The decoded text is hello"


TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable.
You should be able to test the code to encrypt *AND* decrypt a message.
'''

#TODO-3: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
