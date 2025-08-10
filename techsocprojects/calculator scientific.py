import time
import math


time.sleep(1)
s= input("input  :")

if(s[0:3]=="exp"):
   num1=float(s[4:(len(s)-1)])
   print("Output :",math.exp(num1))

if(s[0:3]=="sin"):
   num1= (float(s[4:(len(s)-1)]))*(math.pi/180)
   print("Output :",(math.sin(num1)))
   exit()
if(s[0:3]=="tan"):
   num1= (float(s[4:(len(s)-1)]))*(math.pi/180)
   print("Output :",(math.tan(num1)))
   exit()
if(s[0:3]=="cos"):
   num1= (float(s[4:(len(s)-1)]))*(math.pi/180)
   print("Output :",(math.cos(num1)))
   exit()
if(s[0:4]=="asin"):
   num1= float(s[5:(len(s)-1)])
   print("Output :",(math.asin(num1)),"radian")
   exit()
if(s[0:4]=="acos"):
   num1= float(s[5:(len(s)-1)])
   print("Output :",(math.acos(num1)),"radian")
   exit()
if(s[0:4]=="atan"):
   num1= float(s[5:(len(s)-1)])
   print("Output :",(math.atan(num1)),"radian")
   exit()
if(s[0:2]=="ln"):
  x= float((s[3:(len(s)-1)]))
  ln=math.log(x) 
  print("Output: ",ln)
  exit()

elif(s[0]=="0"or s[0]=="1"or s[0]=="2"or s[0]=="3"or s[0]=="4"or s[0]=="5"or s[0]=="6"or s[0]=="7"or s[0]=="8"or s[0]=="9"):
 len=len(s)
 if(s[len-1]=="0"or s[len-1]=="1"or s[len-1]=="2"or s[len-1]=="3"or s[len-1]=="4"or s[len-1]=="5"or s[len-1]=="6"or s[len-1]=="7"or s[len-1]=="8"or s[len-1]=="9"):
   

                          i= s.find(" ")
                          num1= float(s[0:i])
                          num2= float(s[i+3:len(s)])
                          operator= s[i+1:i+2]
 
                          if(operator=='+'):
                             print("output :",(num1+num2))
                          elif(operator=='-'):
                             print("output :",(num1-num2))
                          elif(operator=='*'):
                             print("output :",(num1*num2))
                          elif(operator=='/'):
                             print("output :",(num1/num2))
                          elif(operator=='%'):
                             print("output :",(num1%num2))
                          elif(operator=='^'):
                             print("output :",(num1**num2))
else:
    print('please read the guidelines at Read.md and than retry')                              