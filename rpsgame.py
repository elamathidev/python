import random

print("The game is Stone,Paper,Scissor, you choose any one of this choice")
person = input("Enter your choice: ")
machine = random.choice(["Stone","paper","scissor"])
print("The Machine choice is : ",machine)

if machine == person:
     print("Both are select the same choice,So it's a Tie Break")
elif person == "paper":
    if machine == "stone":
        print("Paper covers the Stone,so Person win the game")
    else:
        print("Scissor cut the Paper,so Machine win the game")
elif person == "scissor":
    if machine == "paper":
        print("Scissor cut the Paper,so person win the game")
    else:
        print("Stone smashes the Scissor,so machine win the game")
elif person == "stone":
    if machine == "scissor":
        print("Stone smashes the Scissor,so person win the game")
    else:
        print("Paper covers the Stone,so machine win the game")
