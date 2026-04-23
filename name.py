import random 

computer = random.choice([0,1,2])
your_score = int(input("type your number: "))
dictionary = {
    "rock": 0,
    "paper": 1, 
    "scissors": 2
}
reverseDict = {
    0 : "rock",
    1 : "paper",
    2 : "scissors"
}
if your_score not in [0,1,2]:
    print("please enter the correct value ")
else:
    comp = reverseDict[computer]
    my_number = reverseDict[your_score]
    print(f"your selected number is :{my_number}\n the computer guess is : {comp}")
if your_score not in [0,1,2]:
    print("please anter the correct value ")
else:
    if computer == your_score:
        print('game ends before even starting')
    else:
        if computer == 0 and your_score == 1:
            print('alas! computer wins')
        elif computer == 1 and your_score == 0:
            print('wow! you win')
        elif computer == 0 and your_score == 2:
            print('agh! computer won')
        elif computer == 1 and your_score == 2:
            print('great champ!')
        elif computer == 2 and your_score == 1:
            print('computer won!')
        elif computer == 2 and your_score == 0:
            print('you won!')
    