import time
print('''Guidelines for giving input 
    format : num1_+_num2
    NOTE : here _ denotes space''')
time.sleep(1.5)
s= input("input  :")
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