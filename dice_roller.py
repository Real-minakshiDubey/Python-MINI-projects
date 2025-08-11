print("hi welcome to the game of dice roller,here i will roll the dice and " 
"you have to guess the number in the dice from 1 to 6");
print("So,LETS START...");
print("i am rolling the dice...");

import random
num=random.randint(1,6)
guess=int(input("guess a number between 1 to 6 : "));
while(num!=guess):
    print("oh no!,you guessed it wrong");
    guess=int(input("try again!, guess a number between 1 to 6 : "));
  
print("congo!you guessed it right.")


   