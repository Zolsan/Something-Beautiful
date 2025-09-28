# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Alum", color="#cf1a1a")
define d = Character("Dog", color="#ffdbdb")
define p = Character("Perdu", color="#ffdbdb")
define f = Character("Friend", color="#609BD6")
define h = Character("Hiba", color="#609BD6")
define c = Character("Child")

$ lolipopCheck = False
$ dogLeashed = False
$ dogBurned = False
$ dogOverFence = False
$ gameEnding = 0

# The game starts here.

label start:

    play music cafe
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg cafe

    #Start of story - exposition & introduction
    "Papier Cafe"

    show alum norm stand at left
    with dissolve

    a "Phew.."
    
    "It's been a full shift so far at work. I'm just about to sit down, when.."

    "ring ring"

    f "Heyo! Alum, how's it going?"

    "Hiba calls."

    show alum norm happy at left
    with None

    "We talk for a good while."

    a "Hey, it's good to hear your voice. I'll see you soon!"

    "Hiba's coming to meet up at the cafe at four. It's three right now, so..."

    "Let's go on a walk!"
    
    scene bg street

    show alum norm stand at left
    with None

    "I start strolling down cellulose street, the sidewalk giving a nice noice with each step."

    "As I'm strolling I spot a small child with their parent."

    c "Wahh... Wahh!!"

    menu:
        "Give the kid something sweet":
            $ lolipopCheck = True 

        "Glare at the child":
            $ lolipopCheck = False
    
    if lolipopCheck == True:
        "One's colour is a powerful thing. The ability to materalize anything within your material and hue.."
        "I tend to try and use it to help others, and this is a good chance"
        "With a bit of the red in me, I create a nice red loli."
        show alum norm yeah at left
        a "Hey, fella. You want..?"
        "Not a word, but he looks at me innocently and takes it. Walking off, there are no more sounds"
        show alum norm happy at left
        "In time with good food and rest, colour and paper always heals back"
        "Did you know every thirty days, one's paper fully replaces itself?"
        "Heck, you could probably lose an arm and find it back, give or take a couple months"
        "Anywho, something small like a lolipop ain't anything to worry about."

    else:
        "One's colour is a powerful thing. The ability to materalize anything within your material and hue.."
        "I tend to try and use it to help others. I could've made a lolipop or something.."
        "But that kid don't deserve it."
        "I walk by, glaring not at the mother at all, just the child." 
        "I have standards!"
        "Our lifestuffs, the graphite upon our paper, In time with good food and rest it always replaces itself."
        "Still, only so much flesh you can give. Surely it's better used somewhere else.."

    "I keep my stroll at a steady pace."
    "Turning down willow street, I see something skedaddling in the distance.."
    show alum norm surprise at left
    show dog stand at right

    d "Arf!"

    show alum norm tired at left

    a "whatdaheck"

    "A dog! What's it doing here?"

    "I watch it run across the road and then.."

    show alum norm surprise at left  

    show dog surprise

    d "Yelp!"

    hide dog

    "The dog tumbles down a ditch into the woods!"

    show alum norm stand at left

    "I jog up to the outskirts to a cross fence, the barrier of the woods."

    a "How did the dog get over this fence..\?"

    "I lean over the fence, looking for the dog."

    a "Hey!! uh... Dog!! You okay\?"

    "I suppose I lean in too far, because..."

    stop music
    scene bg nadda
    "Fwoomp!"

    scene bg forest
    play music forest
    show alum norm tired at left

    a "Oof..."

    a "What... "

    show alum norm stand at left

    "That was a big tumble.. Still in one piece though."

    a "I really came here because of some silly dog, huh? Might as well look for it"

    "I end up walking, calling for the dog. It takes a little bit of wandering off..."

    show dog stand at right

    "Eventually I spot the dog. Slowly I approach it.."

    show alum stand at center

    a "Here, dog..."

    a "There! Hey.... boy? girl?"

    a "This distinction isn't important."

    d "Woof!"

    "I don't want this fella getting away."

    "A leash will help. Maybe just a bit of red would be worth it.."

    menu:
        "Produce a leash":
            $ dogLeashed = True
        
        "Go without a leash":
            $ dogLeashed = False

    if dogLeashed == True:
        "It's probably worth it."

        "Using some red, I generate a nice simple red leash and get it around the dog's neck."

    elif dogLeashed == False:
        "It's probably worth saving myself. I'll keep an eye on him.."

    a "c'mon lil doggy. Let's get out of this place."

    if dogLeashed == False:

        show dog surprise
        d "Rrrrroof!"

        show alum norm surprise at left

        "The dog dashes off, deeper into the forest."

        a "Hey!"

        show alum norm stand at left

        "I give chase!"

        "The dog weaves deeper into the forest, jumping over fallen trees, breezing past riversides"

        "I stumble somewhat near, trying to follow behind."

        "Oof!"

        "Ow!"

        show dog stand at right

        d "Rrrrroof!"

        a "Gotcha! You-"

        show alum norm surprise

        "\"Splash\""

        "The river between us is missed by me, ending in my plummet into it."

        hide alum

        a "Ah.. I'm soaked.."

        show alum norm tired at left

        "I stand there, beaten by branches and dripping of water."

        "The dog doesn't move while I drag myself out. It stands on the other end and watches.."

        show dog stand at center

        "In a moment of quiet, it quickly gets over to me to sniff."

        show alum norm yeah at left

        a "Gotcha."

        "This time I procure the leash and quickly get the dog hooked on."

        show alum norm stand

        a "I'm not losing you again.. Stick with me." 

    else:

        d "Roof!"

    scene bg forest clearing

    "Slowly, we make it closer to the clearing."

    "The dog looks skiddish. Each step is overly light, and every now and then it gives a shiver."

    if dogLeashed == True:

        show alum norm stand at left
        show dog stand at right

        a "You cold buddy?"
        "We've been walking for a while now. Rest would be smart, even if just for a bit."
        "Let's see..."
    else:

        show alum norm tired at left
        show dog stand at right

        a "You cold?"
        a "....Me too."
        "Maybe we're in need of a rest"

    "Carefully.. I try to set up a small fire."

    "Little bits of paper from my fringes make a good firestarter. Just like colour, this stuff grows back, eventually.."

    show fire right

    a "Just a bit for now.. Hopefully this helps, eh?"

    show alum norm stand at left
    show dog stand at right
    "I sit down near the fire, and eventually the the dog settles down as well."

    a "Phew, this is nice.."

    a "You know, I've been wanting to get something to call you other than just \'dog\'. "

    show alum norm yeah at left

    a "I think I'll call you perdu! Okay?"

    p "rrrowf!"

    show alum norm happy at left

    a "Perdu it is."

    #Path 3 4 & 5

    if dogLeashed == True:
        "Some time passes. Until..."

        show alum norm stand at left

        a "Hey Perdu, move away from the fire. That's too close.."

        p "..."

        show alum norm surprise at left
        show dog fire at right

        p "Whine!"

        a "Perdu!!"

        "He's caught on fire! What do I do??"

        menu:
            "Use paper to smother the fire":
                $ dogBurned = False

            "Do nothing":
                $ dogBurned = True
            
        if dogBurned == True:

            stop music fadeout 1.0
            
            show alum norm stand at left
            hide dog

            "I watch as the dog burns."

            "Bit by bit, until all that's left is black ash."

            a "..."

            "I walk back to wherr I came, to the fence of the forest."

            "Up, over the fence I lift myself."

            scene bg street

            "Back down Willow street, turning down Cellulose street."

            "Back to the Papier Cafe."

            scene bg cafe
            play music cafe

            "It's Four thirty."

            h "Yo Alum! Where've you been? I tried calling you."

            show alum norm stand

            "..."

            $ gameEnding = 5


        elif dogBurned == False:
            hide alum
            hide dog
            "In a move of panic, I grab a large part of me and smother the fire on the dog."

            show dog patched stand at right
            p "Ruff!"

            show alum 1arm tired at left

            "Phew.. Could've lost you buddy."

            show alum 1arm stand at left

            "Oh."

            "Well... It was probably worth it. I'm just glad you're okay, buddy."

            "The dog licks where my arm below the elbow used to be."

            a "Thank you..."

            show alum 1arm tired at left

            a "Let's just get out of here."

            hide alum

            "We make it to the fence where this all began."

            show alum 1arm stand at left

            a "I don't think... both of us can make it over this thing at the same time..."

            menu:
                "Go over without Perdu":
                    $ dogOverFence = False

                "Get Perdu over":
                    $ dogOverFence = True
            
            if dogOverFence == True:
                
                a "Perdu, you go over. Go.. find some help! Please!"

                show dog patched stand at right
                a "Roof!"

                "I'm just able to lift Perdu over the fence. He looks back at me."

                a "Go buddy! Go find help!"

                hide dog

                "After a little bit on innocent hesitation, the fellow skedadles just like he had earlier today."

                show alum 1arm tired at center

                a "Phew..."

                "Just wait for a little bit... I'll find a way around worse case."

                scene bg street

                "It's five thirty."

                "I hear the prancing of a dog coming closer, along with separate set of footsteps."

                "Who is that..?"

                h "Hey! Friendo!"

                "Hiba comes up to the fence."

                h "Alum! What are you doing here? ...Where did your arm go?"

                show alum 1arm tired at center

                a "Eh.. It's a long story.."

                "Hiba helps me over the fence, out of this whole mess."

                $ gameEnding = 4
            elif dogOverFence == False:

                "With the best of my efforts, I manage to get myself over the fence"

                a "You stay here buddy... okay?"

                a "I'll be back! So please! Stay! Okay?"

                scene bg street

                "The dog whines. Slowly.. I back away."

                scene bg cafe

                "I spot Hiba immediately at an empty booth"

                show alum 1arm surprise at center
                
                a "Hiba! Follow me!"

                h "Yo 'lum? What's going-"

                a "Just come!"

                scene bg street

                "I grab Hiba with my good arm and run back down Cellulose street, down the turn to Willow Street, Hiba close behind."

                show alum 1arm tired at center

                a "Perdu! We're here!"

                h "Perdu? What's going on?"

                a "Long story, but there's a dog stuck back here. And he's..."

                show alum 1arm stand at center

                a "Gone."

                h "Ah man.. Alum."

                h "Look, we'll have to come back and look for him."

                h "I think right now we need to you get your some.. attention. Let's rest, okay? Tell me the story."

                h "Soon. We'll be back for him, I promise."

                show alum 1arm tired at center

                a "...."

                a "Okay."

                $ gameEnding = 3  

    elif dogLeashed == False:

        a "Yawwwn.."

        "Quite the calming fire.."

        show alum norm tired at left

        "Might doze off for a bit."

        "I close my eyes. It's a sweet quiet darkness with the ambience of fire."

        "That is until.."

        show dog surprise at right
        
        p "Bark! Bark Bark!!"

        a "...-huh? whaA"

        "My arm's on fire!"

        hide alum

        "Perdu jumps back and forth as I wave around my arm. Eventually it gets out.."

        show alum 1arm tired at left

        a "Whew.."

        "The dog licks what's left after the flames go out."

        "Ouch.. It's.."

        "Let's get out of here."

        scene bg forest 

        "Eventually, we finally make it to the fateful gate that got us here in the first place."
        
        show alum 1arm tired at center

        "Perdu... I don't think I can get both of us over..."

        menu:
                "Go over without Perdu":
                    $ dogOverFence = False

                "Get Perdu over":
                    $ dogOverFence = True
            
        if dogOverFence == True:
                
            a "Perdu, you go over. Go.. find some help! Please!"
                
            show dog stand at right
            a "Roof!"

            "I'm just able to lift Perdu over the fence. He looks back at me."

            a "Go buddy! Go find help!"

            hide dog

            "Perdu runs off. Hopefully for help.."

            show alum 1arm tired at left

            a "I think I'll.. Lay down for a minute while wait."

            "I slump onto the moist soil."

            "Just for a minute.."

            "Pretty quickly I drift off. Without much more to give.."

            "Lights out."

            $ gameEnding = 2

        elif dogOverFence == False:

            a"I'm.. going to go get help."

            a"Please... Perdu. You stay here."

            "Slowly, I struggle over the fence."

            "Attempt after attempt, finally I end up tumbling over the other end onto the ground."

            scene bg street

            "Slowly, I make my way to help."

            "Step by step, trying to keep my balance, holding the remaining elbow."

            scene bg cafe

            "It's around 5.."

            "I spot Hiba at an open both. He looks at me with concern and gets up."

            h "Alum! Hey..? Girl, what happened?"

            show alum 1arm tired at center

            a "I.. need some help."

            "Before I can explain, I trip on the floorboards."

            "Everything goes black."

            $ gameEnding = 1

        scene bg nadda

        if gameEnding == 1:
            show alum 1arm tired at center
            "ENDING 1"
            "You made it out. Just barely."
            "The dog... You'll never know." 
        
        elif gameEnding == 2:
            show alum 1arm tired at center
            "ENDING 2"
            "Your kindness grants the dog another chance."
            "Now here you rest."

        elif gameEnding == 3:
            show alum 1arm stand at center
            "ENDING 3"
            "You made it out."
            "The dog will too... In time."

        elif gameEnding == 4:
            show alum 1arm stand at center
            "ENDING 4"
            "You and the dog, with Hiba's help are all safe."
        
        elif gameEnding == 5:
            show alum norm tired at center
            "ENDING 5"
            "You make it out."
            "By your choice, you make it out alone."

        "Sacrifices had to be made."
            
















    # This ends the game.
    return
