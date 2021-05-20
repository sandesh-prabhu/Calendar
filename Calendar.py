print("Calendar")
date=int(input("Enter Date:"))              #Ex: 5
month=int(input("Enter Month:"))            #Ex: 2
year=int(input("Enter Year:"))              #Ex: 1992
oddyear=[5,3,1,0]
oddleapmonth=[5,1]
oddmonth=[6,2,2,5,0,3,5,1,4,6,2,4]
odd=0
days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
yearmod400=year%400                         #( 1992 % 400 ) = 392
modyear=(yearmod400//100)*100               #( 392 // 100 ) * 100 = 300
if (modyear==100):
    odd=oddyear[0]
elif (modyear==200):
    odd=oddyear[1]
elif (modyear==300):
    odd=oddyear[2]                          #1
else:
    odd=oddyear[3]
modyear=yearmod400%100                      #( 392 % 100 ) = 92
quotientyear=modyear//4                     #( 92 // 4 ) = 23
odd+=modyear+quotientyear                   #( 1 + 92 + 23 ) = 116
remainderyear=odd%7                         #( 116 % 7 ) = 4
finalsum=remainderyear                      #4
if month<=2:                                #2      for January and February
    if (yearmod400==0 or ((yearmod400%100)%4==0 and (yearmod400%100)!=0)): #for leap year
        finalsum+=oddleapmonth[month-1]     #( 4 + 1 ) = 5
    else:
        finalsum+=oddmonth[month-1] #for regular year
else:
    finalsum+=oddmonth[month-1] #for rest of the months
result=(finalsum+date)%7                    #( 5 + 5 ) % 7 = 3
print(days[result])                         #Wednesday
