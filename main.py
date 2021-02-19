#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open("input/Letters/starting_letter.txt") as letter:
    main_letter = letter.read()
with open("input/Names/invited_names.txt") as list_of_names:
    for name in list_of_names.readlines():
        name = name.strip()
        new_letter = main_letter.replace("[name]", name)
        print(new_letter)
        with open(f"Output/ReadyToSend/{name}.txt", "w") as final_letter:
            final_letter.write(new_letter)
