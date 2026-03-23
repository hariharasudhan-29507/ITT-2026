prize=int(input("Enter prize:"))
total_prize=prize*100
result_str=""
match_count=14
for i in range(match_count):
    sub_str=input("enter result of match:")
    result_str=result_str+sub_str
draw_count=result_str.count("D")
chandru_count=result_str.count("C")+(draw_count/2)
nirmal_count=result_str.count("N")+(draw_count/2)
if chandru_count>nirmal_count:
    print("chandru won with prize pool",(total_prize-(60*prize)))
elif chandru_count<nirmal_count:
     print("chandru won with prize pool",(total_prize-(40*prize)))
else:
     print("chandru won with prize pool",(total_prize-(55*prize)))
