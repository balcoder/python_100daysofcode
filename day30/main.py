''' error handling'''

try:
    file = open("day30/missing_file.txt")
    # a_dict = {"key": "value"}
    # print(a_dict["7979"])
except FileNotFoundError as error_message:
    file = open("day30/missing_file.txt", 'w')
    file.write("Something good is going to happen.")
except KeyError as error_msg:
    print(f"The key {error_msg} does not exist.")
else:
    text = file.read()
    print(f"This is the text {text}")
finally:
    file.close()
    print("file was closed")    