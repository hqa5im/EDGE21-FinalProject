#WHAT COLOR ARE YOU QUIZ
print("WHAT COLOR ARE YOU?")

print(" ")

print("Instructions:")
print("You will be asked a series of multiple choice questions. To select your answer input the given number of the bullet point.")

print(" ")

name = input("Name: ")
score = 0
#questions = 8

print("What's your favourite dessert?")
options = ['Ice cream', 'Chocolate chip cookies', 'Cupcakes', 'Pudding']
for i, item in enumerate(options, 1):
    print(i, '. ' + item, sep='', end=' ')
answer = input("Ans: ")
if answer == "4" or "2":
    score += 1
else:
    score += 0

print("What's your favourite animal?")
options = ['Elephants', 'Lions', 'Giraffes', 'Sharks']
for i, item in enumerate(options, 1):
    print(i, '. ' + item, sep='', end=' ')
answer = input("Ans: ")
if answer == "1" or "3":
    score += 1
else:
    score += 0

print("Which do you consider the best super power?")
options = ['Flying', 'Invisibility', 'Time travel', 'Super strength']
for i, item in enumerate(options, 1):
    print(i, '. ' + item, sep='', end=' ')
answer = input("Ans: ")
if answer == "1" or "3":
    score += 1
else:
    score += 0

print("What's your favourite vacation destination?")
options = ['Mountains', 'Beach', 'Lake', 'Jungle']
for i, item in enumerate(options, 1):
    print(i, '. ' + item, sep='', end=' ')
answer = input("Ans: ")
if answer == "1" or "4":
    score += 1
else:
    score += 0

print("Do you consider yourself more logical or creative?")
options = ['Logical', 'Creative']
for i, item in enumerate(options, 1):
    print(i, '. ' + item, sep='', end=' ')
answer = input("Ans: ")
if answer == "2":
    score += 1
else:
    score += 0

print("Do you remain calm under pressure?")
options = ['Yes', 'No']
for i, item in enumerate(options, 1):
    print(i, '. ' + item, sep='', end=' ')
answer = input("Ans: ")
if answer == "1":
    score += 1
else:
    score += 0

print("How would your friends describe you?")
options = ['Kind', 'Smart', 'Loyal', 'Crackhead']
for i, item in enumerate(options, 1):
    print(i, '. ' + item, sep='', end=' ')
answer = input("Ans: ")
if answer == "3" or "4":
    score += 1
else:
    score += 0

print("What's your favourite number?")
options = ['one', 'three', 'seven', 'elven']
for i, item in enumerate(options, 1):
    print(i, '. ' + item, sep='', end=' ')
answer = input("Ans: ")
if answer == "1" or "4":
    score += 1
else:
    score += 0

if score == 8:
    print("You're white! Kinda basic but a classic ")
elif score == 7:
    print("You're blue! A calm individual who always seems like they have it under control even if they may not ")
elif score == 6:
    print("You're red! A fiery beast who's always ready to fight for their rights ")
elif score == 5:
    print("You're yellow! You got those good vibes ")
elif score == 4:
    print("You're green! Quite chill of a person; probably would be down with either staying at home or going out for an adventure ")
elif score == 3:
    print("You're orange! Both a color and fruit making you quite unique ")
elif score == 2:
    print("You're purple! Regal, elegant and sophisticated. A true Queen/King ")
elif score == 1:
    print("You're black! A mystery; probably lives life by the phrase 'keep your friends close but your enemies closer' ")
elif score == 0:
    print("Damnn you're the rainbow. The best of all worlds")


#to check if score counter is working
# print("Your score is: ")
# print(score)
