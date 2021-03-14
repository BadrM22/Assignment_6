def reverse_string(text):
    
    return " ".join(text.split()[::-1])

def capitalize_string(text):
    return "".join(map(lambda char:char.capitalize(),text))

def cap_string(text):
    char=''
    for c in text:
        char+=c.capitalize()
    
    return char
    
