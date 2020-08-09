#guess =0
#while(guess<10):
#    print("guess no 1")
#    guess = guess+1
#n1 = 45
#print("Enter the number you guess")
#n1 =int(input())
#if n1 == 45:
#    print("your guess is right")
#elif n1<45:
#    print("your guess is lesser then original number")
#elif n1>45:
#    print("your guess is grater then original number ")
n=45
number_of_guesses=1
print("Number of guesses is limited to only 9 times.")
while(number_of_guesses<=9):
    guess_number = int(input("Guesse the number:\n"))
    if guess_number<45:
        print("you enter less number please enter the grater number.\n")
    elif guess_number>45:
        print("you enter grater number please enter lesser number.\n ")
    else:
        print("You Won\n")
        print(number_of_guesses,"no of guess he took to finish" )
        break
print(9-number_of_guesses,"no of guesses left")
number_of_guesses = number_of_guesses+1
if(number_of_guesses>9):
    print("GAME OVER")