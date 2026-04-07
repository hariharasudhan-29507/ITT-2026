# Chess Match

## Description

Calculates the prize distribution for a chess match between Chandru and Nirmal based on the results of 14 individual matches, awarding different prize amounts based on who wins overall.

## Approach

Read the prize per match and collect results for all 14 matches as single-character strings ('C' for Chandru, 'N' for Nirmal, 'D' for draw). Count each player's wins, splitting draw points equally. Compare total scores to determine the overall winner, then calculate and print Chandru's share of the total prize pool based on the outcome.

## Algorithm

```
ALGORITHM CHESS_MATCH
// Calculates prize payout based on 14 chess match results
// Input  : Prize per match and 14 match result strings ('C', 'N', or 'D')
// Output : Chandru's prize amount based on overall match outcome

Read prize from user
Set total_prize = prize multiplied by 100
Read results for all 14 matches and concatenate into result_str
Count draws, Chandru wins, and Nirmal wins from result_str
Add half of draw count to each player's win count
If Chandru's count is greater than Nirmal's count
    Print total_prize minus (40 multiplied by prize) as Chandru's prize
Else if Chandru's count is less than Nirmal's count
    Print total_prize minus (60 multiplied by prize) as Chandru's prize
Else
    Print total_prize minus (45 multiplied by prize) as Chandru's prize
```

## Time Complexity

O(1) — the number of matches is fixed at 14, so all operations are constant time.

## Code

[chessMatch.py](../Codes/chessMatch.py)

## Author

hariharasudhan
