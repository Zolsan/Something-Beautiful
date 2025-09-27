# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define s = Character("Friend A")


# The game starts here.

label start:

    play music cafe
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"
    
    s "That'll be cool."
    # This ends the game.
menu:

    e "Where will you go next?"

    "Forest"
    jump forest 

    "Cafe"
    jump cafe

label forest:

    s "forest it is."

label cafe:

    s "cafe sounds good."





    return
