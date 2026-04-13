class TimeDiffCalci:
   def calculate(self,timestamp1,timestamp2):
      date1,time1=timestamp1[:9],timestamp1[11:]
      date2,time2=timestamp2[:9],timestamp2[11:]

      date1_array=date1.split("-")
      date2_array=date2.split("-")

      time1_array=time1.split(":")
      time2_array=time2.split(":")


      d1,t1=list(date1_array),list(time1_array)
      d2,t2=list(date2_array),list(time2_array)

      if self.checkDate(d1,d2):
         return self.diff(t1,t2)
   def diff(self,time1,time2):
      hrs1,min1,sec1=int(time1[0]),int(time1[1]),int(time1[2])
      hrs2,min2,sec2=int(time2[0]),int(time2[1]),int(time2[2])

      hrs=hrs2-hrs1
      mins=min2-min1
      secs=sec2-sec1

      difference=(hrs*3600)+(mins*60)+secs

      return difference

   def checkDate(self,date1,date2):
      for i in range(len(date1)):
         if int(date1[i])==int(date2[i]):
            return True


t=TimeDiffCalci()
timestamp1=input("enter a timestamp:")
timestamp2=input("enter another timestamp:")

print(t.calculate(timestamp1,timestamp2))
