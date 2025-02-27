# Python Code Snippets

This repository contains 15 Python code snippets for performing various operations on lists, strings, and numbers.

## Table of Contents
1. [Print Odd and Even Indexed Names](#print-odd-and-even-indexed-names)
2. [Find Position of 'z' in "Elzero"](#find-position-of-z-in-elzero)
3. [Print Specific Names from a List](#print-specific-names-from-a-list)
4. [Update Last Two Names](#update-last-two-names)
5. [Add Names to the Beginning and End](#add-names-to-the-beginning-and-end)
6. [Remove First Two Names and Last Name](#remove-first-two-names-and-last-name)
7. [Merge Multiple Lists](#merge-multiple-lists)
8. [Sort List Ascending and Descending](#sort-list-ascending-and-descending)
9. [Count Elements in the List](#count-elements-in-the-list)
10. [Nested List with Frameworks](#nested-list-with-frameworks)
11. [Remove Extra Symbols from a String](#remove-extra-symbols-from-a-string)
12. [Format Numbers with Leading Zeros](#format-numbers-with-leading-zeros)
13. [Pad Strings with '@' to Ensure 20 Characters](#pad-strings-with-to-ensure-20-characters)
14. [Swap Case of Letters](#swap-case-of-letters)
15. [Count Occurrences of "Love" in a String](#count-occurrences-of-love-in-a-string)

---

## 1. Print Odd and Even Indexed Names
```python
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[::2])  # "Osama", "Sayed", "Mahmoud"
print(friends[1::2]) # "Ahmed", "Ali"
```

## 2. Find Position of 'z' in "Elzero"
```python
name = "Elzero"
print(name.index("z"))  # Output: 2
```

## 3. Print Specific Names from a List
```python
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[1:4])  # "Ahmed", "Sayed", "Ali"
print(friends[-2:])  # "Ali", "Mahmoud"
```

## 4. Update Last Two Names
```python
friends[-2:] = ["science", "science"]
print(friends)
```

## 5. Add Names to the Beginning and End
```python
friends.insert(0, "Nasser")
print(friends)
friends.append("Salem")
print(friends)
```

## 6. Remove First Two Names and Last Name
```python
friends = friends[2:-1]
print(friends)
friends.pop()
print(friends)
```

## 7. Merge Multiple Lists
```python
merged_list = friends + employees + school
print(merged_list)
```

## 8. Sort List Ascending and Descending
```python
print(sorted(friends))
print(sorted(friends, reverse=True))
```

## 9. Count Elements in the List
```python
print(len(friends))
```

## 10. Nested List with Frameworks
```python
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[4][0])  # Django
print(technologies[4][-1]) # Web
```

## 11. Remove Extra Symbols from a String
```python
name = "#@#@science#@#@"
print(name.strip("#@"))  # science
```

## 12. Format Numbers with Leading Zeros
```python
for num in ["9", "15", "130", "950", "1500"]:
    print(num.zfill(4))
```

## 13. Pad Strings with '@' to Ensure 20 Characters
```python
print(name_one.rjust(20, "@"))
print(name_two.rjust(20, "@"))
```

## 14. Swap Case of Letters
```python
print(name_one.swapcase())
print(name_two.swapcase())
```

## 15. Count Occurrences of "Love" in a String
```python
msg = "I Love Python And Although Love Elzero Web School"
print(msg.count("Love"))  # Output: 2
```

---

## How to Use
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/repository-name.git
   ```
2. Navigate to the directory:
   ```sh
   cd repository-name
   ```
3. Run any Python script to test the code snippets.

## Contributing
Feel free to fork this repository and submit pull requests to improve the code.

## License
This project is licensed under the MIT License.

