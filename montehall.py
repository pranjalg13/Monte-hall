# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 18:17:31 2019

@author: Pranjal
"""
import random
doors=[0]*3
goatdoor=[0]*2
swap=0#for counting win by swap
dontswap=0#for counting win by nonswap
x=random.randint(0,2)
doors[x]="BMW"
for i in range(3):
    if(i==x):
          continue
    else:
        doors[i]="Goat"
        goatdoor.append(i)
choice=int(input("enter your choice"))
door_open=random.choice(goatdoor)
while(choice==door_open):
    door_open=random.choice(goatdoor)
ch=input("want to swap or not enter y or n: ")
if(ch=='y'):
    if(doors[choice]=="Goat"):
        print("player wins")
        swap=swap+1
        
    else:
        print("player loose")
elif():
    if(doors[choice]=="Goat"):
        print("player loose")
    else:
        print("player wins")
        dontswap+=1
else:
    print("plz enter y or only")
    
print(dontswap,"dontswap")
print(swap,"swap")        
        