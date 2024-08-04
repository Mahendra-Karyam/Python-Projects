alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def Caecer_Cipher():
    en_or_de=input("Type 'encrypt' for encryption, type 'decrypt' for decryption:\n")
    word=input("Type your message :\n ").lower()
    shift_number=int(input("Type the shift number :\n"))
    if en_or_de=='encrypt':
        print("Here's the encrypted result: ",end='')
    elif en_or_de=='decrypt':
        print("Here's the decrypted result: ",end='')
    for m in range(len(word)):
        for n in range(len(alphabets)):
            if(word[m]==alphabets[n]):
                encrypt=(n+shift_number)%26
                decrypt=(n-shift_number)%26
                if(decrypt<0):
                    decrypt=(decrypt+26)%26
                if en_or_de=='encrypt':
                    print(alphabets[encrypt],end='')
                elif en_or_de=='decrypt':
                    print(alphabets[decrypt],end='')
Caecer_Cipher()
again = input("\nType 'yes' if you want to go again Otherwise type 'no'.\n")
wanna_again=False
while not wanna_again:
    Caecer_Cipher()
    again = input("\nType 'yes' if you want to go again Otherwise type 'no'.\n")
    if again=='no':
        wanna_again=True
if(again=='no'):
    print("Goodbye")
