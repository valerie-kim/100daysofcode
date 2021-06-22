#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

name_list = []

#Since readlines() saves values in a list, so here read() should be used.
with open("./Input/Letters/starting_letter.txt") as letter:
    txt = letter.read()

with open("./Input/Names/invited_names.txt") as names:
    for name in names.readlines():
        name = name[:-1]
        name_list.append(name)
    
for name in name_list:
    new_txt = txt.replace("[name]", name)
    new_txt = new_txt.replace("Angela", "Valerie")
    invitations = open(f"./Output/ReadyToSend/{name}.txt", "w")
    invitations.write(new_txt)
    invitations.close()
    