answer1 = "01/15/1967"

def print_header():

    print("""

████████╗██████╗ ██╗██╗   ██╗██╗ █████╗     
╚══██╔══╝██╔══██╗██║██║   ██║██║██╔══██╗    
   ██║   ██████╔╝██║██║   ██║██║███████║    
   ██║   ██╔══██╗██║╚██╗ ██╔╝██║██╔══██║    
   ██║   ██║  ██║██║ ╚████╔╝ ██║██║  ██║    
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚═╝╚═╝  ╚═╝    
                                            
        """)

def print_gameover():

    print("""


  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███   ▐██▌ 
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒ ▐██▌ 
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒ ▐██▌ 
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄   ▓██▒ 
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒ ▒▄▄  
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░ ░▀▀▒ 
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░ ░  ░ 
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░     ░ 
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░      ░    
                                                     ░                         
""")

def print_youwin():

    print("""


                      ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄       ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄ 
                     ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░▌
                     ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌     ▐░▌       ▐░▌ ▀▀▀▀█░█▀▀▀▀ ▐░▌░▌     ▐░▌▐░▌
                     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌       ▐░▌     ▐░▌     ▐░▌▐░▌    ▐░▌▐░▌
                     ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌   ▄   ▐░▌     ▐░▌     ▐░▌ ▐░▌   ▐░▌▐░▌
                     ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌  ▐░▌  ▐░▌     ▐░▌     ▐░▌  ▐░▌  ▐░▌▐░▌
                      ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌ ▐░▌░▌ ▐░▌     ▐░▌     ▐░▌   ▐░▌ ▐░▌▐░▌
                          ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌▐░▌ ▐░▌▐░▌     ▐░▌     ▐░▌    ▐░▌▐░▌ ▀ 
                          ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌░▌   ▐░▐░▌ ▄▄▄▄█░█▄▄▄▄ ▐░▌     ▐░▐░▌ ▄ 
                          ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░▌
                           ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀▀       ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀ 
                                                                                                           


""")
#Introduction
name = input("Hi! What's your name?: ")
hometown = input("Where are you from?: ")
food = input("Okay, one more question. What is your favorite food?: ")

print("\n\nWelcome", name,"from",hometown,". You will have a chance at winning one million dollars.")
print("Oh yeaa and also a chance to buy a lifetime supply of",food,"."" All you have to do is answer these three questions correctly.")

#would you like to play survivor mode or time attack?
#BeginGame
#response = "y"
response = input("Are you ready to start(Y/N)?: ")
#Main
if response.lower() == "y":
    print_header()
else:
     print_gameover()
    

#Fix answer Key
answer1 == "01/15/1967"
response1 = input("What date did the Kansas City Chiefs win their first Super Bowl?(MM/DD/YYYY): ")
if response1 == answer1:
    print("Correct! Next question.")
else:
    print("Incorrect!")
    input("You Lose. Would you like to play again(Y/N)?: ")

answer2 == "3"
response2 = input("How many molecules of oxygen does ozone have?")
if response2 == answer2:
    print("Correct! Next question.")    
else:
    print("Incorrect!")
    input("You Lose. Would you like to play again(Y/N)?: ")

answer3 == "Knee cap"
response3 = input("Which bone are babies born without?")
if response3 == answer3:
    print_youwin()    
else:
    print("Incorrect!")
    input("You Lose. Would you like to play again(Y/N)?: ")

















    





