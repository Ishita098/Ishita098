letter=''' Dear<|name|>,
you are selected!
date:<|date|>'''
name=input("Enter your name\n")
date=input("Enter your date\n")
letter=letter.replace("<|name|>", name)
letter=letter.replace("<|date|>", date)

print(letter)
