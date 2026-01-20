name = str(input("     -----::----- Welcome to data type identification game -----::-----      \n\nPlease Enter your name: ")).title()
value = 121
print(f"\nWhat is the data type of {value} ?")
guess = input("\nEnter your answer: ")
print(f"You guessed {guess} .\nThe correct answer is Integer.")

value = 29.30
print(f"\nWhat is the data type of {value} ?")
guess = input("\nEnter your answer: ")
print(f"You guessed {guess} .\nThe correct answer is float.")

value = True
print(f"\nWhat is the data type of {value} ?")
guess = input("\nEnter your answer: ")
print(f"You guessed {guess} .\nThe correct answer is Boolean.")

value = "Hello World"
print(f"\nWhat is the data type of {value} ?")
guess = input("\nEnter your answer: ")
print(f"You guessed {guess} .\nThe correct answer is String.")

value = '"True"'
print(f"\nWhat is the data type of {value} ?")
guess = input("\nEnter your answer: ")
print(f"You guessed {guess} .\nThe correct answer is String.")

print(f"\n\n<--------------------- Thank you for playing the game, {name} --------------------->\n")