weight=int(input())
if(0<weight<=2000):
  print("25 MINUTES")
elif(2000<weight<=4000):
  print("35 MINUTES")
elif(4000<weight<=7000):
  print("45 MINUTES")
elif(weight==0):
  print("0")
else:
  print("OVER LOAD")
