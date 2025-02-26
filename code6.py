# 6) Remove first two names and last name
# """friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
# # Needed Output
# # ["Ahmed", "Sayed", "Salem"]
# # ["Ahmed", "Sayed"]"""

friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

friends = friends[2:-1]
print(friends)
# another solution
# friends.pop(0)
# friends.pop(0)
# friends.pop(-1)
# print(friends)