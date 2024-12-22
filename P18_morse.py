#Author: Bogdan Trigubov
#Date: November 18th, 2024
#Description: Program that can translate between english and morse code. Requires a txt code file with translations. (P18_code.txt)  
import sys
def get_dictionary(code_file):
    """ Generate a morse code dictionary from code_file. 
    precondition: 
    - code_file is txt file with english letter and it's corresponding morse code separated by a space.
    - each entry is separated by a newline"""
    dictionary = {" ":""}
    morse_list = []
    value_string = ""
    with open(code_file) as translation:
        for line in translation: #separates code into lines and puts them into alist
            morse_list+=[line]
        for string in morse_list: # converts each line in list into a string
            string_str = ""
            string_str+=string
            string_str = string_str.replace("\n","") #removes \n and possible space
            string_str = string_str.strip()
            char_list = []
            for char in string_str: #builds new list for each line out of split up charachters
                char_list+= [char]
            key = char_list[0] #returns string
            value_list = char_list[1:] #
            value = ""
            for item in value_list: #converts list of value content back into a string
                value += item
            dictionary[key] = value.strip() # builds dictionary and removes space
    return dictionary

def reverse_dictionary(d):
    """Reverses a dictionary.
    precondition: d is a dictionary"""
    reverse_dict = {}
    dictionary = d
    list_keys = list(dictionary.keys()) #creates list of keys
    list_values = list(dictionary.values()) #creates list of values
    for item in range(len(list_keys)): #takes item for ranged index in each list and assignents it to key and value, which then get added to reverse dict. 
        key = list_values[item]
        value = list_keys[item]
        reverse_dict[key]=value
    return reverse_dict
def translate_fwd(codebook, message):
    """ Translates from regular characters (a-z, 0-9) to morse code using the
    given codebook, separating each code with a space. Unrecognized characters
    are represented with a question mark (?). 
    precondition: 
    - codebook is a dictionary: english keys, morse code values
    - message is an English string"""
    dictionary = codebook
    #dictionary = {' ': '', 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'}
    trans_string = ""
    message = message.upper()
    for char in message:
        translation = dictionary.get(char,"?") #invalid charachters get returned as "?"
        trans_string += translation + " "
    trans_string = trans_string.strip().replace("\n","") # deletes newline
    return trans_string

def translate_rev(codebook, message):
    """ Translate from morse code characters to English, Unrecognized charachters are represented with a question mark (?)
    precondition:
    - codebook is a dictionary: morse code key, english values
    - message is an morse code string
    postcondition: returned string is capitalized"""

    dictionary = codebook
    message = message.upper().replace("'","")
    message = message.split("  ") #processing message
    final_str = ""
    for index in range(len(message)): #message is a list
        string = message[index]
        letters_list = string.split(" ")
        word_str = ""
        for item in letters_list:
            trans_letter = dictionary.get(item, "?") #if item doesn't exist returns "?"
            word_str = word_str+ trans_letter
        final_str = final_str+word_str + " "
    final_str = final_str.strip()
    return final_str

if __name__ == "__main__":
    trans_choice = input("Translate [E]nglish to morse code or [M]orse code to English: ")
    trans_choice = trans_choice.upper()
    while trans_choice != "M" and trans_choice != "E": #User choice loop to ensure valid input
        print(""""Enter valid input! 'M' or 'E' """)
        trans_choice = input("Translate [E]nglish to morse code or [M]orse code to English: ")
        trans_choice = trans_choice.upper()
    message = input("Enter message you wish to translate: ")
    codebook = get_dictionary("P18_code.txt") #codebook is a dictionary with english keys and morse code values
    if trans_choice == "M":
        codebook = reverse_dictionary(codebook) #morse keys, english values        
        print(translate_rev(codebook,message))
    if trans_choice == "E":
        print(translate_fwd(codebook,message))