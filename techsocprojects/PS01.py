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


inp = input('''if you want to encode a message please enter "encode" 
     else if you want to "decode" than enter decode :''')
if(inp=="encode"):
     os=input("Please enter your message :")
     num= int(input("Please enter the number from which you want to shift :"))
     encode(os,num)