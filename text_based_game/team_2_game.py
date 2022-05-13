from helpers import slow_print, fast_print, really_fast_print, get_random_image, scramble_image, credits_print, ascii_puzzle_print, ascii_puzzle
from time import time, sleep
from random import randint

item ='whip' # selected

def start_game():
    print()
    credits_print(''' █████  ███    ██  ██████ ██ ███████ ███    ██ ████████     ████████  ██████  ███    ███ ██████  ███████     
██   ██ ████   ██ ██      ██ ██      ████   ██    ██           ██    ██    ██ ████  ████ ██   ██ ██          
███████ ██ ██  ██ ██      ██ █████   ██ ██  ██    ██           ██    ██    ██ ██ ████ ██ ██████  ███████     
██   ██ ██  ██ ██ ██      ██ ██      ██  ██ ██    ██           ██    ██    ██ ██  ██  ██ ██   ██      ██     
██   ██ ██   ████  ██████ ██ ███████ ██   ████    ██           ██     ██████  ██      ██ ██████  ███████     
                                                                                                            ''')
    print()
    slow_print("Welcome explorer, to Ancient Tombs!")
    print()

    prologue = input('"PRESS ENTER" to play the prologue. "TYPE ANYTHING" to skip. ').lower()
    print()

    if prologue != "":
        print()
        print("Prologue skipped!")
        print()
        entrance_puzzle()

    else:
        slow_print("For decades, the Tomb of the Holy Grail has successfully fended off many attempts by ambitious adventurers hoping to swipe ")
        print()
        slow_print("the treasure rumoured to lie within.")
        print()
        slow_print("Some met particularly grisly ends, but without risk there is no reward.")
        print()
        slow_print("You are a fearless adventure who laughs in the face of danger.")
        print()
        slow_print("Armed with a trusty whip, lantern and blade, it is up to you to navigate the tomb and escape with the treasure... and your life.")
        print()

        entrance_puzzle()

def entrance_puzzle():
    slow_print("You stand before the crumbling ancient tomb. The entrance door is shut tight.")
    sleep(1)
    print()
    ascii_puzzle()
    print()
    sleep(1)
    slow_print("There are a row of symbols next to the door. An upwards arrow, a man running, a fox, a dog and three z's positioned together.")
    print()
    slow_print("You pull out the clue you won in a game of cards. It reads :")
    print()
    sleep(1)
    print(
        '''                                     ----------------------------------------------
                                    |                                              |
                                    | The quick brown fox jumps over the lazy dog  |
                                    |                                              |
                                     ----------------------------------------------'''
    )
    sleep(1)
    print()
    slow_print("Looks like you'll have to press each of the symbols in the correct order to open the entrance.")
    print()
    fast_print( "1. Upwards arrow")
    print()
    fast_print( "2. Dog")
    print()
    fast_print( "3. Running Man")
    print()
    fast_print( "4. Three Z's")
    print()
    fast_print( "5. Fox")
    print()
    correct_order = [3, 5, 1, 4, 2]
    user_attempt = select_ascii_image()
    
    while user_attempt == "error":
        user_attempt = select_ascii_image()
    
    if user_attempt == correct_order:
        print("There is a rumble and the large stone doors slowly swing open. You step through the opening and find yourself in a dimly lit corridor.")
        dodge_obstacles()
    else:
        print("You hear a hiss and then feel a sting on your arm. You pull out the small poisoned dart just before you pass out.")
        game_over()

def select_ascii_image():

    puzzle_attempt = []
    words = ["first", "second", "third", "fourth", "final"]
    for x in range(0,5):
        try:
            choice = int(input(f"{words[x].upper()} CHOICE : "))
            if 1 <= choice <= 5:
                puzzle_attempt.append(choice)
                print()
                print(f"Current order: {(puzzle_attempt)}")
                print()
            else:
                print()
                print("That number is not an option!")
                print()
                puzzle_attempt = "error"
                return puzzle_attempt
        except ValueError:
            print()
            print("That's not a number. Please try again.")
            print()
            puzzle_attempt = "error"
            return puzzle_attempt
    return puzzle_attempt

def dodge_obstacles():
    print()
    slow_print("You're inside the tomb.  You stop.")
    print()
    slow_print("Something doesn't feel right... Get ready...")
    select_jump()

def select_jump():
    print()
    fast_print("A trap door opens! ")
    print()
    sleep(1)
    current_time = time()
    response = input('QUICK! Type "JUMP" : ').lower().strip()
    if response != "jump":
        print()
        fast_print("Incorrect! You fall down the trap door.")
        game_over()
    elif current_time + 10 < time():
        print()
        fast_print("You did not jump to safety in time! You fall down the trap door.")
        game_over()
    else:
        print()
        fast_print("You leap to safety, that was close...")
        select_duck()

def select_duck():
    print()
    fast_print("But now.. A poisonous dart is flying towards you!")
    print()
    sleep(1)
    current_time = time()
    response = input('QUICK! Type "DUCK" : ').lower().strip()
    print()
    if response != "duck":
        fast_print("Incorrect!  The dart hits your neck and you soon pass out!")
        game_over()
    elif current_time + 5 < time():
        fast_print("You did not duck in time! The dart hits your neck and you soon pass out!")
        game_over()
    else:
        select_roll()

def select_roll():
    fast_print("There's a sudden noise. A boulder is coming right at you! ")
    print()
    sleep(2)
    current_time = time()
    response = input('QUICK! Type "ROLL" : ').lower().strip()
    print()
    if response != "roll":
        fast_print("Incorrect! You got flattened by the boulder!")
        game_over()
    elif current_time + 5 < time():
        fast_print("You did not roll fast enough! You got flattened by the boulder!")
        game_over()
    else:
        slow_print("You roll away through an open doorway, the boulder smashing against it and blocking the way back to the entrance.")
        sleep(1)
        print()
        slow_print("It seems like that's all the traps for now, but be careful, there could be more traps ahead...")
        print()
        select_item()

def select_item():
    slow_print("You take a brief rest to check your equipment.")
    print()
    slow_print("Unfortunately, you have lost 2 items from your bag while dodging the traps.")
    print()
    slow_print("There is no way to go back and grab them now. Which item do you have left with you?")
    print()
    slow_print("PICK ONE: ")
    print()
    slow_print("1. Whip")
    print()
    slow_print("2. Blade")
    print()
    slow_print("3. Lantern")
    print()
    global item
    item_choice = ""
    item_choice = input("YOU CHOOSE : ")
    print()

    if item_choice == "1":
        slow_print("You have chosen to keep the whip!")
        item = "whip"
        print()
        hidden_door()

    elif item_choice == "2":
        slow_print("You have chosen to keep the blade!")
        item = "blade"
        print()
        hidden_door()

    elif item_choice == "3":
        slow_print("You have chosen to keep the lantern!")
        item = "lantern"
        print()
        hidden_door()

    else:
        print("That's not a valid option, please try again")
        item_choice == "error"
        select_item()


def hidden_door():
    print()
    slow_print(f"Well at least you did not lose your {item}, you may need it later on. \n\nYou feel a breeze behind the wall on your right, possibly a hidden door! \n\nThere is also an open corridor on the opposite end of the room that you could take.")
    print()
    select_hidden_door()


def select_hidden_door():
    open_door = input("Do you want to try and open the hidden door? (Y / N) : ").lower().strip()
    if open_door == 'y' or open_door == 'yes':
        select_second_chance()
    elif open_door == 'no' or open_door == 'n':
        print()
        slow_print("You decide against trying to open the hidden door, \n\nwho knows what could be behind it after all? \n\nInstead, you carry on through the passage opposite.")
        riddle_game()
    else:
        print('Your answer must be yes or no!') 
        select_hidden_door()
        
count_chances = 0
def select_second_chance():
    global count_chances 
    if count_chances == 0:
        print()
        slow_print("You approach the wall and feel over the stone bricks. \n\nAha! Your hands find the edge of a concealed door and you start to pull. \n\nYou swear you hear a faint hiss as the stiff door partially opens.")
        print()
        count_chances += 1
        slow_print("You start to have second thoughts.")
        print()
        unstick_door = input("Are you sure that you want to continue opening the door? ( Y / N) : ").lower().strip()
        print()
        if unstick_door == 'y' or unstick_door == 'yes' :
            slow_print("After a couple of minutes battling to unstick the door, you finally have enough room to pass through it.")
            print()
            slow_print("The hissing grows louder.\n\nIn the low light, you see a tiny snake in the centre of the secret room.")
            sleep(1)
            credits_print('''                   ____          
                  / . .\\
                  \\  ---<
                   \\  /
        ___________/ /
     -=:____________/''')
            sleep(1)
            print()
            slow_print("It gives an angry hiss at being disturbed, but otherwise slithers off.")
            print()
            slow_print("There are hieroglyphics along the wall, but they are covered in years of dust and grime.")
            print()
            bonus_game()
        elif unstick_door == 'n' or unstick_door == 'no':
            slow_print("It feels like a wise decision to leave the door alone. \n\nWhat even was that hissing anyway? \n\nInstead, you carry on through the passage opposite.")
            riddle_game()
        else:            
            slow_print('Please answer yes or no!') 
            select_second_chance()
            
    else:
        unstick_door = input("Do you want to unstick the door ( Y / N) ").lower().strip()
        print()
        if unstick_door == 'y' or unstick_door == 'yes' :
            slow_print("After a couple of minutes battling to unstick the door, \n\nyou finally have enough room to pass through it.")
            print()
            slow_print("The hissing grows louder.\n\nIn the low light, you see a tiny snake in the centre of the secret room")
            sleep(1)
            credits_print('''                   ____          
                  / . .\\
                  \\  ---<
                   \\  /
        ___________/ /
     -=:____________/''')
            sleep(1)
            print()
            slow_print("It gives an angry hiss at being disturbed, but otherwise slithers off.")
            print()
            slow_print("There are hieroglyphics along the wall, but they are covered in years of dust and grime.")
            print()
            bonus_game()
        elif unstick_door == 'n' or unstick_door == 'no':
            slow_print("It feels like a wise decision to leave the door alone. \n\nWhat even was that hissing anyway? \n\nInstead, you carry on through the passage opposite.")
            riddle_game()
        else:
            print('You must answer yes or no!') 
            select_second_chance()

PERCENT_SCRAMBLED_RESET = 70
percent_scrambled = PERCENT_SCRAMBLED_RESET
random_image = get_random_image()
bonus_game_image = random_image["animal"]
bonus_game_answer = random_image["name"]

def bonus_game():
    global percent_scrambled
    global bonus_game_image
    global bonus_game_answer
    fast_print("---- Bonus Game! ----")
    sleep(0.5)
    print()
    # scramble the image
    scramble_image(bonus_game_image, percent_scrambled)
    sleep(1)
    print()
    fast_print("Can you make out the hieroglyph?")
    print()
    fast_print('Type "CLEAR" to clear away some of the dirt.  Or "QUIT" to exit.')
    sleep(0.5)
    print()
    response = input('Or can you "GUESS" : ').strip().lower()
    if response == "clear":
        percent_scrambled -= 20
        print()
        fast_print("You wipe away some dirt.  The image becomes clearer.")
        print()
        bonus_game()
    elif response == bonus_game_answer:
        print()
        sleep(1)
        scramble_image(bonus_game_image, 0)
        print()
        vowels = ['a', 'e', 'i', 'o', 'u']
        if bonus_game_answer[0] in vowels:
            a_an_correction = 'n'
        else:
            a_an_correction = ''
        fast_print(f"Whoa! It's a{a_an_correction} {bonus_game_answer}!")
        sleep(1)
        print()
        if bonus_game_answer == "alien":
            fast_print("Hmmmm... Very strange... Maybe this will be relevant in the sequel...")
            print()
        play_again = input("Want to look at more hieroglyphics? (Y/N) : ").lower().strip()
        sleep(1)
        if play_again == 'y':
            print()
            # reset the image
            percent_scrambled = PERCENT_SCRAMBLED_RESET
            random_image = get_random_image()
            bonus_game_image = random_image["animal"]
            bonus_game_answer = random_image["name"]
            bonus_game()
        else:
            print()
            fast_print("It's best not to get distracted for too long.")
            print()
            fast_print("You head back the way you came and then progress forward through the passage.")
            riddle_game()
    elif response == "quit":
        print()
        fast_print("It's best not to get distracted for too long.")
        print()
        fast_print("You head back the way you came and then progress forward through the passage.")
        riddle_game()
    else:
        print()
        fast_print("Incorrect! Try again!")
        print()
        bonus_game()

def riddle_game():
    print()
    slow_print("You enter a small room, with a closed door at one end. There are holes lined up along the stone walls, with the tips of spears poking out of them")
    print()
    slow_print("A disembodied voice fills the room:")
    print()
    slow_print('"You are close to your reward. You need only answer this riddle correctly to carry on to the treasure"')

    select_riddle()

def select_riddle():
    print()
    ascii_puzzle_print('''          ----------------------------------------------------------------------------------------------------------------
         |                                                                                                                |
         | ...'I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?'..." |
         |                                                                                                                |
          ----------------------------------------------------------------------------------------------------------------''')
    sleep(1)
    print()
    slow_print("PICK ONE: ")
    print()
    slow_print("1. Sound")
    print()
    slow_print("2. Echo")
    print()
    slow_print("3. Glare")
    print()
    answer = input("YOU CHOOSE : ").lower().strip()

    if answer == "2":
        print()
        slow_print('"CORRECT" the voice booms, sound bouncing off the walls. The exit door creaks open and you stride on ahead."')
        print()
        holy_grail()
    
    else:
        print()
        slow_print('"Wrong answer adventurer. You can try again if you wish"')
        print()
        select_riddle()

def holy_grail():
    slow_print("You find yourself in an impressively large room with a long table in the centre, filled with cups of different shapes and sizes.")
    print()
    slow_print("An old looking man in crusader knight armor stands next to it. This all feels familiar somehow...")
    print()
    slow_print("He speaks:")
    print()
    slow_print('"I am a Hero of the ancient era and I followed the Holy God."')
    print()
    slow_print('Your task is simple; Pick the Holy Grail.  If you pick right you will be a living immortal, but if not, your life is withdrawn."')
    select_treasure()

def select_treasure():
    print()
    slow_print("You approach the table. Your adventurer's instincts narrow your selection down to three choices : ")
    print()
    slow_print("PICK ONE: ")
    print()
    slow_print("1. Jade Grail")
    print()
    slow_print("2. Wooden Grail")
    print()
    slow_print("3. Golden Grail with Embedded Jewels")
    print()
    answer = input("Please choose which chalice you think that the treasure is : ").lower().strip()
    print()
    if answer == "2":
        slow_print('You take a sip from the wooden grail. You feel invigorated!"')
        print()
        slow_print('The knight approves of your choice. "You have chosen... wisely. Now you shall never age."')
        print()
        slow_print("The tomb suddenly starts to shake, bits of rock falling from above. It's time to get out of here!")
        print()
        escape()
    else:
        print()
        slow_print("You take a sip from the cup. You suddenly feel very old and frail, collasping to the floor.\n\nThe knight stands over you.")
        print()
        slow_print("Wrong choice...")
        game_over()

def escape():
    slow_print('You search frantically for an exit and spot three possible routes.')
    print()
    slow_print('There is a wooden suspension bridge but it looks old and rotted. Above it there are wooden beams across the ceiling.') 
    print()   
    slow_print("The second path seems straight forward, except for another knight standing in the narrow doorway. He does not look friendly.")
    print()
    slow_print("The third path leads to a room that's as dark as night. You can't decipher anything else about it.")
    print()
    slow_print(f"You remember that you still have your {item}. Where might it be used best here?")
    print()    
    select_escape_route()

def select_escape_route():
    slow_print("PICK ONE: ")
    print()
    slow_print("1. Bridge")
    print()
    slow_print("2. Knight")
    print()
    slow_print("3. Dark")
    print()
    route = input('YOU CHOOSE : ').lower().strip()
    if route == '1' or route == 'b':
        print()
        if item == 'whip':
            slow_print("You put one foot down on the first plank and the entire bridge collapses. That was close!")
            print()
            slow_print("Fortunately you still have your whip to hand.\n\nYou wrap it around one of the sturdy wooden beams and swing across the chasm to safety!")
            print()
            slow_print("You emerge from the tomb and step into the bright sunlight outside. Freedom!")
            print()
            ending()
        else:

            slow_print("You put one foot down on the first plank and the entire bridge collapses. That was close!")
            print()
            slow_print(f"There doesn't seem to be any way you could use your {item} to get across...")
            print() 
            slow_print("You try to go back to the treasure room but the path is blocked by the falling rocks. Soon you are buried under the debris yourself.")
            print()
            game_over()
        
    elif route == '2' or route == 'k':
        print()
        if item == 'blade':
            slow_print('Stepping closer to the knight, he draws his short sword.')
            print()
            slow_print('Fortunately you kept the blade. You parry his slow attack and knock the old man over with a shove, running on to the exit.')
            print()
            slow_print("You emerge from the tomb and step into the bright sunlight outside. Freedom!")
            print()
            ending()
        elif item == 'lantern':
            slow_print('Stepping closer to the knight, he draws his short sword.')
            print()
            slow_print('You take out your lantern. Not knowing what else to do, you throw it at the knight and it bounces harmlessly off his chainmail.')
            print()
            slow_print('"Really?"\n He runs you through with his sword')
            print()
            game_over()
        elif item == 'whip':
            slow_print('Stepping closer to the knight, he draws his short sword.')
            print()
            slow_print('Taking out the whip, you try to attack him with it')
            print()
            slow_print('The knight catches the end of the whip, pulls you closer with it and runs you through with his sword.')
            print()
            game_over()            
        else:
            slow_print('How did you even trigger this message?')
            game_over()

    elif route == '3' or route == 'd':
        print()
        if item == 'lantern':
            slow_print("You pause before the dark entrance to take out your trusty lantern, switching on the bright light.")
            print()
            slow_print("The lantern exposes a tripwire, which you neatly step over. Otherwise, the way out is clear!")
            print()
            slow_print("You emerge from the tomb and step into the bright sunlight outside. Freedom!")
            ending()
        else:
            slow_print(f"You take out your {item} and dash into the darkness.\n There is a 'twang' as your foot gets snagged on something. A tripwire!")
            print()
            slow_print("There is a loud bang and the ground caves in beneath your feet, sending you plummeting down to land on sharp spikes. Ouch..")
            game_over()
    else:
        print()
        print(f"'{route}' is not an option! Please try again")
        select_escape_route()

def ending():
    print()
    slow_print("Congratulations! You claimed the treasure and escaped the tomb in one piece! Very well done!")
    print()
    slow_print("Thank you for playing our game.")
    play_again()

def game_over():
    sleep(1)
    print()
    print('''                    .~~~~`\~~\\
                   ;       ~~ \\
                   |           ;
               ,--------,______|---.
              /          \-----`    \    
       _       `.__________`-_______-'      _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(__/  \__)( |     _.=" <        ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
      (_/"=._"=._ |/     /\     \| _.="_.="\_)      ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
             "=._ (_     ^^     _)"_.="             ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
                 "=\__|IIIIII|__/="                 ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
                _.="| \IIIIII/ |"=._                ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
      _     _.="_.="\          /"=._"=._     _       ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/                                    \_)''')
    print()
    play_again()

def play_again():
    print()
    answer = input("Would you like to play again?...(Y/N) : ").lower()
    if answer == "yes" or answer == "y":
        start_game()
    else:
        print()
        credits()

def credits():
    credits_print('''                                       █████  ███    ██  ██████ ██ ███████ ███    ██ ████████     ████████  ██████  ███    ███ ██████  ███████     
                                      ██   ██ ████   ██ ██      ██ ██      ████   ██    ██           ██    ██    ██ ████  ████ ██   ██ ██          
                                      ███████ ██ ██  ██ ██      ██ █████   ██ ██  ██    ██           ██    ██    ██ ██ ████ ██ ██████  ███████     
                                      ██   ██ ██  ██ ██ ██      ██ ██      ██  ██ ██    ██           ██    ██    ██ ██  ██  ██ ██   ██      ██     
                                      ██   ██ ██   ████  ██████ ██ ███████ ██   ████    ██           ██     ██████  ██      ██ ██████  ███████     
                                                                                                            ''') 
    print()
    credits_print('''                     -----
                    \     /                   
                     \   /                     _     _                  ______ _ _                           _     _ 
              \     __\_/__     /             | |   (_)                 |  ___(_) |                         | |   | |
                   /   |   \                  | |    _  __ _ _ __ ___   | |_   _| |_ ______ _  ___ _ __ __ _| | __| |
            __    /    |    \    __           | |   | |/ _` | '_ ` _ \  |  _| | | __|_  / _` |/ _ \ '__/ _` | |/ _` |
                 /     |     \                | |___| | (_| | | | | | | | |   | | |_ / / (_| |  __/ | | (_| | | (_| |
                /______|______\               \_____/_|\__,_|_| |_| |_| \_|   |_|\__/___\__, |\___|_|  \__,_|_|\__,_|
                 \    )|(    /                                                           __/ |   
                  \  ( | )  /                                                           |___/   
                   \  = =  /
                    \__|__/''')
    print()
    print()

    credits_print('''                     .---.
                     |---|
                     |---|
                     |---|
                 .---^ - ^---.                 _____                _                     _     
                 :___________:                |  __ \              (_)                   | |   
                    |  |//|                   | |  \/_ __ __ _  ___ _  __ _ _ __   ___   | |    _   ___   ___   _ _ __   __ _  __ _ 
                    |  |//|                   | | __| '__/ _` |/ __| |/ _` | '_ \ / _ \  | |   | | | \ \ / / | | | '_ \ / _` |/ _` |
                    |  |//|                   | |_\ \ | | (_| | (__| | (_| | | | | (_) | | |___| |_| |\ V /| |_| | | | | (_| | (_| |
                    |  |//|                    \____/_|  \__,_|\___|_|\__,_|_| |_|\___/  \_____/\__,_| \_/  \__,_|_| |_|\__, |\__,_|
                    |  |//|                                                                                              __/ |   
                    |  |//|                                                                                             |___/  
                     \   /
                      \ /
                       V''')
    print()
    print()
                                                                  
                                           
    credits_print('''                   ,adP""""""""Yba,    
                 ,dP"            `Yb,   
                ,d'    ,dP""Yb,    `Y,          _           _      ______          _      _  
               ,d"      "b,   `Y,   `8,        | |         (_)     | ___ \        | |    (_)   
                d'    _   `Y,   `8   `8        | |    _   _ _ ___  | |_/ /___   __| |_ __ _  __ _ _   _  ___  ___  
                8     8    `8    8     8       | |   | | | | / __| |    // _ \ / _` | '__| |/ _` | | | |/ _ \/ __| 
                 Y,   `b, ,aP     P    8       | |___| |_| | \__ \ | |\ \ (_) | (_| | |  | | (_| | |_| |  __/\__ \\
                `Ya    """"     d'    ,P       \_____/\__,_|_|___/ \_| \_\___/ \__,_|_|  |_|\__, |\__,_|\___||___/ 
                 `Ya         ,8"     ,P'                                                     __/ |    
                   `Ya,,__,,d"'    ,P'                                                      |___/  
                     `""""'      ,P                        
            /"""'""""'""""'""""',P                 
            \"""'""""'""""'""""' ''')

    print()
    print()        
    credits_print('''                  .~~~~`\~~\\
                  ;       ~~ \\
                  |           ;
              ,--------,______|---.             _____ _                        ______ _ _ _      
             /          \-----`    \           /  ___| |                       | ___ (_) | | 
             `.__________`-_______-'           \ `--.| |__   __ _ _   _ _ __   | |_/ /_| | | _____      _____ 
                 /   O      O   \               `--. \ '_ \ / _` | | | | '_ \  | ___ \ | | |/ _ \ \ /\ / / __|
                |                |             /\__/ / | | | (_| | |_| | | | | | |_/ / | | | (_) \ V  V /\__ \\
                :  ,          ,  :             \____/|_| |_|\__,_|\__,_|_| |_| \____/|_|_|_|\___/ \_/\_/ |___/
                 \  '-......-'  /
                  '.          .'
                    '-......-' ''')

start_game()
