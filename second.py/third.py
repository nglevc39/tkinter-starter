def clear(): 
    from os import system, name 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 

    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')
clear()
 
answer1 = input("Welcome to The Invasion, would you like to get started?")
if answer1 == "no":
  print(" Why are you here.")
else:
  print("Welcome, you will play as Sergeant Gleb. You are part of the United Nations Space Command defending against the invading Aliens called the Covenant. The Covenant is made up of different species of aliens. Grunts= Canon Fodder. Elites= Warriros  ")
  print("You are stationed at Outpost Delta 1, you need to use the bathroom but your squad needs to be sent out for a patrol.")
  
 
 
choice1 = input("Do you use the bathroom or go out with your squad? Choose 1 or 2.")
if choice1 == "1":
 choice2 = input("You go to use the bathroom and tell your squad to wait for you, you reach the bathroom.Should you use the (1) uniral or the (2) uniral?")
if choice2="2":
 print("You go to use the 2nd uniral, a plasma ball rips through the cieling and kills you. Game Over.")
if choice2 == "1":
 choice3=input("you use the 1st uniral, you empty your bladder. you zip up and go wash to wash your hands. Right as you were about to wash your hands something rips through the cieling and crashes into the 2nd uniral.You see the strange object is a plasma ball, used by the covenant. Should you run out(1) or examine it closer.?(2)")
if choice3 == "2":
   print("You examine it closer and you see a plasma rifle, you pick it up and the ball explodes. Game Over.")
if choice3 == "1":
 choice4=input("You run out of the bathroom, you and make it outside, you see Covenant ships floating over your head, and dropping troops. Your squad is no where insight, should you flee the action(1) or get closer to the enemy troops?(2)")
if choice4 == "2":
if choice4 == "1":
   print("You flee the action, and run into the city.")
 choice5=input("You get closer to the troops, the firing starts to get more intense the closer you get. You see a pack of grunts and a Elite leading them. Should you ignore them(1) or open fire(2).")
if choice5 == "1":
 choice6=("You ignore the aliens and run around them. You start to quickly realize that theres a UNSC chopper evacuating soldiers, maybe your squad is on there. Should you hop on(1) or stay and keep looking?(2) ")
if choice6 == "1":
 choice7=input("You run to hop on the helicopter but your squad hops out and one of them says, Sir sorry for leaving you, but we are here now! You were about to say something but a covenant speder rams into you. A squad of Grunts and a Elite leading them charges you. You fall back but your squad is still fighting, should you go back in there or find a weapon?(2)")
if choice7 == "2":
 choice8=input("You run to find a better weapon, you see a plasma rifle on the floor, you figure out how to use it. You go back and open fire on the Grunts and they soon fall back. You and your squad regroup and you see another dropship drop off a Covenant General. He drops down with his troops, Both sides engage. You and the General engage in 1v1 combat, he whips out his energy sword. You have a combat knife, Should you run up and go for a attack?(1) Or Wait for him(2)")
 print("░░░░░░░░░░░░░░░░░░░░░░░▄▄██▀▀░░░░░░▀███░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░▐░░░░░░░░")
 print("░░░░░░░░░░░░░░░░░░░░░░░███░░░░░░█░░░░░▀██▄░░░░░░░░░░░░░░░░░░░░░▄█▄▀░█░░░░░░░░")
 print("░░░░░░░░░░░░░░░░░░░░░▐██░░░░░░░░█░░░░░░░████░░░░░░░░░░░░░░░░▄▀▀▀▀█░░░█▀█░░░░░")
 print("░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░█░░░░▐▄█░██▌░░░░░░░░░░░░░░░█░░░░░░█▄█░░▐░░░░░")
 print("░░░░░░░░░░░░░░░░░░░░░███░░░░░█▄▄█▄▄░░░██▄░██░░░░░░░░░░░░░░█░░░░░▄█░░░▀▄█░░░░░")
 print("░░░░░░░░░░░░░░░░░░░░░███▀▀▀▀▀▀░░█▄░▀▀███▄▄██░░░░░░░░░░░░░░▌░░░░█░░░░░▐▌█▀█░░░")
 print("░░░░░░░░░░░░░░░░░░░░░██░░▄▄█░░░▐▄█░░░▄▄▀█░░█▌░░░░░░░░░░░░░░░░░▐░░░░░░░▌▐░░▌░░")
 print("░░░░░░░░░░░░░░░░░░░░░█▌▐█░░░▀█░░▄▄█▀░▄██▄░░▐▌░░░░░░░░░░░░░▌░░░▐░▄██▄░░▌▐░░▌░░")
 print("░░░░░░░░░░░░░░░░░░░░░█▌▐░░▄░░░▀▀░░░░▄▐█▀██░▐▌░░░░░░░░░░░░░██▀███▀▄░░▄█░▐░░▌░░")
 print("░░░░░░░░░░░░░░░░░░░░░▐░▐░▐██▄░░░░░▄░████▄▌░▐▌░░░░░░░░░░░░░▐█████▄░█▀█░█░██░░░")
 print("░░░░░░░░░░░░░░░░░░░░░░█░▌░▀▀█▌░░░░░███▀░░█░█░░░░░░░░░░░░░░░▀█▄▐░███░█░░▌▀░░░░")
 print("░░░░░░░░░░░░░░░░░░░░░░▐█▌░░░░░░░▄▀██░▀░░░▄▀░░░░░░░░░░░░░░░░░░░█▀▀▀█░█░░▌░░░░░")
 print("░░░░░░░░░░░░░░░░░░░░░░█░▀█▄░█▀█▀▀▀██▄▄░█▀██▄░░░░░░░░░░░░░░░░░░▐░░░▐░▀██░░░░░░")
 print("░░░░░░░░░░░░░░░░░▄▄▄█▀█░░░░██░█▄░█▄█░██░░░█░░▀█▄▄░░░░░░░░░░░░░▀▀█▄█▀░░░░░░░░░")
 print("░░░░░░░░░░░▄▄█▀▀░░░░░░██▄▄▄██▀░░▀░░░█▀░░░░█░░░░░░▀█▄░░░░░░░░░▀░░░░░▀█░░░░░░░░")
 print("░░░░░░░░▄▀░░░░░░░░░░░░█░░░░░░█░░░░░█▀▀▀▀▀▀░▌░░░░░░░░▀█▄░░░░░▐░░░░░░░▐░░░░░░░░")
 print("░░░░░░░█░░░░░░░░░░░░░░░▐█▄▄▄▄█░░░░░█░░░░▄▄▀░░░░░░░░░░░░░█▄░░▌░░░░░░░▐░░░░░░░░")
 print("░░░░░░█▄▄▄▄▄▄▄▄▄▄▄▄▄█▀▀▀░█░░░░░░░░░░▀██▀░░░░░░░░░░░░░░░░░░█▐░░░░░░░░█░░░░░░░░")
 print("░░░░░░██▄▄▄▄▄█▀▀▀█▀▀▐░▄▄░▐▄▄▄▄▄▄▄▄▄▄█▐█▀█▀█▀▀▀▀▀▀▀▀▀▀████▀▄▌░░░░░░░░░░░░░░░░░")
 print("░░░░░▐░░░░░░░░░░░▐░░▐░░░░▐░░░░░░░░░░▐░░░█░▌░░░░░░░░░░░░░▀▀█▄░░░░░░░█░░░░░░░░░")
 print("░░░░░█░░░░░█░░░░░█░░▐▄▄▄▄█▀▀▀▀▀▌░░░░▐▄▄█░░█░░░░░░░░░░░░░░░░░▀█░░░░█░░░░░░░░░░")
 print("░░░░█░░░░░▐░░░░░░█▀▀▄▄▄▄▌░░░░░░█▄▄▄▄▄▄▄▄▄▀▐▀█▄▄░░░░░░░░░░░░░▄▀░░░█░░░░░░░░░░░")
 print("░░░█░░░░░░▌░░░░░░█▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░░░░░█░░░░▀▀▀▄▄▄▄▄▄▄▄█▀█▄▄▄█░░░░░░░░░░░░")
 print("░░░▌░░░░░█░░░░░░▐░░░░░░░░░░░░░▀▀▀▀▀▀▀▀▀▀░░▌░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
 print("░░░▌░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
if choice8 == "2":
 choice9=input("You wait for him to make a move, he sprints at you and swings, you duck and stab him in the chest. He groans and steps back. Should you take a swing at him?(1) or Wait for him to make a move?(2)")
if choice9 == "2":
 choice10=input("You wait for him to make a move, he waits for you to make a move....He gets impatient and charges you with a screem. He stops right in front of you and dosen't move. Should you attack him(1) or stay still.(2)")
if choice10 == "2":
 choice11=input("You wait and stay still, He dosen't make a move...He gets impatient and yells.You spot a Magnum on the floor, Should you go for it(1), or attack him?")
if choice11 == "1":
 choice12=input("You go for the magnum and he chaces after you, You grab the magnum and turn around. You open fire and blast his head open. You see your squad fighting, should you help them out?(1) or Leave them behind and run away.(2)")
print("░▒▒▒▒▒░░░░░░░░░░░░░░░░░▄▄██▀▀░░░░░░▀███░░░░░░░░░░░░░░░░▄▄░░░░░░░░░░░░░░")
print("░░░░░▒▒▒▒░░░░░░░░░░░░░░███░░░░░░█░░░░░▀██▄░░░░░▄▄▄████▀▀░░░░░░░░░░░░░░░")
print("░░░░░░░░▒▒▒░░░░░░░░░░▐██░░░░░░░░█░░░░░░░████▀██▄█▀▀░░░░░░░░░░░░░░░░░░░░")
print("░░░░░░░░░░░▒▒▒▀▀░░░░░██░░░░░░░░░█░░░░▐██▄███▀░░░░░░░░░░░░░░░░░░░░░░░░░░")
print("░░░░░░░░░░░░░▒▒▒░░░░░███░░░░░█▄▄█▄▄▄████▄▄██▄▄▄▄▄▄▄▄░░░░░░░░░░░░█▌░░░░░")
print("░░░░░░░░░░░░██▄░▒▒▒▀████▀▀▀▀▀▀░▄░██▀▀███▄▄██▄▄▄█▀▀██▄░░░░░░░░░░░░██░░░░")
print("░░░░░░░░░░░███░░░░▒▒▒████▄▄█░▐▒▒█▒▒▒█████▄▄██▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░")
print("░░░░░░░░░░████░░░░░░▒██████▄▄▄▄▄▒▄█▀█▄███▀▀███░░░░░░█░░░░░░░░░░▀░░░░░░░")
print("░░░░░░░░░░█████░░░░░░██▒█▄▒▒▒▒███▌▒▒▒████████░░░░░░░███▄░░░░░░░░░░░░░░░")
print("░░░░░░░░░░░▀▀▀▀░░░░░░█▄▒▒▒▒██▀▒█▀▀█▒▒█████▄██▌░░░░░░▀▀░░░░░░░░░░░░░░░░░")
print("░░░░░░░░░░░░░░░░░▄▄██████▒▒▒███▒▒▒▒███▀░░█▀█▀███▄▄▄░░░░░░░░░░░░░░░░░░░░")
print("░░░░░░░▄▄█▀▀▀███████▀▀███▒▒███▒███▀▀▀▀░░░▄▀░░░░░██████▄░░░░░░░░▀▀█░░░░░")
print("░░░░░░░░░░░░░░▀▀▀▀▀▀▀▀█▀▀████▒▒██▀███▄░█▀██▄░░░░░░░░░░▀▀░░░░░░░░░░░░░░░")
print("░░██░░░░░░░░░░░░░▄▄▄█▀█░░░░██▄████▄█▌██░░░█░░▀█▄▄░░░░░░░░░░░░░░░░░░░░░░")
print("░░██░░░░░░░▄▄█▀▀░░░░░░███▄▄████▀▀░░░█░░░░▄█░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░")
print("░░░░░░░░▄▀░░░░░░░░░▄▄████▀████▌░░░▐█░▀▀▀▀░█░░░░░░░░░▀█▄░░░░░░░░░░░░░░░░")
print("░░░░░░░█░░░░░░░▄███▀████░█████░░░░░▀▀▀▀▀▀▀░░░░░░░░░░░░░░█▄░░░░░░░░░░░░░")
print("░░░░░░█▄▄▄▄▄▄███▄████▀█▀░██░░▀█▄▄░░░▀██▀░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░")
print("░░░░░░██▄▄▄▄▄█▀▀▀█▀▀▐░████▄▄▄▄███▄▄▄█▐█▀█▀█▀▀▀▀▀▀▀▀█▀████▀░░░░░░░░░░░░░")
print("░░░░░▐░░░░░░░░░░░▐░░▐███░▐░░░██░░░░░▐░░░█░▌░░░░░░░░░▄░░░░░░░░░░░░░░░░░░")
print("░░░░░█░░░░░░░░░░░█░░██▄▄▄█▀▀▀▀▀█░░░░▐▄▄█░░█░░░░░░░░░▐░░░░░░░░░░░░░░░░░░")
print("░░░░█░░░░░░░░░░░░█▀██▄▄▄▌░░░░░░█▄▄▄▄▄▄▄▄▄▀▐▀█▄▄▄▄▄▄░░▌░░░░░░░░░░░░░░░░░")
print("░░░█░░░░░░░░░░░░░█▄█▄▄▄▄▄▄▄▄▄▄░░▀░░░░░░░█▀█▀▀▀░▀░░░░█░░░░░░░░░░░░░░░░░░")
if choice12 == "1":
 choice13=input("You go in and help your squad out, the grunts start fleeing.A Covenant dropship drops off more troops, but you see Banshee Laying around. Should you go for it,(1) or fall back with your squad to a Helicopter and evacuate?(2).")
if choice13 == "1":
 choice14=input("You go for the Banshee(Covenant flying ship for one person.) Grunts and Elites start shooting you. You barey made it past them and you climb inside the Banshee.Should you go in and target the Covenant Capital Ship(1) or fly away in peace and harmony?(2)")
if choice14 == "2":
 choice15=input("You decide to fly away peacfully and not risk your life. You see a UNSC Capital ship come in from slipspace, The Covenant Ships are now evacuating. Most of them are demolished and crash down into earth, you fly away knowing that earth is defended, you watch as the ships crash down.Press 1 to end the game.")
print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒░░░▒▀▀▀▀█████████████▀▀▀░░░░░░░░░░░░░░")
print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░▒▒▒░░░░░░████████░░░░░░░░░░░░░░░░░░░░")
print("░░░░░░░░░░▄▄▄▒▒▒░▐█▄░░▄███▌░░░░░░░░░░░░▄░▒▒█░░▒▒▒░░░░▀▀█████▄░░░░░░░░░░░░░░░░░░")
print("░░░░░░▐██▀░▒▒▒█▄░░▄████░░░░░░░░░░░░░░░████░▒▒▒▒░░░░░███████░░░░░░░░░░░░░░░░░░░░")
print("░░░░░░▐░▒▒▒░░░█▀███░░░██░░░░░░░░░░░░░░█████▒░░░░░░░░█████▀▀▀░░░░░░░░░░░░░░░░░░░")
print("░░░░░░▐▒▒░░█░░▒▒░░▀░▒▒▒░░░░░░░░░░░░▄█▀░░░░░░░░░░░░░░░░░███░░░░░░▄▄▄▄▄░░░░░░░░░░")
print("░░░░░░▐░█░▒▒▒▒▌█▄▒▒▒▒▄▄▄▄░░░░░░░░░░██░░░░░░░░░░░░░░░░░░███░░░░░░█░░░░░█░░░░░░░░")
print("░█▀▀█▀▌▒▒▒▒░▐░▌▒▒▒░▌░░░░░▌░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▐█░░░░░░░▐░░█░▀█░░░░░░░░")
print("░▌░░░░▒▒█░▐░░▒▒▌░░░▌▐░░█▐░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▌░░░░░░▐▀▀░▄▄█░░░░░░░░")
print("░▌░░▀▐░▐▐░▐▒▒░▌▌░▌░▌░▌░░▐░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░▐░█▀░░░▀█▄▄▄░░░")
print("░▌░▌░█░█▐░▒▒░░▌█░░▌▌░░░░▐░░░░░░░░░░░▄▄▄▄▄▄▄▄░░░░░░░░░░░░▐███▀█▄▄█░░░█░░░█░░░█░░")
print("░▌░▄░▌░█░▌░▌▐░▌█░░░▌░▌▀░█░░░░░░░░▄█▀░░░░░░░░░▀█░░░░░░░░░░██░▌░░█░░░█▄█░▀░░░░▐▌░")
print("▌░░░░░▐░▌░░░░▌▌░█▐░░░░░█░░░░░░░█░░░░░░░░░░░░░░▀░░░░░░░░░███░▀░▀▀▀▀▀▀▀█▀░░▄░▐░░")
print("░▌▐░░█░▐░▄░░▄░▌█░░▐░░█░▌▐░░░░░░█░░░░░░░░░░░░░░░░█░░░░░░▄░░█░░░▌░▀▀▀█░░█░░░░░▐░░")
print("░▌░░░░█░░█░░░░▌█▐░▐░░░░░░░░░░░▐░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄██▄▄▄▄▄█▄▄▄▄▄░░▄░░░░░░▐░░")
print("░░░░░▄▄█▄█▄▄▄▄▄▄▄▄██▀▀▀▀▀▀▀▀▀▀▀▀▀▀░░█████░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀▀▀▀▀▀░░")
print("░░▀▀▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄███████▄▄▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▐░░▌░░░░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
print("░░░░░░░░░░░░░░░▄██▄░░░░░░░░░░░░░█░░▌░░░░░░█░░▌░░░░░░░░░░░░▄█▀▀▀▄░░░░░░░░░░░░░░░")
print("░░░░░░░░░░░░░░░█░░░█▀▀▀█▄▄▄░░░▐▀▐░░▌░░░░░░▐░░▌▀▄░▄▄▄▄▄█▀▀█▒█▄▒▄█░░░░░░░░░░░░░░░")
print("░░░░░░░░░░░░░░▒▒▒▒█▄▄▒▄▄▄▄▒███▌░▐▄▄▀▀▀▀█▄▄█▄░▌░░█░░▄▄▒█▒▀░▒▒░▒▒░░░░░░░░░░░░░░░░")
print("░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒░▒░▒░▒░░▌░░░░░░░░░░░░░▀░░░▌░▀░░▒▒▒▒▒░▒▒▒▒▒░░░░░░░░░░░░░░░")
print("░░░░░░░░░░░░░▒▒▒▒░▒░░░░▒░▒░░░░█░░░░░░░░░░░░░░░░░▌░░░░░▒░░▒░░")
 
if choice15 == "1":
 print("Congrats on getting to the first ending!")