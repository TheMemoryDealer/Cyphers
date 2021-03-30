import string # import this so no need to define alphabet urself

alpha = string.ascii_lowercase # "abcdefghijklmnopqrstuvwxyz"

'''
Function takes in user message and key and applies Caesar cypher, then writes to file. 
'''
def encrypt():
    print("ENCRYPTION START\n")
    file_path = input("Specify the file where the message is: ")
    f = open(file_path, "r") # opens txt file
    message = f.read().lower() # reads in file contents into memory
    key = int(input("Enter your key: ")) # this is the shift

    encrypted_message = ""

    for c in message: # loop through letters in plain msg

        if c in alpha: # punctuation and similar symbols aren't encrypted, so leave em
            position = alpha.find(c) # get position of that char
            new_position = (position + key) % 26 # compute new position using formula. 26 cuz theres 26 letters A-Z
            new_character = alpha[new_position] # get encrypted character using position
            encrypted_message += new_character # add it to message
        else:
            encrypted_message += c # if not letter, leave as it is

    print("Processing...")
    print("Your encrypted message is:\n")
    print(encrypted_message)
    print('ENCRYPTION END')
    
    ##############################
    ##### SERIALIZATION PART #####
    ##############################
    
    path = input("Specify filename to which encryption output should be written to. File should exist in the same directory and have appendix .txt : ")
    
    f = open(path, "w")
    f.write(encrypted_message)
    f.close()
    

encrypt()
