import time
import math

print('''Guidelines for giving input 
    format : num1_+_num2
    NOTE : here _ denotes space
 ** if you want natural log then sample input should be like given below
      input : ln("your number")
 **for trigonometric functions enter angle in degrees for sin ,cos, tan 
      && for inverse trigo output will be in radian 
      
 *** for calculating exponent of a number
     Sample input: exp(____) your number in blank space ''')
time.sleep(1)
s= input("input  :")
if(s[0:3]=="exp"):
   num1=float(s[4:(len(s)-1)])
   print("Output :",math.exp(num1))

if(s[0:3]=="sin"):
   num1= float(s[4:(len(s)-1)])
   print("Output :",(math.sin(num1)))
   exit()
if(s[0:3]=="tan"):
   num1= float(s[4:(len(s)-1)])
   print("Output :",(math.tan(num1)))
   exit()
if(s[0:3]=="cos"):
   num1= float(s[4:(len(s)-1)])
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

else:
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