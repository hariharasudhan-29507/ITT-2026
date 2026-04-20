class TotalHoursTracker:
        def track(self,time_unit,hours):
                perday = 24
                full_session = hours//perday

                extra_session = time_unit - full_session

                full_hours = full_session*perday
                extra_hours = (hours - full_hours) / extra_session

                return int(full_session),int(extra_session)

t = TotalHoursTracker()

time_unit = int(input("Enter time units : "))
hours = int(input("Enter Hours : "))

flag = 0
flag = 1 if (time_unit < hours and hours >= 24 and hours % 2 == 0) else 0

full_session , extra_session = 0,0
if flag == 1:
        full_session , extra_session = t.track(time_unit,hours)

        print("full session :",full_session , "\nextra session :",extra_session)

else :
        print("Invalid input ")
