with open("./Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines()
with open("./Input/Letters/starting_letter.txt", "r") as letter_file:
    content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        letter = content.replace("[name]", stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as final_letter:
            final_letter.write(letter)





