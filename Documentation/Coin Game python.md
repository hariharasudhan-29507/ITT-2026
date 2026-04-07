# Coin Game

## Description

Simulates a three-round coin game between Suresh and Sundar where the loser of each round receives coins from a third player Raja. After each round, the player with more coins is tracked and the next round's loser gains coins from the current round's winner.

## Approach

Compare Suresh's and Sundar's coin counts to determine the winner of each round. The loser of the current round gains the winner's coins added to their own. After each round, print who has fewer coins (indicated by "S" for Suresh or "N" for Nirmal/Sundar), then repeat for the next two rounds using the updated coin counts.

## Algorithm

```
ALGORITHM COIN_GAME
// Simulates three rounds of coin redistribution between two players
// Input  : Coin counts for Suresh, Sundar, and Raja
// Output : "S" or "N" after each of the three rounds indicating who has fewer coins

Read suresh, sundar coin counts from user
Determine round 1 winner by comparing suresh and sundar
Read raja's coin count from user
If Suresh wins round 1
    Print "N" (Sundar loses)
    Add raja's coins to Sundar's total
Else
    Print "S" (Suresh loses)
    Add raja's coins to Suresh's total
Determine round 2 winner by comparing updated coin counts
If Suresh wins round 2
    Print "N"
    Add Suresh's coins to Sundar's total
    Determine round 3 winner and print "N" or "S"
Else
    Print "S"
    Add Sundar's coins to Suresh's total
    Determine round 3 winner and print "N" or "S"
```

## Time Complexity

O(1) — a fixed number of comparisons and additions are performed for exactly three rounds.

## Code

[coinGame.py](../Codes/coinGame.py)

## Author

hariharasudhan
