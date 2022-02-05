# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#First we count each letter in the name strings
  #counting True
name1_true = name1.lower().count('t') + name1.lower().count('r') + name1.lower().count('u') + name1.lower().count('e')
name2_true = name2.lower().count('t') + name2.lower().count('r') + name2.lower().count('u') + name2.lower().count('e')
name_true = name1_true + name2_true
  #counting Love
name1_love = name1.lower().count('l') + name1.lower().count('o') + name1.lower().count('v') + name1.lower().count('e')
name2_love = name2.lower().count('l') + name2.lower().count('o') + name2.lower().count('v') + name2.lower().count('e')
name_love = name1_love + name2_love

#Calculating the love score(sum of true is first digit and sum of love is second digit)
love_score = str(name_true) + str(name_love)
print(love_score)
#Printing final result
if int(love_score) < 10 or int(love_score) > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= int(love_score) < 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")


