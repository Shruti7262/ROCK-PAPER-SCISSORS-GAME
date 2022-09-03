import random
game_list = ['Rock','Paper','Scissors']
computer = c = 0
command = p = 0
print("Score: Computer " + str(c) + "Player " + str(p))

run = True
while run:
    computer_choice = random.choice(game_list)
    command = input("Rock, Paper, Scissors or Quit: ")
    if command == computer_choice:
        print("Player: " + command)
        print("Computer: " + command)
        print("TIE")
    elif command == 'Rock':
        if computer_choice == 'Scissors':
            print("Player: " + command)
            print("Computer: " + command)
            print("Player Won!")
            p +=1
        else:
            print("Player: " + command)
            print("Computer: " + command)
            print('Computer Won!')
            c +=1
    
    elif command == 'Paper':
        if computer_choice == 'Rock':
            print("Player: " + command)
            print("Computer: " + command)
            print("Player Won!")
            p +=1
        else:
            print("Player: " + command)
            print("Computer: " + command)
            print('Computer Won!')
            c +=1
    
    elif command == 'Scissors':
        if computer_choice == 'Paper':
            print("Player: " + command)
            print("Computer: " + command)
            print("Player Won!")
            p +=1
        else:
            print("Player: " + command)
            print("Computer: " + command)
            print('Computer Won!')
            c +=1
    
    elif command == 'Quit':
        break
    else:
        print("Wrong command! ")

print("Player: " + command)
print("Computer: " + command)
print("")
print("Score: Computer " + str(c) + "Player " + str(p))
print("")