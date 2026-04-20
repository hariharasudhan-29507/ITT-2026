# Author - Hariharasudhan A

prize=int(input("Enter prize:"))
total_prize=prize*100
result_str=""

match_count=14
'''
In 14 matches ,we need to find the amount of money chandru recieves , if he won/loss/draw
'''
for i in range(match_count):
    sub_str=input("enter result of match:")
    result_str=result_str+sub_str

# array will have D(draw) , C(chandru won) , N(nirmal won)
draw_count=result_str.count("D")
chandru_count=result_str.count("C")+(draw_count/2)
nirmal_count=result_str.count("N")+(draw_count/2)

if chandru_count>nirmal_count:
    print("chandru recieves prize pool",(total_prize-(40*prize)))

elif chandru_count<nirmal_count:
     print("chandru recieves prize pool",(total_prize-(60*prize)))

else:
     print("chandru recieves prize pool",(total_prize-(45*prize)))
