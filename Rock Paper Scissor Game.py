"""
    0 -> Rock
    1 -> Paper
    2 -> Scissor
"""

Rock="""  
     --------         
---"  _ _ _ _}
      {_ _ _ _}
      {_ _ _-}
      {_ _--}
--~,_ _{_ _}
"""

Paper="""
     --------         
---"    _ _ _} _ _
         _ _ _ _ _}
           _ _ _ _-}
          _ _ _ _-}
--~,_ _ _ _ _ __}
"""

Scissor="""
     --------         
---"    _ _ _} _ _
         _ _ _ _ _-}
        _ _ _ _ _ _-}
          {_ _}
--~, _ _ _{_}

"""
Game_Image=[Rock,Paper,Scissor]
import random
you=int(input("Enter your choice(0/1/2) :"))
List=[0,1,2]
computer=random.choice(List)
if(you < 0 or you > 2):
    print("You entered invalid choice")
else:
    print(Game_Image[you])
    print(f"Computer choose :")#print(f"Computer choice :{computer}")
    print(Game_Image[computer])
    if(computer==0 and you==0):
        print("Match tied")
    elif(computer==0 and you==1):
        print("You wins")
    elif(computer==0 and you==2):
        print("Computer wins")
    elif(computer==1 and you==0):
        print("Computer wins")
    elif(computer==1 and you==1):
        print("Match tied")
    elif(computer==1 and you==2):
        print("You wins")
    elif(computer==2 and you==0):
        print("You wins")
    elif(computer==2 and you==1):
        print("Computer wins")
    elif(computer==2 and you==2):
        print("Match tied")
    else:
        print("Invalid")
