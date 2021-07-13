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
if answer == "4":
    score += 1
else:
    score += 0

print("What's your favourite animal?")
options = ['Birds', 'Lions', 'Giraffes', 'Sharks']
for i, item in enumerate(options, 1):
    print(i, '. ' + item, sep='', end=' ')
answer = input("Ans: ")
if answer == "1":
    score += 1
else:
    score += 0

print("Which do you consider the best super power?")
options = ['Flying', 'Invisibility', 'Time travel', 'Super strength']
for i, item in enumerate(options, 1):
    print(i, '. ' + item, sep='', end=' ')
answer = input("Ans: ")
if answer == "1":
    score += 1
else:
    score += 0

print("What's your favourite vacation destination?")
options = ['Mountains', 'Beach', 'Lake', 'Desert']
for i, item in enumerate(options, 1):
    print(i, '. ' + item, sep='', end=' ')
answer = input("Ans: ")
if answer == "1":
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
if answer == "3":
    score += 1
else:
    score += 0

#to check is score counter is working
print("Your score is: ")
print(score)
