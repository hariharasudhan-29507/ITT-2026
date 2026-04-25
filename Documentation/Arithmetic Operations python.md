# Arithmetic Operations

## Description

Performs basic arithmetic operations (addition, subtraction, multiplication, division, and modulus) on two numbers based on a menu choice provided by the user.

## Approach

Accept two numbers and a menu choice from the user. Use a match statement to select the appropriate arithmetic operation and print the result. If the choice does not correspond to any operation, prompt the user to enter a valid option.

## Algorithm

```
ALGORITHM ARITHMETIC_OPERATIONS
// Performs one of five arithmetic operations based on user menu selection
// Input  : Two integers num1 and num2, and an integer choice (1-5)
// Output : Printed result of the selected arithmetic operation

Read num1 from user
Read num2 from user
Display menu options: 1-addition, 2-subtraction, 3-multiplication, 4-division, 5-modulus
Read choice from user
If choice is 1
    Print sum of num1 and num2
Else if choice is 2
    Print difference of num1 and num2
Else if choice is 3
    Print product of num1 and num2
Else if choice is 4
    Print quotient of num1 divided by num2
Else if choice is 5
    Print remainder of num1 divided by num2
Else
    Print invalid operation message
```

## Time Complexity

O(1) — a single arithmetic operation is performed regardless of input size.

## Code

[Arith.py](../Codes/Arith.py)

## Author

Hariharasudhan A
sophomore in CSE , MEPCO schlenk engineering college 
Sivakasi
