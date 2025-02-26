friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

odd_names = []
even_names = []

for i, name in enumerate(friends):
    if i % 2 == 0:
        odd_names.append(f"{name}")
    else:
        even_names.append(f"{name}")

print(odd_names)
print(even_names)
