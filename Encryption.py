ALPHABET = "abcdefghijklmnopqrstuvwxyz"

#---functions---

def key_conv():
    try:
        key= int(input("Enter the required shift value in the range 1-25: "))
        conversion(key)
    except:
        print("Only an integer value is accepted as the key")                 #making sure that the program won't crash if a string value was input as the key, by the user


def conversion(key):
    if key>0 or key<26:
            index=0
            while index<len(message):
                letter=message[index]
                #print(letter,end="")       #to check whether the correct letter was selected
                character = ALPHABET.find(letter)           #Finding the index of the letter in ALPHABET, (-1)= not found in ALPHABET
                #print(character," ",end="")         #to check whether the letter represents the correct index
                if character!=(-1):             #to make sure that only lowercase alphabetic characters are shifted
                    if to_do == 'e':            #applying the key to find the new index, when encoding
                        new_character = ((character + key)%26)     #applying the key to find the new index, %26 is used for wrap-around
                    elif to_do == 'd':          #applying the key to find the new index, when decoding
                        new_character = (character - key)     #applying the key to find the new index, %26 isn't required for wrap-around because (-)ve indexes start from behind and max key is 25
                    new_letter= ALPHABET[new_character]    #finding the letter that represent the new position
                    print(new_letter,end="")
                else:
                    print(letter,end="")
                index= index+1

    else:
        print("Invalid shift value. Please enter a shift value in the range 1-25.")



#---program---

to_do = ""  #string variable used for while loop
while to_do!='q':
    
    to_do= input("\n\nWhat is your requirement?\ne = Encode a string\nd = Decode a string\nq = Quit program\n")         #user requirement
    to_do = to_do.lower()           #for ease of user (capital letters accepted)

    if to_do=='e':      #part A:Encoding
        message= input("Enter the message that is required to be Encoded: ")
        key_conv()



    elif to_do=='d':            #Decoding
        prompt_d=input("Do u know the key of the Encoded text?(yes/no) ")
        prompt_d = prompt_d.lower()         #for ease of user (capital letters accepted)
        
        if prompt_d=="yes" or prompt_d=="y":                       #part B:Decoding
            message= input("Enter the message that is required to be Decoded: ")
            key_conv()


            
        elif prompt_d=="no" or prompt_d=="n":                      #part C:Decoding(Extension-plain text)
            message= input("Enter the message that is required to be Decoded: ")
            plain_text =input("Enter a plain-text word: ")

            try:
                #finding the index of the first encoded letter in the message entered to be decoded, in ALPHABET
                index_plain_txt=0
                while index_plain_txt<len(plain_text):
                    letter_plain_txt = plain_text[index_plain_txt]      #selecting a letter in the plain text according to the index
                    character_plain_txt = ALPHABET.find(letter_plain_txt)   #finding the specific letter's index in ALPHABET
                    if character_plain_txt!=(-1):
                        break
                    else:
                        index_plain_txt = index_plain_txt + 1
                    
                count=0
                index=0
                while index<len(message):
                    letter=message[index]
                    #print(letter,end="")           #to check whether the correct letter was selected
                    character = ALPHABET.find(letter)       #Finding the index of the letter in ALPHABET, (-1)= not found in ALPHABET
                    #print(character,end="")        #to check whether the letter represents the correct index
                    if character!=(-1):             #to make sure that only lowercase alphabetic characters are shifted
                        if count==0:        #finding the rotation key only for the first letter which was encoded, to make sure that the letter chosen for this was the same as in the plain_text
                            rotation_key = character - character_plain_txt      #this gives the key that was used to encode the message
                            count+= 1
          
                        #print(rotation_key,end="")
                        new_character = (character - rotation_key)     #applying the key to find the new index, %26 isn't required for wrap-around becasue (-)ve indexes start from behind and max key is 25
                        dec_letter= ALPHABET[new_character]    #finding the letter that represents the new position
                        print(dec_letter,end="")
                    else:
                        print(letter,end="")
                    index= index+1

                if rotation_key>=0:
                    print("\nrotation key = ",rotation_key)
                else:
                    print("\nrotation key = ",(26+rotation_key))    #to make sure that the rotation key isn't given as a negative value
            except:
                print("\nOnly the first word is accepted as the plain text in this program. Please try again.")

        else:
            print("Invalid input. Please try again.")       #can use a loop to get back to decoding method section instead of going back to the main menu



    elif to_do== 'q':
        print("Exiting program...")
        continue
    
    else:
        print("Error! Please enter valid input", end="")    #re-prompting for a valid input command

