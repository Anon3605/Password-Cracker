import random        #randomly generated indexes reduces time
import pyautogui     #pyautogui for auto marked tkinter Gui for user friendly env

chars="abcdefghijklmnopqurstuvwxyz0123456789"
characters=list(chars)

passwd=pyautogui.password("Enter a Password to test (a-z || 0-9): ")
sample=""
passwd=list(passwd)
while True:
    sample=random.choices(characters, k=len(passwd))
    #choiceing random characters within the length of given password
    print(f"Checking password with {sample}")
    if sample==list(passwd):
        print(f"The Bruteforce Attack is successful and the password is {sample}")
        #Wallah, we are done here
        break