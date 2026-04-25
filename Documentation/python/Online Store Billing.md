# Online Store Billing

## Description

Calculates the final bill amount for an online store purchase by applying a discount based on the purchase amount tier.

## Approach

Read the purchase amount from the user. Apply a 2% discount for amounts of 5000 or more, or a 1% discount for amounts between 3000 and 5000. For amounts below 3000, display an invalid amount message. Subtract the discount from the purchase amount to get the final bill.

## Algorithm

```
ALGORITHM ONLINE_STORE_BILLING
// Calculates discounted bill based on purchase amount tier
// Input  : An integer amount representing the purchase amount
// Output : The final bill amount after applying the applicable discount

Read amount from user
If amount is greater than or equal to 5000
    Set discount = amount multiplied by 0.02
    Set amount = amount minus discount
Else if amount is between 3000 and 5000 (inclusive)
    Set discount = amount multiplied by 0.01
    Set amount = amount minus discount
Else
    Print invalid amount message
Print final bill amount
```

## Time Complexity

O(1) — a fixed number of operations are performed regardless of the input value.

## Code

[OnlineStore.py](../Codes/OnlineStore.py)

## Author

Hariharasudhan A  
sophomore in CSE , MEPCO schlenk engineering college  
Sivakasi  
reach me : sudanayyappann_bcs28@mepcoeng.ac.in
