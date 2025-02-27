<h1 align="center">
  <br>
  <a href="https://github.com/mostafashaddad/AI-task"><img src="https://raw.githubusercontent.com/github/explore/main/topics/python/python.png" alt="Python Code Snippets" width="200"></a>
  <br>
  Python Code Snippets
  <br>
</h1>

<h4 align="center">A collection of 15 Python code snippets for list, string, and number operations.</h4>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#download">Download</a> •
  <a href="#license">License</a>
</p>

## Key Features

* Various list operations like sorting, merging, and updating elements.
* String manipulations including case swapping and symbol removal.
* Number formatting techniques such as leading zeros.
* Working with nested lists and counting occurrences in strings.

## How To Use

To clone and run these Python snippets, you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/downloads/) installed on your computer. From your command line:

```bash
# Clone this repository
git clone https://github.com/mostafashaddad/AI-task.git

# Go into the repository
cd AI-task

# Run any Python script
touch script.py  # Create a script file
python3 script.py  # Run the script
```

## Snippets

### 1. Print Odd and Even Indexed Names
```python
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[::2])  # "Osama", "Sayed", "Mahmoud"
print(friends[1::2]) # "Ahmed", "Ali"
```

### 2. Find Position of 'z' in "Elzero"
```python
name = "Elzero"
print(name.index("z"))  # Output: 2
```

### 3. Print Specific Names from a List
```python
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[1:4])  # "Ahmed", "Sayed", "Ali"
print(friends[-2:])  # "Ali", "Mahmoud"
```

### 4. Update Last Two Names
```python
friends[-2:] = ["science", "science"]
print(friends)
```

### 5. Add Names to the Beginning and End
```python
friends.insert(0, "Nasser")
print(friends)
friends.append("Salem")
print(friends)
```

### 6. Remove First Two Names and Last Name
```python
friends = friends[2:-1]
print(friends)
friends.pop()
print(friends)
```

### 7. Merge Multiple Lists
```python
merged_list = friends + employees + school
print(merged_list)
```

### 8. Sort List Ascending and Descending
```python
print(sorted(friends))
print(sorted(friends, reverse=True))
```

### 9. Count Elements in the List
```python
print(len(friends))
```

### 10. Nested List with Frameworks
```python
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[4][0])  # Django
print(technologies[4][-1]) # Web
```

### 11. Remove Extra Symbols from a String
```python
name = "#@#@science#@#@"
print(name.strip("#@"))  # science
```

### 12. Format Numbers with Leading Zeros
```python
for num in ["9", "15", "130", "950", "1500"]:
    print(num.zfill(4))
```

### 13. Pad Strings with '@' to Ensure 20 Characters
```python
print(name_one.rjust(20, "@"))
print(name_two.rjust(20, "@"))
```

### 14. Swap Case of Letters
```python
print(name_one.swapcase())
print(name_two.swapcase())
```

### 15. Count Occurrences of "Love" in a String
```python
msg = "I Love Python And Although Love Elzero Web School"
print(msg.count("Love"))  # Output: 2
```

## License

This project is licensed under the MIT License.

