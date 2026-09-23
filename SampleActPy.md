# Python Activities for Learning

## Activity 1: Basic I/O, Operators, Conditions, Loops

### Exercise 1.1 - EASY: Temperature Converter
**Difficulty:** Easy  
**Topics:** I/O, Operators, Conditions

**Problem:**
Create a program that:
- Asks the user to input a temperature in Celsius
- Converts it to Fahrenheit using the formula: F = (C × 9/5) + 32
- Displays the result
- Tells the user if the temperature is "Cold" (< 0°C), "Cool" (0-15°C), "Warm" (15-25°C), or "Hot" (> 25°C)

**Example Output:**
```
Enter temperature in Celsius: 25
Temperature in Fahrenheit: 77.0
Status: Warm
```

**Hints:**
- Use `input()` to get user input
- Convert string to float using `float()`
- Use if-elif-else for conditions

---

### Exercise 1.2 - MEDIUM: Number Pattern Pyramid
**Difficulty:** Medium  
**Topics:** Loops, Operators, I/O

**Problem:**
Create a program that:
- Asks the user for a number (n)
- Creates a pyramid pattern where:
  - Row 1 has 1 number
  - Row 2 has 2 numbers
  - Row n has n numbers
  - Each row shows the row number repeated

**Example Output (n = 5):**
```
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
```

**Hints:**
- Use nested loops (outer loop for rows, inner loop for columns)
- Use string multiplication or join()

---

### Exercise 1.3 - HARD: Number Guessing Game with Statistics
**Difficulty:** Hard  
**Topics:** Loops, Conditions, Operators, User Input

**Problem:**
Create a number guessing game where:
- Program generates a random number between 1 and 100
- User tries to guess the number with up to 10 attempts
- Program gives feedback: "Too high", "Too low", or "Correct!"
- After the game ends, display:
  - Whether they won or lost
  - Number of attempts used
  - The secret number
- Ask if they want to play again

**Example Output:**
```
I'm thinking of a number between 1 and 100
Guess the number (Attempts left: 10): 50
Too high! Try again.
Guess the number (Attempts left: 9): 25
Too low! Try again.
...
Correct! You found it in 7 attempts!
Play again? (yes/no): no
Thanks for playing!
```

**Hints:**
- Use `import random` and `random.randint()`
- Track attempts with a counter
- Use while loops for game logic
- Add a while loop for "play again" functionality

---

## Activity 2: Functions and Collections

### Exercise 2.1 - EASY: List Statistics Calculator
**Difficulty:** Easy  
**Topics:** Functions, Lists, Collections

**Problem:**
Create a program with a function that:
- Takes a list of numbers as input
- Returns a dictionary with:
  - `sum`: sum of all numbers
  - `average`: average of the numbers
  - `max`: maximum value
  - `min`: minimum value
  - `count`: count of numbers

**Example:**
```python
numbers = [10, 20, 30, 40, 50]
result = calculate_stats(numbers)
print(result)
# Output: {'sum': 150, 'average': 30.0, 'max': 50, 'min': 10, 'count': 5}
```

**Hints:**
- Define a function with one parameter (the list)
- Use built-in functions: `sum()`, `len()`, `max()`, `min()`
- Return a dictionary
- Use len() to calculate average

---

### Exercise 2.2 - MEDIUM: Student Grade Manager
**Difficulty:** Medium  
**Topics:** Functions, Lists, Dictionaries, Conditions

**Problem:**
Create a program with functions that:
- Store student data as a dictionary of dictionaries: `{name: {'math': score, 'english': score, 'science': score}}`
- Function to add a student with their grades
- Function to calculate average grade for a student
- Function to find the student with the highest average
- Function to display all students and their averages

**Example:**
```
--- Student Grade Manager ---
1. Add Student
2. View All Students
3. Find Top Student
4. Exit

Enter choice: 1
Student name: Alice
Math grade: 85
English grade: 90
Science grade: 88
Alice added successfully!

Enter choice: 2
Alice - Average: 87.67
Bob - Average: 82.33

Enter choice: 3
Top student: Alice (Average: 87.67)
```

**Hints:**
- Create a global dictionary to store students
- Write separate functions for each operation
- Use loops to iterate through dictionaries
- Format output nicely with f-strings

---

### Exercise 2.3 - HARD: Word Frequency Analyzer with File Processing
**Difficulty:** Hard  
**Topics:** Functions, Collections (Lists/Dictionaries), File I/O, Sorting

**Problem:**
Create a program that:
- Reads text from a file (or gets text from user input)
- Creates functions to:
  - Extract and clean words (lowercase, remove punctuation)
  - Count word frequencies and return as a dictionary
  - Find the top N most common words
  - Find words by frequency range (e.g., appears 5-10 times)
- Displays results in a formatted table

**Example:**
```
--- Word Frequency Analyzer ---
Enter text (or press Enter to read from file): 
[User enters or file is read]

Total unique words: 150
Total words: 1200

Top 10 Most Frequent Words:
Rank  Word        Frequency
1.    the         85
2.    and         62
3.    to          51
4.    a           48
...

Words appearing 5-10 times: ['python', 'data', 'program', ...]
```

**Hints:**
- Use `string.punctuation` for removing punctuation
- Use `.split()` for word tokenization
- Use `sorted()` with `key` parameter for sorting by frequency
- Create dictionaries to store word counts
- Use list comprehensions or loops to filter by frequency range
- Consider using `collections.Counter` for cleaner code

---

## Solution Template Starters

### Activity 1.1 Template:
```python
# Temperature Converter
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit}")

# Your condition logic here
```

### Activity 2.1 Template:
```python
def calculate_stats(numbers):
    stats = {
        'sum': sum(numbers),
        'average': sum(numbers) / len(numbers),
        'max': max(numbers),
        'min': min(numbers),
        'count': len(numbers)
    }
    return stats

# Test your function
numbers = [10, 20, 30, 40, 50]
result = calculate_stats(numbers)
print(result)
```

---

## Challenge Extensions

Once you complete an exercise, try these extensions:

**Activity 1:**
- Add input validation (handle non-numeric input)
- Add menu options for multiple conversions
- Create a logging system to save all calculations

**Activity 2:**
- Add ability to edit/delete students
- Calculate letter grades (A, B, C, etc.)
- Export student data to a CSV file
- Add search/filter functionality

