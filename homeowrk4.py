def myfunc3 ():
  num = int(input("Enter a number: "))
  num1 = int(input("Enter another number: "))
  if ((num %2 ==0), (num1 %2 ==0)): #even
    print (num, num1)
    print (min(num, num1))
  elif ((num %2 !=0), (num1 %2 !=0)): #odd
    print ("hi")
    print(max(num, num1))
  else: 
    print("hi")
    #print (max(num, num1))
myfunc3 ()