age=[]
Sum=0
for i in range(20):
    m=int(input())
    if m=="":
        break
    elif int(m) in range(0,120):
        age.append(int(m))
    else:
        print("Invalid")
for i in age:
    if i<=17:
        Sum+=200
    elif i>17 and i<=40:
        Sum+=400
    elif i>40:
        Sum+=300
print(f"Total amount{Sum}INR")
        
    
