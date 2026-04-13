class codehit:
    def checkhit(self, str1, str2):
        res = ""
        l = min(len(str1), len(str2))
        for i in range(l):
            if str1[i] == str2[i]:
                res += str(i) + "H"
            elif str1[i] in str2:
                res += str(i) + "N"
        return res

c = codehit()
code = input("enter a code: ")
guess = input("enter a guess: ")
print(c.checkhit(code, guess))
