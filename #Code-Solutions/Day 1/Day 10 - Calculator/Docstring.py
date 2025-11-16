def format_name(f_name, l_name):
    """Takes first and last name, 
        then format them """              # DocString
    f_name = f_name.title()               # title() function changes any string to "Title case", aka: first letter is capitalized
    l_name = l_name.title()
    full_name = f_name +" "+  l_name
    return (f"Your name is {full_name}")

name= format_name("AHMED", "SHWEtA")
print(name)