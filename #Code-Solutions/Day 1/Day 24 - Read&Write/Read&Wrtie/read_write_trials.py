# with open(file = "my_text.txt") as file:
#     contents = file.read()
#     print(contents)


# with open(file = "my_text.txt", mode="a") as file:  # mode "w", write   mode "a", append
#     file.write("\nNew text.")


# when trying to open a file that doesn't exist, it gets created for you

# with open("new_file.txt", mode="w") as file:
#     file.write("hi bitch.")

### Absolute file path ###

# with open(r"C:\Users\ahmed\Desktop\my_text.txt") as file:
#     contents = file.read()
#     print(contents)


### Relative file path ###
relative_path = "../../my_folder/my_text.txt"        # go back two folders, then go into my_folder, then read the text

with open(relative_path, mode="r" ) as file:
    print(file.read())
