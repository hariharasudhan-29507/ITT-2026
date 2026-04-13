# Johncook algorithm
"""
1.Take last 2 digits from year as y
2.divide y/4 and add with y
3.add day of the mon
4 sub 1 in jan or feb of a leap year
5.mod by 7
-------------------------------------
to remember
month table
jan 6 may 0 sep 4
feb 2 jun 3 oct 6
mar 2 jul 5 nov 2
apr 5 aug 1 dec 4

week table
sun 0
mon 1
tue 2
wed 3
thu 4
fri 5
sat 6
----------------------------------------
"""

class DayFind:
    def weekTable(self, val):

        week = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]
        if 0 <= val <= 6:
            return week[val]
        return " "

    def monTable(self, val):
        mon_dir = {1: 6, 2: 2, 3: 2, 4: 5, 5: 0, 6: 3, 7: 5, 8: 1, 9: 4, 10: 6, 11: 2, 12: 4}
        return mon_dir.get(val, -1)

    def is_leap(self, year):
        return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

    def FindDay(self, date):
        arr = date.split()
        day = int(arr[0])
        mon = int(arr[1])
        year = int(arr[2])
      
        y = year % 100
        value = y + (y // 4)

        mon_key = self.monTable(mon)
        if mon_key == -1:
            return "Invalid month"

        value = value + mon_key + day
      
        if self.is_leap(year) and mon in (1, 2):
            value -= 1
          
        wk_key = value % 7
        wk_str = self.weekTable(wk_key)
        return wk_str


d = DayFind()
date = input("enter date (DD MM YYYY): ")
print(d.FindDay(date))
