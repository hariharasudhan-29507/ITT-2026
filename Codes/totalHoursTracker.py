# Author - Hariharasudhan A
class TotalHoursTracker:
        def track(self,time_unit,hours):
                '''
                from the given total hours and unit time 
                we need to find full session work in hours 
                and extra session work in hours
                '''
                perday = 24 # perday - 24 hrs
                full_session = hours//perday 

                extra_session = time_unit - full_session

                # finding full hours and extra hours from given time unit and hours
                full_hours = full_session*perday
                extra_hours = (hours - full_hours) / extra_session

                return int(full_session),int(extra_session)

t = TotalHoursTracker()

time_unit = int(input("Enter time units : "))
hours = int(input("Enter Hours : "))

flag = 0
# checking constraints
flag = 1 if (time_unit < hours and hours >= 24 and hours % 2 == 0) else 0

full_session , extra_session = 0,0
if flag == 1:
        full_session , extra_session = t.track(time_unit,hours)
        # printing it in console
        print("full session :",full_session , "\nextra session :",extra_session)

else :
        print("Invalid input ")
