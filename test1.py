# name: Raghav
# author: Raghav
name = input("Enter your name\n")
email = input("Enter your email\n")
password = int(input("Create a numberic password\n"))
# seeing that passord is greater than 8 digits
while password < 10000000:
    password = int(input("It is small: "))
# confirming
comfirm = int(input("Comfirm your password: "))
while not password == comfirm:
    comfirm = int(input("Enter again password\nDoesn't match\n"))
# info
info = {
    "name": name,
    "email": email,
    "password": password,
}
# details
detail = {name, email, password}
# start menu
print(f"Hello {name} to this game")
options = ["Terminal", "Play"]
for option in options:
    print(option)
# function to add number
def prizeAdd(prize_var, add):
    return prize_var + add
choose = input(">> ")
# play
if choose == 1 or choose.lower() == "play":
    print("Welcome to Guess game")
    prize = 0
    guess1 = input("Which is the most populated country\n1-China\n2-India\n3-USA\n4-Russia\n")
    if guess1.lower() == "INDIA".lower():
        print("yes")
        # prizeAdd(prize, 100) doesn't working
        prize = prize + 100
        print(f"You won {prize}")
        guess2 = int(input("How many planets in our solor system\n1-9\n2-8\n3-0\n4-1\n"))
        if guess2 == 8 or guess2 == 9:
            print("yes")
            # prizeAdd(prize, 200) doesn't working
            prize = prize + 200
            print(f"You won {prize}")

            guess3 = input("How many gender exist\n1-10\n2-2\n3-1\n4-100\n")
            if guess3 == 3 or guess3 == 2:
                print("yes")
                prize = prize + 900
            else:
               print("You only win", prize)
        else:
            print("You only won {}".format(prize))
    else:
        print("Lose all")
elif choose == 2 or choose.lower() == "terminal":
# terminal
    print("Welcome from here")
    while True:
        com = input(">>>>")
        if com == "info":
            for information in info.values():
                print(information)
        elif com == "change.name":
            name = input("Enter new name: ")
            print(f"Name set to {name}")
        elif com == "see.password":
            print(info['password'])
        else:
            print("ERROR")
