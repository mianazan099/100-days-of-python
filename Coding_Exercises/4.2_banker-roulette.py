import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# You are not allowed to use the choice() function.
person = names[random.randint(0, len(names) - 1)]
print(f'{person} is going to buy the meal today!')
