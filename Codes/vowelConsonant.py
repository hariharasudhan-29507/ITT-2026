# Author - Hariharasudhan A
class VowelConsonant:
  '''
  simple vowel or consonant checking
  '''
  def isVorC(self,char): # ternary condition
    print("given char is vowel") if char in "aeiou" else print("given char is consonant")
v=VowelConsonant()
char=input("enter a character:")
v.isVorC(char)
