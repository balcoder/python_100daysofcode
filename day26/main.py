import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

df = pandas.read_csv("day26/nato_phonetic_alphabet.csv")

nato_phonetic_dict = {row.letter:row.code for (index, row) in df.iterrows()}
# use if statement to catch non letters in input

# while True:
#     # 2. Create a list of the phonetic code words from a word that the user inputs.
#     word = input("What word would you like to translate?\n").upper()
#     phonetic_code = [nato_phonetic_dict.get(letter) for letter in word]
#     if None in phonetic_code:
#         print("Sorry only letters")
#     else:
#         # phonetic_code = [nato_phonetic_dict.get(letter) for letter in word]
#         print(phonetic_code)

# use try block to catch non letters with while loop

# keep_translating = True
# while keep_translating:
#     word = input("Type QUIT to exit. What word would you like to translate?\n").upper()
#     if word == "QUIT":
#         keep_translating = False
#     else:
#         try:
#             phonetic_code = [nato_phonetic_dict[letter] for letter in word]            
#         except KeyError:
#             print("Sorry only letters")
#         else:
#             print(phonetic_code)

# using a try block with recursive function call
def generate_code():    
    word = input("Type QUIT to exit. What word would you like to translate?\n").upper()

    if word == "QUIT":
        print("Exiting program")
        return
    try:
        phonetic_code = [nato_phonetic_dict[letter] for letter in word]            
    except KeyError:
        print("Sorry only letters")
        generate_code() # if error then call function again
    else:
        print(phonetic_code)
        generate_code()

generate_code()
