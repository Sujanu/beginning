alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l" ,"m","n","o","p","q","r","s","t","u","v"
            ,"w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l" ,"m","n","o","p","q","r",
            "s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l" ,"m","n","o",
            "p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l" 
            ,"m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

direction =input("type 'encode' for encrypt and decode for 'decrypt':    \n")
text = input("enter your message:   \n")
shift = int(input("enter number of shift:    \n"))

    

def encrypt(plain_text, shift_amount):
    cypher_text = ""
    for letter in plain_text:
        pos = alphabet.index(letter)
        npos = pos + shift_amount

        nlet = alphabet[npos]
        cypher_text += nlet
    print("encoded cypher text is : ", cypher_text)



def decrypt(cypher_text, shift_amount):
    plain_text = ""
    for letter in cypher_text:
        pos = alphabet.index(letter)
        npos = pos - shift_amount
        plain_text += alphabet[npos]
    print("encoded cypher text is : ", plain_text)
    
    
if direction == "encode":
    encrypt(plain_text=text,shift_amount=shift)
elif direction=="decode":
     decrypt(cypher_text=text,shift_amount=shift)