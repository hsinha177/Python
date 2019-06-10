#pgm to take username check it and if all the letters r char thn make the user & assign password hello[username]

import os 
import crypt

l=['0','1','2','3','4','5','6','7','8','9']
u_n=input("Enter username : ")
check=0

for i in u_n :
    if i in l :
        check=1
        
if check==1:
    print('Invalid username')

else:
    passkey = "hello"+u_n
    encPass = crypt.crypt(passkey,"22")
    os.system("user added -p " + encPass +" "+u_n)
    print("username accepted")



