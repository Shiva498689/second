import array as ar
s = input("please enter your message : ")
msgs=[]
for  val in range(1,26):
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
     msgs.append(str)
z=""
r=0
for i in range(0,25):
     s=msgs[i]
     itr = [0]*26
     
     for j in range(0,len(s)):
          c= (s[j])
          if(c=="E"or c=="e"):
               itr[0]+=1
          if(c=="T"or c=="t"):
               itr[1]+=1
          if(c=="A"or c=="a"):
               itr[2]+=1
          if(c=="O"or c=="o"):
               itr[3]+=1
          if(c=="I"or c=="i"):
               itr[4]+=1
          if(c=="N"or c=="n"):
               itr[5]+=1
          if(c=="S"or c=="s"):
               itr[6]+=1
          if(c=="H"or c=="h"):
               itr[7]+=1
          if(c=="R"or c=="r"):
               itr[8]+=1
          if(c=="D"or c=="d"):
               itr[9]+=1
          if(c=="L"or c=="l"):
               itr[10]+=1
          if(c=="C"or c=="c"):
               itr[11]+=1
          if(c=="U"or c=="u"):
               itr[12]+=1
          if(c=="M"or c=="m"):
               itr[13]+=1
          if(c=="W"or c=="w"):
               itr[14]+=1
          if(c=="F"or c=="f"):
               itr[15]+=1
          if(c=="G"or c=="g"):
               itr[16]+=1
          if(c=="Y"or c=="y"):
               itr[17]+=1
          if(c=="P"or c=="p"):
               itr[18]+=1
          if(c=="B"or c=="b"):
               itr[19]+=1
          if(c=="V"or c=="v"):
               itr[20]+=1
          if(c=="K"or c=="k"):
               itr[21]+=1
          if(c=="J"or c=="j"):
               itr[22]+=1
          if(c=="X"or c=="x"):
               itr[23]+=1
          if(c=="Q"or c=="q"):
               itr[24]+=1
          if(c=="Z"or c=="z"):
               itr[25]+=1
     a=0
     for p in range(0,25):
          if(itr[p]>=itr[p+1]):
               a=a+1
     if(a>r):
      z=s
      r=a
     else:
          continue

print(z)  
       

                        
