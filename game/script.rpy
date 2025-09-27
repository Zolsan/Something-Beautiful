# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Alum", color="#FFFFFF")
define f = Character("Friend", color="#609BD6")
define c = Character("Child")

$ lolipopCheck = False
$ danger1 = True
$ danger2 = True
$ danger3 = True

# The game starts here.

label start:

    play music cafe
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg cafe

    #Start of story - exposition & introduction
    "Papier Cafe"

    show alum proto at left
    with dissolve

    a "Phew.."
    
    "It's been a full shift so far at work. I'm just about to sit down, when.."

    "ring ring"

    f "Heyo! Alum, how's it going?"

    "Hiba calls."

    "We talk for a good while."

    a "Hey, it's good to hear your voice. I'll see you soon!"

    "Hiba's coming to meet up at the cafe at 4. It's 3 right now, so..."

    "Let's go on a walk!"
    
    scene bg street

    show alum proto at left
    with dissolve

    "I start strolling down cellulose street, the sidewalk giving a light crinkle with each step."

    "As I'm strolling I spot a small child with their parent."

    c "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

    menu:
        "Give the kid something sweet":
            $ lolipopCheck = True 

        "Glare at the child":
            $ lolipopCheck = False
    
    if lolipopCheck == True:
        "I give the kid some candy or something"

    else:
        "That kid don't deserve it."
    # These display lines of dialogue.



    # This ends the game.
    return
