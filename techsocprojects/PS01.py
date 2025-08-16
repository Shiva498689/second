def encode(s,val):
    length= len(s)
    str=""
    for i in range(length):
        c=s[i]
        if(ord(c)>=65 and ord(c)<=90 ):
            ascii=ord(c)
            if(ascii + val <= 90):
                str+=chr(ascii+val)
            else:
                 n=ascii+val-90+64
                 str+=chr(n)
        elif(ord(c)>=97 and ord(c)<=122):
            
                ascii=ord(c)
                if(ascii + val <= 122):
                     str+=chr(ascii+val)
                else:
                     n=ascii+val-122+96
                     str+=chr(n)
        else:
             str+=c
    print("Output :",str)

def decode(s,val):
    length= len(s)
    str=""
    for i in range(length):
        c=s[i]
        if(ord(c)>=65 and ord(c)<=90 ):
            ascii=ord(c)
            if(ascii - val >= 65):
                str+=chr(ascii-val)
            else:
                 n=91-(65-(ascii-val)) 
                 str+=chr(n)
        elif(ord(c)>=97 and ord(c)<=122):
            
                ascii=ord(c)
                if(ascii - val >= 97):
                     str+=chr(ascii-val)
                else:
                     n=122-(97-(ascii-val)) 
                     str+=chr(n)
        else:
             str+=c
    print("Output :",str)

inp = input('''if you want to encode a message please enter "encode" 
     else if you want to "decode" than enter decode :''')
if(inp=="encode"):
     os=input("Please enter your message :")
     num= int(input("Please enter the number from which you want to shift :"))
     encode(os,num)
if(inp=="decode"):
     os=input("Please enter your message :")
     num= int(input("Please enter the number from which you want to shift or decode  :"))
     decode(os,num)