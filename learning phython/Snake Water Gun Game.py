import random
import time

k= True
ch= input('''if you want to play please enter yes else no ''')
if(ch=="yes"):
   k= True
else:
   k= False


dict = {
   's':"snake 🐍",
   'g' :"gun🔫💥💀",
   'w': "water 🌊"
     }



 
  
while(k):
  computer= random.choice(["s",'w','g'])
  user = input('''enter your choice
             s for snake 🐍 
             w for water 🌊
             g for gun  🔫💥💀
               :  ''')
  time.sleep(1)
  print(f'''you have entered {dict[user]}''')
  time.sleep(2)
  print(f'''computer has choosen {dict[computer]} ''')
  time.sleep(1)
  if(computer==user):
    print("Congrats! But its a draw 💀")
  else :
    if(computer== 's' and user== 'w' ):
        print("You lost 🫣 ")
    elif(computer== 's' and user== 'g' ):
        print ("You win ✌️ ")
    elif(computer== 'g' and user== 'w' ):
        print("You win ✌️")
    elif(computer== 'g' and user== 's' ):   
        print("You lost 🫣 ")
       
    elif(computer== 'w' and user== 's' ):
        print("You win ✌️ ")
    elif(computer== 'w' and user== 'g'):
        print("You lost 🫣")
    else:
        print("Something went wrong")
  ch= input('''if you want to play again please enter yes else no
            :    ''')   
  if(ch=="yes"):
    k=True
  else:
    k= False