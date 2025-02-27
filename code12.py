# 12)Format numbers with leading zeros
# """num = "9"
# num = "15"
# num = "130"
# num = "950"
# num = "1500"

# # Needed Output
# # 0009
# # 0015
# # 0130
# # 0950
# # 1500"""

num = "9"
print(num.zfill(4))
num = "15"
print(num.zfill(4))
num = "130"
print(num.zfill(4))
num = "950"
print(num.zfill(4))
num = "1500"
print(num.zfill(4))

# another solution

# numbers = [9, 15, 130, 950, 1500]

# for num in numbers:
#     print(f"{num:04d}")  

