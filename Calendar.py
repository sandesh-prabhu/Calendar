print("Calendar")
date=int(input("Enter Date:"))
month=int(input("Enter Month:"))
year=int(input("Enter Year:"))
oddyear=[5,3,1,0]
oddleapmonth=[5,1]
oddmonth=[6,2,2,5,0,3,5,1,4,6,2,4]
odd=0
days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
yearmod400=year%400
modyear=yearmod400
if (modyear in range(1,101)):
    odd=oddyear[0]
elif (modyear in range(101,201)):
    odd=oddyear[1]
elif (modyear in range(201,301)):
    odd=oddyear[2]
else:
    odd=oddyear[3]
modyear%=100
quotientyear=modyear%4
odd+=modyear+quotientyear
remainderyear=odd%7
finalsum=remainderyear
if month<=2:
    if (yearmod400==0 or ((yearmod400%100)%4==0 and (yearmod400%100)!=0)):#leap year
        finalsum+=oddleapmonth[month-1]
    else:
        finalsum+=oddmonth[month-1]
else:
    finalsum+=oddmonth[month-1]
result=(finalsum+date)%7
print(days[result])
