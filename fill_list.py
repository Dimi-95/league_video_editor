import os
import sys

amount = int(sys.argv[1])
print("amount: ", amount)
path = "samples/clips"
dir_list = os.listdir(path)

counter = 0


while(True):
    if(amount != 0):
        #print(dir_list[counter])
        f = open("clip_list.txt", "a")
        f.write(f"\nfile 'samples/clips/{dir_list[counter]}'")
        counter = counter + 1 
        amount = amount - 1
    else:
        break
