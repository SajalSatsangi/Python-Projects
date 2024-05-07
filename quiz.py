print('Welcome to my computer quiz!')

playing = input('Do you want to play? ')

if playing.lower() != 'yes':
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("1. What is the purpose of Python's print() function? ").lower()
if answer == "displaying output on the console":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("2. Which keyword is used for creating a function in Python? ").lower()
if answer == "def":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("3. What does the len() function return in Python? ").lower()
if answer == "length of a sequence":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("4. How do you comment a single line in Python? ").lower()
if answer == "using the # symbol":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("5. Which data structure in Python is ordered and mutable? ").lower()
if answer == "list":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("6. What does the import statement do in Python? ").lower()
if answer == "imports modules or packages into the current script or module":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("7. Which operator is used for exponentiation in Python? ").lower()
if answer == "**":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("8. What is the output of bool('False') in Python? ").lower()
if answer == "true":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("9. What does the range() function return? ").lower()
if answer == "a sequence of numbers.":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("10. Which method is used to remove an item from a list in Python? ").lower()
if answer == "remove()":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"You scored {score} out of 10.")
print("you got"  + str( (score/10) * 100) + "%.")
