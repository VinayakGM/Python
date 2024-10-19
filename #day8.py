
#ceaser cipher project

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction=input("Type 'encode' to encrypt, type 'decode' to decrypt\n").lower()
text=input("Type your message : \n").lower()
shift=int(input("Type the shift number : \n"))

def encrypt(original_text,shift):
    encrypted_text=""
    for char in original_text:
        index=alphabet.index(char)
        new_index=(index+shift)%26
        encrypted_text+=alphabet[new_index]
    print(f"Encoded text {encrypted_text}\n")

def decrypt(text,shift):
    original_text=""
    for char in text:
        index=alphabet.index(char)
        new_index=(index-shift)%25
        if new_index<0:
            new_index+=25
        original_text+=alphabet[new_index]
    print(f"Decoded text: {original_text}")

if direction=="encode":
    encrypt(text,shift)
elif direction=="decode":
    decrypt(text,shift)
else:
    print("you typed wrong option\n")
