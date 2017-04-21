
print ("You walk down a wooded path, the dark trees blocking your view of the three paths you just arrived at. Standing at the junction, you notice the first path curves away, the second is straight but dark, and the third has a cool breeze coming out of it.")
print ("Which path do you choose? 1, 2, or 3?")
path = input("> ")

if path == "1":
    print ("Your travels bring you to a decrepit old man, sitting on a log. He appears to be eating a squirrel. He turns to you and asks: \"Answer me this riddle, and I shall let you live. 'You will always find me in the past. I can be created in the present, but the future can never taint me. What am I?'")
    print ("1 = Time, 2 = History, 3 = Pancakes")
    riddle = input("> ")
    if riddle == "2":
        print ("You may pass, I detect a great heroism within you.")
        print ("You continue on your journey, and find yourself on a cliff. Hearing a roar in front you, you are startled to see a dragon rise from beneath the cliff. He burns you to a crisp. ")
    else:
        print ("The old man jumps from his log, and grabbing his staff, he shoots you with a lightning bolt. You are super super dead.")
if path == "2":
    print ("The dark path is treachorous, so you want to make a torch from a tree branch. Upon lighting it, you see many glittering eyes in the woods. Do you: 1) Flee back to the path entrance, 2) Keep forging forward, or 3) fashion a spear and attempt to fight?")
    eyes = input("> ")
    if eyes == "1":
        print ("The creatures chase you, you can hear them tearing through the forest. It seems like you have been running far longer than you were walking. Apparently the forest has sealed you in. You die after being devoured and enjoyed thoroughly by the monstrous creatures.")
    if eyes == "2":
        print ("You run forward, and find yourself at the bottom of a cliff. A dragon flys overhead but doesn't notice you. You made it!")
    if eyes == "3":
        print ("How are you going to fashion a spear without a knife? You're eaten by the creatures.")
if path == "3":
    print ("You walk for a while, and find a simple golden ring laying on the ground. You place it in your pocket, and continue on your way. You come upon a pathetic little creature, scurrying around on all fours. He snaps his head around at you and asks:\"Where is she? Where is my precious!? She's a small golden ring and the love of my life!")
    print ("1: It's right here little guy, 2: No idea buddy, sorry, 3: *beat the crap out of him* ")
    gollem = input("> ")
    if gollem == "1":
        print ("Like a drug addict, the creature lunges for you, and bites your finger off in his gambit for the ring. You die of an infected wound a few days later. Nice.")
    if gollem == "2":
        print ("The creature doesn't seem to believe you. He chases you, and when you trip on a rock, the ring flies into the air with a mind of its own and lands on your finger. All of a sudden you're invisible. Guess it's time to go home. Nice!")
    if gollem == "3":
        print ("A passing orc patrol hears the ruckus. They come and kill you, feeling the power of the ring. They return the ring to Mordor, and Sauron uses its power to reclaim his rule over all of Arda. Congratulations.")
