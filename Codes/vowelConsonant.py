class VowelConsonant:
  def isVorC(self,char):
    print("given char is vowel") if char in "aeiou" else print("given char is consonant")
v=VowelConsonant()
char=input("enter a character:")
v.isVorC(char)
