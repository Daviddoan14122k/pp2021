# import package
import os

print("Hello!! Wellcome to cmd of DoanVanChuong \n")
print(" Current Working Directory:" , os.getcwd())

# change directory at Home
currentdir=os.getenv("HOME")
cmd = os.chdir(currentdir)
cmd = ""

while True:
    cmd=input("ch@David:~"+ os.getcwd() +"$ ")
    if cmd.split()[0] == "cd": #check first word of cmd after space
        try:
            #Change directory
            os.chdir(cmd[3:])  
        except FileNotFoundError:
            # If not found direction show that:
                print("bash: No such file or directory")              
    elif cmd == "exit":
        break
    else:
        os.system(cmd)  
            
