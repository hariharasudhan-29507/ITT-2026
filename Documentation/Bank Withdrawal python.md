# Bank Withdrawal

## Description

Simulates a bank withdrawal system that validates the account balance and withdrawal amount before allowing the transaction, enforcing a minimum balance and requiring amounts to be multiples of 100.

## Approach

Read the current balance from the user. If the balance is at least 500, prompt for a withdrawal amount. Validate that the amount is positive, less than the balance, and a multiple of 100. If all conditions are met, subtract the amount from the balance and print the new balance. Otherwise, print the appropriate error message.

## Algorithm

```
ALGORITHM BANK_WITHDRAWAL
// Validates and processes a bank withdrawal
// Input  : An integer balance and an integer amount to withdraw
// Output : Updated balance or an error message

Read balance from user
If balance is less than 500
    Print minimum balance error and stop
Read amount from user
If balance is greater than amount AND balance is greater than 0 AND amount is greater than 0
    If amount is divisible by 100
        Set balance = balance minus amount
        Print "withdrawn" and new balance
    Else
        Print "not a multiple of 100" error
Else
    Print invalid balance error
```

## Time Complexity

O(1) — a fixed set of comparisons and one subtraction are performed.

## Code

[withdraw.py](../Codes/withdraw.py)

## Author

Hariharasudhan A

sophomore in CSE , MEPCO schlenk engineering college

Sivakasi

