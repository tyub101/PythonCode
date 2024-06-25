import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_choice= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
choices=[rock,paper,scissors]
if user_choice >=3 : 
  print("You typed an inavalid number . You lose")
else:
    print(choices[user_choice])
    print("computer chose :")
    random_integer = random.randint(0,2)
    print(choices[random_integer])
    if int(user_choice) == random_integer : 
        print("Draw")
    elif user_choice == 0 and random_integer == 2 or user_choice == 1 and random_integer == 0 or user_choice == 2 and random_integer ==1:
        print("You win")
    else: 
        print("You lose")



