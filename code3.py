# 3) Print the set of names 2, 3, and 4 on the first line, then the last name and the one before it on the second line, knowing that the code should work if we change the number of elements in the list."""
# """friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
# # Needed Output
# # "Ahmed", "Sayed", "Ali",
# # "Ali", "Mahmoud""""

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[1], friends[2], friends[3])
print(friends[-2], friends[-1])

# another solution

# print(" ".join(friends[1:4]))

# print(" ".join(friends[-2:]))