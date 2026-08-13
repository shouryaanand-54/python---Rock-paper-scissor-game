# PROGRAM OF SNAKE,WATER AND GUN GAME
import random

computer=random.choice(["1", "2", "3"])
a = input("Enter your choice (1=Snake, 2=Water, 3=Gun): ")
b={"1": "Snake", "2": "Water" , "3": "Gun"}
print(f"Computer choose: {b[computer]}")
print(f"You choose : {b[a]}")

if (computer==a):
    print("It,s a draw!")
else:
    if(computer=="1" and a=="2"):
        print("You lose!")
    elif(computer=="1" and a=="3"):
        print("You win!")
    elif(computer=="2" and a=="1"):
        print("You win!")
    elif(computer=="2" and a=="3"):
        print("You lose!")
    elif(computer=="3" and a=="1"):
        print("You lose!")
    elif(computer=="3" and a=="2"):
        print("You win!")

print("Good bye!")