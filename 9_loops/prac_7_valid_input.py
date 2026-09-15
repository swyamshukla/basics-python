def game():
    num=int(input("guess a number between 1 and 10:"))
    while 1:
        if(num>=1 and num<=10):
            print("You win")
            break
        print("try again")
        num=int(input("guess a number between 1 and 10: "))


game()
