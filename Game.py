print('***********************************************************************************************')
print('King Arthur was a decent man and was elected by the people because of his justice and good character')
print('His Step brother was jealous of him and wanted to defeat him')
print('He has attcaked the kingdom and you are given the task to defeat him')
print('On doing so you will be rewarded and married to the daughter of the King Arthur')
print('Go Show your POWER and defeat his brother Ilmerith')#this is the story
print('***********************************************************************************************')
#Note
#enhancments made by me are changing Reactions of Different Results
#And made them more Humourous
import random #importing the random function from library

lives = 5
score = 0

while lives > 0:
    print('Pick a Weapon To Defeat it ! ')
    print('1...Sword                         Damage: 400 Success Rate:20%  \n2...Dagger                        Damage: 1000 Success Rate:10% \n3...Holy Hand Grenade of Antioch  Damage:100 Success Rate:90% \n4...Axe                           Damage:2000 Success Rate:5% \n5...SHAZEL THE WARRIOR            Damage:500 Success Rate: 50%')
    print('Choose the Number of Weapon ! BE WISE ! ') # This is the Menu given to User
    weapon = int(input())
    
    r = random.randrange(100)   
    # here r randomize itself within 100
    if weapon == 1: #Sword
        print('***********************************************************************************************')
        print('You have choosen the Sword')
        if r < 20: #20% chance #400 damage
          print('Good Hogya G You Killed the Rabbit')#success 
          score = score + 400
        else:
          print('You are Dead, perhaps you are not worthy for the sword')#failure
          lives = lives - 1
        print('***********************************************************************************************')
        print('Remaining lives are', lives)
        print('Your score is', score)
        print('***********************************************************************************************')
    elif weapon == 2: #Dagger
        print('You have choosen Dagger')
        if r < 10: #10% Chance #1000
          print('Good Hogya G You Killed the Rabbit')#success
          score = score + 1000
        else:
          print('You are Dead, you cant even use a dagger SHAME!')#FAILURE
          lives = lives - 1
        print('***********************************************************************************************')
        print('Remaining lives are', lives)
        print('Your score is', score)
        print('***********************************************************************************************')
    elif weapon == 3: #Grenade
        print('You have choosen Grenade')
        if r < 90: #90% chance #100
          print('Good Hogya G You Killed the Rabbit')#success
          score = score + 100
        else:
          print('You are Dead, couldnt even throw a grenade? mazaq e?')#failure
          lives = lives - 1
        print('***********************************************************************************************')
        print('Remaining lives are', lives)
        print('Your score is', score)
        print('***********************************************************************************************')
    elif weapon == 4: #axe
        print('You have choosen Axe')
        if r < 5: #5% chance #2000
          print('AMAZING!!!!!! You Killed the Rabbit LEGENDARY MOVE')#SUCCESS
          score = score + 2000    
        else:
          print('You are Dead, DID U REALLY THINK U COULD EVEN PICK THAT UP?')#FAILURE
          lives = lives - 1
        print('***********************************************************************************************')
        print('Remaining lives are', lives)
        print('Your score is', score)
        print('***********************************************************************************************')
    elif weapon == 5: #SHAZEL
        print('You have choosen TO GET HELP FROM SHAZEL THE WARRIOR')
        if r < 50: #50% chance #500
          print('SHAZEL helped Kill the Rabbit \nLong live the Warrior')
          score = score + 500
        else:
          print('You are Dead, abhi bhi waqt hai bhag jaa!')
          lives = lives - 1
        print('***********************************************************************************************')
        print('Remaining lives are', lives)
        print('Your score is', score)
        print('***********************************************************************************************')
    else: 
        print('***********************************************************************************************')
        
        print('Select a valid weapon warna tu mera putar chutty kar')
        print('***********************************************************************************************')
        print('***********************************************************************************************')
print('\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n Game Over')
print('Your Score is:' ,score)
print('***********************************************************************************************')

            
    
    
