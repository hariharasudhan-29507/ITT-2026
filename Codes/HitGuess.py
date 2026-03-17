class codehit:
    def checkhit(self,str1,str2):
        str1cp=list(str1)
        str2cp=list(str2)
        res=""
        if len(str2)<len(str1):
            l=len(str2)
        else:
            l=len(str1)
        for i in range(l):
            for j in range(l):
                if str1[i]==str2[j]:
                    res=res+(str(i)+"H")
                elif str1[i] in str2:
                    res=res+(str(i)+"N")
        return res
c=codehit()
code=input("enter a code:")
guess=input("enter a code to guess")
print(c.checkhit(code,guess))
