# 
''' Create a letter using starting_letter.txt for each name in invited_names.txt '''

PLACEHOLDER = "[name]"
with open('day24/Input/Names/invited_names.txt', 'r',  encoding="utf-8") as names:
    for name in names:
        new_letter = open(f'day24/Output/letter_for_{name.strip()}.txt', 'w',  encoding="utf-8")
        with open('day24/Input/Letters/starting_letter.txt', 'r', encoding="utf-8") as template:
            for line in template.readlines():
                new_line = line.replace(PLACEHOLDER, name.strip())
                new_letter.write(new_line)



