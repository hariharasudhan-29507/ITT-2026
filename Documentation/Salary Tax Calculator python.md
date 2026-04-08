# Salary Tax Calculator

## Description

Calculates the income tax owed based on a salary slab system, printing either the tax amount or a no-tax message.

## Approach

Read the salary from the user. Compare it against predefined salary slabs and apply the appropriate tax rate. Salaries up to 250000 are tax-free. Salaries between 250000 and 500000 are taxed at 0.5%. Salaries between 500000 and 1000000 are taxed at 10%. Salaries above 1000000 are taxed at 15%.

## Algorithm

```
ALGORITHM SALARY_TAX_CALCULATOR
// Calculates income tax based on salary slab
// Input  : An integer salary
// Output : Tax amount or a no-tax message

Read salary from user
If salary is less than or equal to 250000
    Print "no tax"
Else if salary is between 250000 and 500000 (exclusive)
    Print salary multiplied by 0.005 as tax amount
Else if salary is between 500000 and 1000000 (exclusive)
    Print salary multiplied by 0.1 as tax amount
Else
    Print salary multiplied by 0.15 as tax amount
```

## Time Complexity

O(1) — a fixed number of comparisons are performed regardless of the salary value.

## Code

[salaryTax.py](../Codes/salaryTax.py)

## Author

hariharasudhan
