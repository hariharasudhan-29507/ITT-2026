# Valid Email

## Description

Validates whether an input string is a valid email address by checking for the presence of an @ symbol, a domain dot, and the absence of invalid characters in the domain portion.

## Approach

Read the email input from the user. Check that the string is not empty. Locate the @ symbol — if it is absent, the email is invalid. After finding @, scan the domain portion for invalid special characters. Then locate the domain dot and verify that neither the domain nor the extension portion contains digits. If all checks pass, the email is valid.

## Algorithm

```
ALGORITHM VALID_EMAIL
// Validates a user-provided email address string
// Input  : A string mail representing a potential email address
// Output : "this mail is valid" or an invalid message

Read mail from user
If mail is empty, print required field message and exit
Find index of '@' in mail; if not found, print error and exit
Scan characters after '@' for invalid special characters; if found, print error and exit
Find index of '.' in mail; if not found, print error and exit
Check that no digits appear between '@' and '.' or after '.'; if found, print error and exit
If all checks passed, print "this mail is valid"
```

## Time Complexity

O(n) — the string is scanned a fixed number of times where n is the length of the email.

## Code

[validMail.py](../Codes/validMail.py)

## Author


Hariharasudhan A
sophomore in CSE , MEPCO schlenk engineering college 
Sivakasi
reach me : sudanayyappann_bcs28@mepcoeng.ac.in
