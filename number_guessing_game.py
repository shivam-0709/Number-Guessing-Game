print('*****This is a number guessing game ****')

print ('Please choose level "1 for easy or 2 for hard"')
print ('For hard 5 chances for easy 10 chances')



import random

while True:
    try:
        level = int (input('**Let us play the game please type  ** --  '))

    except ValueError:
        print ("Please type 1 or 2 only")
        continue



    a = random.randint(1,100)

    if level == 1:
        chance = 6
    elif level == 2:
        chance = 11
    else:
        print ("Please enter 1 or 2 only")
        continue

    for i in range  (chance):
        print(f'Chances left-- {chance-1}')
        chance = chance-1
        if chance == 0:
            break

        

        try:
            b = int(input('Guess the number -  '))
        
        except ValueError:
            print('Please enter the number in range of 1 to 100 only, Lets Play again')
            break


        if a == b:
            print('Guess correctly')
            break

        elif a >= b:
            print ('Number is less try again')
            continue

        elif b >= a:
            print('Number is big try again')
            continue

        else:
            print ('failed')

            

    again = input('Wanna play again press "y for YES"  ')
    if again == 'y':
        continue
    else:
        break

print ("aa gaye game se bahar khelan ke liye thanks")