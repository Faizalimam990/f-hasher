import hashlib
from pyfiglet import Figlet
from termcolor import colored

f=Figlet(font="slant")
text=colored(f.renderText('F-hasher'),'red')
print(text)
print("______CREATED BY FAIZAL IMAM______")

while True:
    text1=input(colored("Press D for Decryption or press S for saving in text file And E for exit:",'green'))
    if text1=="d" or text=="D":
        h=hashlib.md5()
        enc=input(colored("input Your text:",'blue'))
        h.update(enc.encode())
        hex=h.hexdigest()
        print("______________________________________")
        print("your encoded text is:",hex)
        print("______________________________________")
    
    elif text1=='S' or text1=="s":
        h=hashlib.md5()
        enc=input(colored("input Your text:",'blue'))
        h.update(enc.encode())
        hex=h.hexdigest()
        f=open("enc.txt","w")
        f.write(str(hex))
        f.close()
        print("Your encrypted text is saved successfully!!!")
    
    elif text1=="e" or text1=="E":
        print(colored("thanks for using my tool",'yellow'))
        break
    else:
        print("Invalid command")
        break

