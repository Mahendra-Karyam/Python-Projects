import random
print("Welcome to the Shuffle Password Generator!")
letters_number=int(input("How many letters would you like in your password?\n"))
letter=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
special_characters_number=int(input("How many symblols would you like?\n"))
special_character=['!','@','#','$','%','^','&','*','(',')']
Numbers_number=int(input("How many numbers would you like?\n"))
Number=['1','2','3','4','5','6','7','8','9','0']
PASSWORD=""
for i in range(1,letters_number+1):
    letters=random.choice(letter)
    PASSWORD=PASSWORD+letters
for j in range(1,special_characters_number+1):
                              special_characters=random.choice(special_character)
                              PASSWORD=PASSWORD+special_characters                             
for k in range(1,Numbers_number+1):
    Numbers=random.choice(Number)
    PASSWORD=PASSWORD+Numbers
PASSWORD=list(PASSWORD)
random.shuffle(PASSWORD)  #Here,it prints like list.But,we need PASSWORD as string.So,we create empty string.
rdp=""
for l in range(0,letters_number+special_characters_number+Numbers_number):
    rdp=rdp+PASSWORD[l]
print(rdp)
