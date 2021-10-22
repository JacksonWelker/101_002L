print('MAIN MENU:')

print('1) Encode a String')
print('2) decode a string')
print('Q) Quit')

selection = input('Enter your selection:')

if selection == 1:
    encode = input("Enter (brief) text to encrypt: ")
    shift = input('Enter the number to shift letters by: ')
    print(str.encode(encode, shift))
    
elif selection == 2:
    decode = input("Enter (brief) text to decode: ")
    shift = input('Enter the number to shift letters by: ')
    print(str.decode(encode, shift))

else:
    exit()

MAIN MENU:
1) Encode a string
2) Decode a string
Q) Quit
Enter your selection ==> 1
Enter (brief) text to encrypt: hello world
Enter the number to shift letters by: 3
Encrypted: KHOOR ZRUOG
    
MAIN MENU:
1) Encode a string
2) Decode a string
Q) Quit
Enter your selection ==> 2

Enter (brief) text to decrypt: khoor zruog
Enter the number to shift letters by: 3
Decrypted: HELLO WORLD

MAIN MENU:
1) Encode a string
2) Decode a string
Q) QuitEnter your selection ==> 1

Enter (brief) text to encrypt: eleven leaping lavender antelope
Enter the number to shift letters by: 3
Encrypted: HOHYHQ OHDSLQJ ODYHQGHU DQWHORSH

MAIN MENU:
1) Encode a string
2) Decode a string
Q) Quit
Enter your selection ==> Q
    

