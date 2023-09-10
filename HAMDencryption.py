# encryption.py
# Hamd Khan, ENDG 233 F21









### Define your functions here
import string #imports string module


def encode(encoding_cipher,text_encoding,dict_pair): #defines function called encod
    """
    function: this functions job is to take user input and encrypt such input based off a provided cipher algorthim
    parameter: (encoding_cipher) this parameter serves to provide a base to encrypt off
    parameter: (text_encoding) this is text provided by user which will be incoded based off of cipher_encoding
    parameter: (dict_pair) this the dictionary_encode created in main function which has zipped the valid cipher to the alphabet bank in lowercases, where the keys are the cipher letters and values are the alphabet
    return: (output) the function returns the encoded output based off of the parameters listed above
    """
    output = ""
    for indiv_letter in text_encoding:
        for encoding_cipher, values in dict_pair.items(): 
            if values == indiv_letter:
                output = output + encoding_cipher
    return output


def decode(decoding_cipher, text_decoding,dict_pair):
    """
    function: this functions job is to take user input which has been encoded and reverse it to a decrypted output based off a inputted cipher algorthim
    parameter: (decoding_cipher) this parameter serves to provide a base to decrpty off
    parameter: (text_decoding) this is the encoded text provided by user which will be decrypted based off of their chosen cipher
    parameter: (dict_pair) this is the dictionary_decode created in main function which has zipped the the alphabet bank to the valid cipher, which is in the dictionary form with key being the alphabetbank and value being the cipher
    return: (output) 
    """
    output = ''
    for indiv_letter in text_decoding:
        for decoding_cipher, values in dict_pair.items():
            if values == indiv_letter:
                output = output + decoding_cipher
    return output

def cipher_validator(chosen_cipher):
    '''
    function: this function validates the cipher based of being a length of 26 characters and if the user inputted an alphanumerical cipher, else if one or more of these conditions are not fullfilled then the user is prompted back to the main function to restard program
    parameter: (chosen_cipher) parameter is the inputted cipher by the user
    return: returns the chosen cipher only under the condition that the cipher is valid based of the conditions stated above
    '''
    if len(chosen_cipher) == 26 and chosen_cipher.isalnum():
        print('Your cipher is valid')
        return chosen_cipher
    else:
        print('Your cipher must contain 26 unique elementsz of a-z or 0-9.')
        main()
   
    

print("ENDG 233 Encryption Program")

def main():
    '''
    function: this funtion will call upon all other functions above in order to execute code, firstly promps user for input 1,2,0 depending on user input it will run through if, else branches and call on the respective function based off of this input
    variable: (loop_var) the loop variable which is assigned an arbitrary value in order for the main function to continously repeat unless user inputs 0
    variable: (text) is assigned to the input of the user, this is what the user would like to be proccessed
    variable: (validated_cipher) calls upon the cipher_validator function to call the valid cipher
    variable: (alphabet_bank) is imported using string module which allows to create a string of the lowercase ASCII alphabet
    variable: (dictionary_encode) is a dictionary made by zipping the validated_cipher to keys and alphabet_bank to values
    variable: (dictionary_decode) is a dictionary made by zipping the alphabet_bank to keys and validated_cipher to values
    returns: function returns none
    
    '''
    loop_var= 0 #arbitrary number assigned to maintain while loop
    while loop_var == 0:
        user_input = int(input(
    'Select 1 to encode or 2 to decode your message, select 0 to quit: '))
        if user_input == 0:
            print('Thank you for using the encryption program.')
            break
        text = input('Please enter the text to be processed: ')
        cipher= input('Please enter your cipher text: ').lower()
        validated_cipher = cipher_validator(cipher)
        alphabet_bank = string.ascii_lowercase
        dictionary_encode = dict(zip(validated_cipher,alphabet_bank))
        dictionary_decode = dict(zip(alphabet_bank,validated_cipher))
        if user_input == 1:
          print(encode(validated_cipher,text,dictionary_encode))
        elif user_input == 2:
          print(decode(validated_cipher,text,dictionary_decode))

    
main()

print('Thank you for using the encryption program.')

#