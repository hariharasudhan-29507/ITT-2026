# Car Bike Tyres

## Description

Determines whether the tyres remaining after cars have taken their share can form exactly one bike, which requires exactly 2 spare tyres.

## Approach

Read the total number of tyres. Each car uses 4 tyres. Check if the total count is even (a requirement for distributing tyres). If the count is divisible by 4, no tyres remain for a bike. If it is even but not divisible by 4, exactly 2 tyres remain, which is enough for a bike. Print whether a bike can be formed.

## Algorithm

```
ALGORITHM CAR_BIKE_TYRES
// Checks if remaining tyres after cars form a valid bike
// Input  : An integer tyre_count (between 2 and 100)
// Output : "YES" if exactly 2 tyres remain for a bike, "NO" otherwise

Set possible_bike = 0
Read tyre_count from user
If tyre_count is between 2 and 100 (inclusive)
    If tyre_count is divisible by 2
        If tyre_count is divisible by 4
            Set possible_bike = 0
        Else
            Set possible_bike = 1
If possible_bike equals 1
    Print "YES"
Else
    Print "NO"
```

## Time Complexity

O(1) — a fixed number of arithmetic checks are performed.

## Code

[carBike.py](../Codes/carBike.py)

## Author

Hariharasudhan A
sophomore in CSE , MEPCO schlenk engineering college
Sivakasi
