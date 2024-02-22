#Text based choices three level deep in any scenario.
#Additional Creativity:
# Made the scenarios and choices more interactive. Styling was game-like
#Used upper() option inside the input function, instead of creating a new variable to hold the uppercase of the first variable.
# Used the special new-line character, \n. 

print("Congratulations traveler, you have made it to New-Bay Utopia.")
#title_1 = "Mage"
#title_2 = "Sword Saint"
#title_3 = "Body Builder"
alli = "Mage Swordsman Body-Builder"
title = input(f"Please choose your beginner's path to glory \n {alli.upper()} \n What do you want to be?: ")
rtitle = title.lower()

#Second phase of choice: Paths under Mage

if rtitle == 'mage':
    print("\nYou chose the mage route")

    mage_choices = "Academy, Forest, Mage Tower"
    utopia_choices = input(f"Mage, please choose where you would like to be transported to \n{mage_choices.upper()}?: ")
    rutopia_choices = utopia_choices.lower()
#Academy Choice
    if rutopia_choices == "academy":
        print("A good choice, but wait, you don't have money to pay your entrance fee. But don't fret!")

        academy_choices = "a: Sit for a King's private scholarship \n b: Find a way to make money from taking quests \n c: show your competency to a teacher and pass his test."
        academy = input(f"There's a way out of this: \n{academy_choices.upper()}\n Please pick your choice: ")
        racademy = academy.lower()

        if racademy == "a":
            print("The king of nerve cells is compassionate enough to give free schlarships to poor children... you just have to sign a lifelong contract with the royal family.")
        
        elif racademy == "b":
            print("Quest are a good way for poor people to earn money and reputation... and most poeple take these dangerous quests for that, even if they die")
        
        elif racademy == "c":
            print("There are countless bored teachers around, show them your skills")
        else:
            print("Typo at the first part, the academy part.")

#Forest Choice
    elif rutopia_choices == "forest":
        print("You appear in the evernor forest, but you hear the sound of intense fighting. What should you do?")

        forest_choices = "A: Help them \n B: Go far away \n C: Hide and access the situation"
        forest = input(f"Three choices present before you are \n {forest_choices.upper()},\n please choose wisely: ")
        rforest = forest.lower()

        if rforest == "a":
            print("You go to help them with the vigor of youth. The opponent they are facing is the ferocious spike tiger, all of you barely have a chance, i mean barely.")
        
        elif rforest == "b":
            print("Your life is considered precious. But when going far away, one of them sees, and marks you. Be careful now.")

        elif rforest == "c":
            print("hide, don't let the tiger see you, or the bloodthirsty fighters")

        else:
            print("Typo at forest. Recheck.")

#Mage tower choice
    elif rutopia_choices == "mage tower":
        tower_choices = "A: Join the caravan to protest against the tryant mage \n B: Safe the Tryant \n C: Loot the mage tower"

        print("The Mage tower is current being besieged by some mecenaries. They claim the mage is an evil person. It's up to you to decide theirs, yours, and the mage's fate")
        final_tower = input(f"The choices present before you are: \n {tower_choices.upper()} \n Make your choice: ")
        rfinal_tower = final_tower.lower()
#Final Tower Choice
        if rfinal_tower == "a":
            print("The tryant suddenly burst out with unimaginable power and destroys everything. You should know, for a mage to have a tower, his strength is ten times as much as a teacher in the academy")

        elif final_tower == "b":
            print("The Mage say he was falsely accused, and this was an act orchestrated by his enemy.")
        
        elif final_tower == "c":
            print("You are badly defeated and hung for being a criminal. the city frown upon thieves")

        else:
            print("You seem to type badly")
    else:
        print("You wrote a wrong choice under mage")
# Swordsman

elif rtitle == "swordsman":
    sword_route = "A: King's Martial Arena \n B: One-Sword Martial School \n C: Go for a Quest"

    print("\nYou chose the swordsman route")
    sword_choice = input(f"A swordman must not look back. Before you are three choices... \n {sword_route.upper()} \n Follow your heart and pick a letter: ")
    rsword_choice = sword_choice.lower()

    if rsword_choice == "a":
        print("The king's martial arena is an annual battle event that brings all the experts and has generous rewards")

        arena_choice = " a: be bold and register, let the world see your stength. \n b: be the darkhorse that shocks everyone. \n c: dont participate but instead bet on the fighters."
        rarena_choice = arena_choice.upper()

        arena = input(f"You have enough strength to shock everyone, but your victory is not assured. You can choose to: \n {rarena_choice}\n Choose a letter: ")
        rarena = arena.lower()

        if rarena == "a":
            print("Get ready to begin your first match")

        elif rarena == "b":
            print("People are unsure about the real identity this darkhorse, and the true power he has. Can you shock them?")

        elif rarena == "c":
            print("The betting area is filled with crooks who only cheat their way to riches, but your intellect may surpass them. Check the odds of winnings of the players and bet.")

        else:
            print("OOps, you made a typo at the martial arena choice. Retry")
        

    elif rsword_choice == "b":
        print("The one sword martial school is a school that trains swordsmen. Made of the best swrodsmen. Choosing the One-sword Martial School, you are gifted with a treasure map, the location of the treasure is in the school")
        school_choice = "a: sell the map \n b: enter the school as a student \n c: meet an information broker to find the real location of the treasure"
        rschool_choice = school_choice

        school = input(f"The treasure map points to a large area within the school, your choices are; \n {rschool_choice.upper()} \n Choose a letter: ")
        rschool = school.lower()

        if rschool == "a":
            print("You can sell the map, but no one will believe it is authentic, reducing the value. You loose")

        elif rschool == "b":
            print("You registered sucessfully, but realize that the area is larger than you think, and that place is resricted. Well, with time, may fortune come upon you")

        elif rschool == "c":
            print("The broker doesn't believe you at first, but when he does, his eyes shines with greed.")

        else:
            print("there must be a typo mistake, please check one-sword martial school again.")


    elif rsword_choice =="c":
        print("You choose to go for a quest directly. You have appeared in the mountain range flowing with beasts of different strength.")

        quest_choice = "a: enter the cave and take  a peek \n b: visit a nearby town to buy materials \n c: forget about the cave and explore the forest"
        quest = input(f"You suddenly see a cave with strange cravings at the entrance, should you: \n{quest_choice.upper()} \n Please choose a letter: ")
        rquest = quest.lower()

        if rquest == "a":
            print("As a true adventurer and swordsman, you should face danger bravely. But a word of advice: 'Foolishness can often times be confused for bravery")

        elif rquest == "b":
            print("What ever is in the cave can always wait until you are prepared, right? But can it? And, if it cannot wait, what if it decides to come out, now!?")

        elif rquest == "c":
            print("Your eyes are not stainted with the allure of treasure. But as an adventurer...")

        else:
            print("Kindly check your wordings, there must be a typo somewhere in the Quest.")
        
    else:
        print("Check typos on entire swordsman.")


elif rtitle == "body-builder":
    print("Your body building journey begins. As a body builder, your muscles and bones are your real strength.")

    body_choice = "a: exercise \n b: Go to china to learn Inner Origin kunfu \n c: go to japan to learn snake judo"
    body = input(f"Choose a path to find your real strength, \n {body_choice.upper()}\n Please choose a letter: ")
    rbody = body.lower()

    if rbody == "a":
        print("With strenous exercise your muscles can become strong to lift towers and castles.")

        exercise_choice = "a: full body exercise \n b: one part focus \n c: calistenics and meditation"
        exercise = input(f"Body building through exercise has three part:\n {exercise_choice.upper()} \n Choose a letter")
        rexercise = exercise.lower()

        if rexercise == "a":
            print("You decide to do a full body workout. take an adventure to the west to unlock your body potential")

        if rexercise == "b":
            print("focusing on a part until you reach the best state, take a journey to the mountains")

        if rexercise == "c":
            print("calistenics and meditation is best in Korea. start your journey")
            
        else:
            print("typo at body exercise. please correct it")
        
    elif rbody == "b":
        print("Inner Origin kunfu is practised in china. You reached China, but there are choices ahead of you.")

        kunfu_choices = "a: learn with the mountain hermits \n b: learn with a monk temple \n c: explore the ruined city of quanshi"
        kunfu = input(f"{kunfu_choices.upper()}\n Please pick a letter.")
        rkunfu = kunfu.lower()

        if rkunfu == "a":
            print("Learning with the mountain hermits is a path for soltary heroes, but can you convince the hermits to accept you?")

        elif rkunfu == "b":
            print("With the monks, the stable foundation can be built. You have to first passed their test.")

        elif rkunfu == "c":
            print("Quanshi city has lost books and methods that can greatly increase your strength, but how certain is this rumor?")

        else:
            print("Typo somewhere at Origin Kunfu. please recheck answers")

    elif rbody == 'c':
        print("snake jutsu teaches fastness, exploring the explosive speed of the body")

        jutsu_choices = "a: meet the water tribe \n b: find bobby, take him as your tutor \n c: find bobby, let both of explore japan."
        jutsu = input(f"The choices to eplore in japan are: \n {jutsu_choices.upper()} \n choose a letter. bobby is important: ")
        rjutsu = jutsu.lower()

        if rjutsu == "a":
            print("The water tribe are a canivorous tribe. If you were with bobby...")

        elif rjutsu == "b":
            print("You find bobby, but he is saddened by his past and rebukes you. How can you convince him to teach you?")

        elif rjutsu == "c":
            print("Bobby's eyes spark when he hears of an adventure. But what do the cruel world hold for both of you?")

        else:
            print("type at Jutsu, recheck")
    else:
        print("Typo at somewhere at the entire body builing person. recheck.")

else:
    print("The grandfather typo. This should be at the start and through.")


