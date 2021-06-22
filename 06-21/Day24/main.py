#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

name_list = []
with open("./Input/Names/invited_names.txt") as name:
    names = name.readlines()
    
with open("./Input/Letters/starting_letter.txt") as letter:
    txt = letter.read()
    for n in names:
        new_name = n[:-1]
        new_txt = txt.replace("[name]", new_name)
        new_txt_2 = new_txt.replace("Angela", "Valerie")
        with open(f"./Output/ReadyToSend/{new_name}.txt", "w") as person:
            person.write(new_txt_2)
            