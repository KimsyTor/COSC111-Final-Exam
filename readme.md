[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/jZg3kZEa)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14849394&assignment_repo_type=AssignmentRepo)
# Final Coding Exam - CSCI/COSC 111

> **NOTE:** You can search internet for solutions, however, you will still need to
> explain your code to your professor at any time after your submission.
> If you fail to explain, this will result in a score deduction or failing the exam.

### Exercise 1 - 1pt

You prefer a good old 12-hour time format. But the modern world we live in would rather use the 24-hour format and you see it everywhere. 

Your task is to convert the time from the 24-h format into 12-h format by following the next rules:
- The output format should be `hh:mm a.m.` (for hours before midday) or `hh:mm p.m.` (for hours after midday)
- If hours is less than 10 - don't write a `0` before it. For example: `9:05 a.m.`  

Here you can find some useful information about the [12-hour format](https://en.wikipedia.org/wiki/12-hour_clock) .

**Input:** Time in a 24-hour format (as a string).

**Output:** Time in a 12-hour format (as a string).

**Example:**

```python
time_converter('12:30') == '12:30 p.m.'
time_converter('09:00') == '9:00 a.m.'
time_converter('23:15') == '11:15 p.m.'
time_converter('00:00') == '12:00 a.m.'
```

---

### Exercise 2 - 5pts

Say you have a list of lists where each value in the inner lists is a one-character string, like this:

```python
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
```

Think of grid[x][y] as being the character at the x- and y-coordinates of a “picture” drawn with text characters. 

The (0, 0) origin is in the upper-left corner, the x-coordinates increase going right, and the y-coordinates increase going down.

Copy the previous grid value, and write code that uses it to print the image.
![Alt text](<resource/Pasted image 20220420235809.png>)

**Hint:** You will need to use a loop in a loop in order to print `grid[0][0]`, then `grid[1][0]`, then `grid[2][0]`, and so on, up to `grid[8][0]`.

---

### Exercise 3 - 1pt

You have a number and you need to determine which digit in this number is the biggest.

**Input:** A positive int.

**Output:** An int (0-9).

**Example:**

```python
max_digit(0) == 0
max_digit(52) == 5
max_digit(634) == 6
max_digit(1) == 1
max_digit(10000) == 1
```

---

### Exercise 4 - 1pt

Write a Python function called `count_vowels` that takes a string as input and returns the count of vowels (both uppercase and lowercase) in the string.

**Example:**

```python
input_string = "Hello, World!"
result = count_vowels(input_string)
print(result)

# 3

```

**Explanation:**
The function should count the number of vowels (both uppercase and lowercase) in the input_string and return the count as the output. In this example, there are three vowels in the string: 'e', 'o', and 'o'.

**Reminders:**
- Vowels are considered to be 'a', 'e', 'i', 'o', and 'u' (both uppercase and lowercase).
- Other characters such as spaces, punctuation, and numbers should be ignored.

---

### Exercise 5 - 2pts

Write a Python function called `find_matrix_avg` that takes a two-dimensional list of integers as input and returns the average of all the elements in the matrix.

**Example:**

```python
matrix = [
    [3, 5, 2],
    [7, 1, 4],
    [6, 8, 9]
]
result = find_matrix_avg(matrix)
print(result)

# 5.0
```

**Explanation:**
The function should calculate the average of all the elements in the `matrix` and return the average as the output. In this example, the average of all the elements in the matrix is 5.0.

**Reminders:**
- The matrix is a two-dimensional list of integers.
- The average should be calculated as the sum of all elements divided by the total number of elements.

---

### Exercise 6 - 3pts

Write a Python function called `list_to_dict` that take a list of tuples as input `lst` and returns a list of dictionaries. 

`lst` index 0 is considered as the key of all other elements in the list.

**Example:**

```python
list_to_dict([
        ("name", "age", "phone"),
        ("John", 25, "1234567890"),
        ("Jane", 24, "9876543210"),
        ("Doe", 26, "1234567890"),
])
```

#### Output
```bash
[
        {"name": "John", "age": 25, "phone": "1234567890"},
        {"name": "Jane", "age": 24, "phone": "9876543210"},
        {"name": "Doe", "age": 26, "phone": "1234567890"}
]
```


---

### Exercise 7 - 2pts

Write a Python function called `word_frequency_counter` that takes a list of words as input and returns a
dictionary containing the frequency count of each word in the list.

**Example:**

```python
word_list = ["apple", "banana", "orange", "apple", "grape", "banana", "apple", "orange"]

result = word_frequency_counter(word_list)

# {'apple': 3, 'banana': 2, 'orange': 2, 'grape': 1}

```

**Explanation:**
The function should count the occurrences of each word in the `word_list` and return a dictionary where the keys are the unique words, and the values are their corresponding frequencies.

**Reminders:**
- The word frequency count should be case-sensitive. For example, "Apple" and "apple" should be treated as different words.
- The word list may contain punctuation and whitespace, but these should not be considered part of the word.
