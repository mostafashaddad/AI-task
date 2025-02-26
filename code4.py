# 4)Update last two names
# #Update the last two names in the list to the name “science”
# """friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
# # Needed Output
# # ["Osama", "Ahmed", "Sayed", "science", "science"]"""

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
friends[-2:] = ["science", "science"]
print(friends)