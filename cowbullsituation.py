import random
num = str(random.randint(1000,9999))


while True:
    guess = str(input("A 4 digits number, what is your guess? \n"))
    cow = bull = 0
    for i in range(4):
        if guess[i] == num[i]:
            cow += 1
        else:
            if guess[i] in num:
                bull += 1
    print(str(cow)+' cows, '+str(bull)+' bulls')

    if guess == num:
        print("correct, the number is ",guess)
        break