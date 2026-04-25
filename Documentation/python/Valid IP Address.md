# Valid IP Address

## Description

Validates whether an input string is a valid IPv4 address by checking the number of dots and verifying each octet is a numeric value between 0 and 255.

## Approach

Count the number of dot characters in the input. If the count is not exactly 3, the address is invalid. Otherwise, split the string by dots to get the four octets. Check that each octet is numeric and its integer value falls within 0 to 255. If all checks pass, the IP address is valid.

## Algorithm

```
ALGORITHM VALID_IP_ADDRESS
// Validates an IPv4 address string
// Input  : A string ip representing a potential IPv4 address
// Output : "valid IP address" or an invalid/error message

Read ip from user
Count number of '.' characters in ip
If count is not equal to 3
    Print "not an IPv4" and exit
Split ip by '.' into list iplist
Set flag = 0
For each octet in iplist
    If octet is numeric AND its integer value is between 0 and 255 (inclusive)
        Set flag = 1
    Else
        Set flag = 0 and break
If flag equals 1
    Print "valid IP address"
Else
    Print "not a valid IP address"
```

## Time Complexity

O(1) — an IPv4 address always has exactly 4 octets, so the number of operations is constant.

## Code

[validIP.py](../Codes/validIP.py)

## Author

Hariharasudhan A  
sophomore in CSE , MEPCO schlenk engineering college  
Sivakasi  
reach me : sudanayyappann_bcs28@mepcoeng.ac.in
