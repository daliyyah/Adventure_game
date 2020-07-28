import time

import random

enemy = random.choice(["troll", "dragon", "pirate", "wicked fairie", "gorgon"])


def pause(message):
    print(message)
    time.sleep(2)


def intro():
    pause("You find yourself standing in\
an open field, filled with \
grass and yellow wildflowers.\n")
    pause(f"Rumor has it that a {enemy} is \
somewhere around here, \
and has been terrifying \
the nearby village.\n")
    pause("In front of you is a house.\n")
    pause("To your right is a dark cave.\n")
    pause("In your hand you hold your \
trusty (but not very \
effective) dagger.\n")


def play_again(sword):
    answer = input("Would you like to play again? (y/n)").lower()
    while True:
        if answer == "n":
            pause("Thanks for playing! See you next time.")
            break
        elif answer == "y":
            pause("Excellent! Restarting the game ...")
            intro()
            path_choice(sword)
            break
        else:
            play_again(sword)


def fight_flee(sword):
    options = input("Would you like to (1) fight or (2) run away?\n")
    if options == "2":
        pause("You run back into the field. \
Luckily, you don't seem \
to have been followed.")
        path_choice(sword)
    elif options == "1":
        if "the magical Sword of Ogoroth" in sword:
            pause(f"As the {enemy} moves \
to attack, you unsheath \
your new sword.")
            pause("The Sword of Ogoroth shines \
brightly in your hand as you brace \
yourself for the attack.")
            pause(f"But the {enemy} takes one \
look at your shiny new \
toy and runs away!")
            pause(f"You have rid the town of the {enemy}. \
You are victorious!")
            play_again(sword)
        else:
            pause("You do your best...")
            pause(f"but your dagger is no match for the {enemy}.")
            pause("You have been defeated!")
            play_again(sword)
    else:
        fight_flee(sword)


def choice1(sword):
    pause("You approach the door of the house.")
    pause(f"You are about to knock when \
the door opens and out steps a {enemy}.")
    pause(f"Eep! This is the {enemy}'s house!")
    pause(f"The {enemy} attacks you!")
    pause("You feel a bit under-prepared for this...")
    fight_flee(sword)


def choice2(sword):
    if "the magical Sword of Ogoroth" in sword:
        pause("You peer cautiously into the cave.")
        pause("You've been here before,\
and gotten all the good stuff.\
It's just an empty cave now.")
        pause("You walk back out to the field.")
    else:
        pause("You peer cautiously into the cave.")
        pause("It turns out to be only a very small cave.")
        pause("Your eye catches a glint of metal behind a rock.")
        pause("You have found the magical Sword of Ogoroth!")
        pause("You discard your silly old dagger \
and take the sword with you.")
        pause("You walk back out to the field.")
        sword.append("the magical Sword of Ogoroth")
    path_choice(sword)


def path_choice(sword):
    choice = input("Enter 1 to knock on the door of the house.\n\
Enter 2 to peer into the cave.\n\
What would you like to do?\n\
(Please enter 1 or 2.)\n")
    while True:
        if choice == "1":
            choice1(sword)
            break
        elif choice == "2":
            choice2(sword)
            break
        else:
            path_choice(sword)


def play_game():
    sword = []
    intro()
    path_choice(sword)


play_game()
