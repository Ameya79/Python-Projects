# TODO-1: Import and print the logo from art.py when the program starts.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


over = False



def caesar(original_text, shift_amount, encode_or_decode):
    cipher_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:

        if letter in alphabet:
            position = alphabet.index(letter)
            new_pos = position + shift_amount
            cipher_text = cipher_text+alphabet[new_pos]
        else:
            cipher_text = cipher_text + letter
    print(f"Here is the {encode_or_decode}d result: {cipher_text}")




while not over :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    again = input(f"Do you want to go again type 'yes' to do so or type 'no' \n")
    if again.lower() == 'no':
        over = True
        print('bye')










        

