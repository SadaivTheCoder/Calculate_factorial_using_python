## 🧮 Factorial Calculator using Python Recursion

This repository contains a simple Python program that calculates the factorial of a given number using recursion. It's a great example for beginners to understand how recursive functions work in Python.

### 📌 What is Factorial?

The factorial of a non-negative integer `n` is the product of all positive integers less than or equal to `n`. It is denoted by `n!` and defined as:

- `0! = 1` (by definition)
- `n! = n × (n-1)!` for `n > 0`

### 🧠 How Recursion Works Here

The program uses a recursive function `facto(n)` which calls itself with `n-1` until it reaches the base case `n == 0`.

### 💻 Code Overview

```python
def facto(n):
    if(n == 0):
        return 1
    else:
        return n * facto(n - 1)

n = int(input("Enter a number:-> "))
print(facto(n))
```

### 🚀 How to Run

1. Clone the repository or copy the code into a `.py` file.
2. Run the script using any Python interpreter.
3. Enter a non-negative integer when prompted.
4. Get the factorial result printed on the screen.

### 📚 Learning Outcome

- Understand recursion in Python.
- Learn how base cases prevent infinite loops.
- Practice user input and function calls.
