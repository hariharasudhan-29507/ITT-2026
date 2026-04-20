# Author - Hariharasudhan A
class codehit:
    def checkhit(self, str1, str2):
        res = ""
        l = min(len(str1), len(str2)) 
        '''
        because the we are determining the hit guess for two strings
        if we choose smaller length string it will be convinient to compare
        '''
        for i in range(l):
            if str1[i] == str2[i]:
                res += str(i) + "H" # element in same index of both strings should match
            elif str1[i] in str2:
                res += str(i) + "N" # element should present in another string
        return res

c = codehit()
code = input("enter a code: ")
guess = input("enter a guess: ")
print(c.checkhit(code, guess))
