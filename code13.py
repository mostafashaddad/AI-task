# 13) Pad strings with '@' to ensure 20 characters
# """name_one = "computer"
# name_two = "computer_science"
# # Needed Output
# #@@@@@@@@@@@@computer
# # @@@@computer_science"""

name_one = "computer"
name_two = "computer_science"
print(name_one.rjust(20, "@"))
print(name_two.rjust(20, "@"))

# الصيغة العامة
# string.rjust(width, fillchar)