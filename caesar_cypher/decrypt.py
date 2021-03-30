import string # import this so no need to define alpha urself

alpha = string.ascii_lowercase # "abcdefghijklmnopqrstuvwxyz"

def decrypt():
    print("DECRYPTION START\n")
    
    ##############################
    #### DESERIALIZATION PART ####
    ##############################
    
    # get path from user input
    file_path = input('"Specify filename form which decryption should read in. File should exist in the same directory and have appendix .txt : "')
    f = open(file_path, "r") # opens txt file
    encrypted_message = f.read() # reads in file contents into memory
    key = int(input("Enter key to decrypt: ")) # get key from user input
    
    decrypted_message = "" # assign dummy

    for c in encrypted_message: # loop through letters in encrypted msg

        if c in alpha: # loop through alphabet
            position = alpha.find(c) # get pos of letter in aphabet
            new_position = (position - key) % 26 # apply formula
            new_character = alpha[new_position] # get new char
            decrypted_message += new_character # add it to decrypted
        else:
            decrypted_message += c # symbols arent encrypted

    print("Your decrypted message is:\n")
    print(decrypted_message)

decrypt()