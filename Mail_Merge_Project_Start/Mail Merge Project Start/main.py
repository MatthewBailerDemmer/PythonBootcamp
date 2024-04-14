#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACE_HOLDER = "[name]"
text = ""
people = []
with open("Input/Letters/starting_letter.txt") as file:
    text = file.read()

with open("Input/Names/invited_names.txt") as file:
    people = file.readlines()

for person in people:
    new_person = person.replace("\n", "")
    name = new_person.strip()
    with open(f"Output/ReadyToSend/{new_person}", "w") as file:
        new_letter = text.replace(PLACE_HOLDER, name)
        file.write(new_letter)