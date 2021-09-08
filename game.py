import random
from playsound import playsound
def start():
    playsound('D:\\rock_paper_scissors\\start.mp3')
def turn():
    playsound('D:\\rock_paper_scissors\\turn.mp3')
def won():
    playsound('D:\\rock_paper_scissors\\won.mp3')   
def lose():
    playsound('D:\\rock_paper_scissors\\lose.mp3')     
def tie():
    playsound('D:\\rock_paper_scissors\\tie.mp3')    
def r1():
    playsound('D:\\rock_paper_scissors\\r1.mp3') 
def r2():
    playsound('D:\\rock_paper_scissors\\r2.mp3')
def r3():
    playsound('D:\\rock_paper_scissors\\r3.mp3')
def r4():
    playsound('D:\\rock_paper_scissors\\r4.mp3')
def game_exit():
    playsound('D:\\rock_paper_scissors\\exit.mp3')       
def record():
    playsound('D:\\rock_paper_scissors\\record.mp3')
         
def game(c,y):
    if c=='r':
        if y=='p':
            return True
        elif y=='s':
            return False
    elif c=='p':
        if y=='s':
            return True
        elif y=='r':
            return False   
    elif c=='s':
        if y=='r':
            return True
        elif y=='p':
            return False               

       
command="yes"
score=0

a=input("audio off or on\n")
print("lets start game rule is\n1.If one player picks rock and one scissors, the player who showed rock wins the dispute. To explain this, say rock crushes scissors (no need to actually crush)")
if(a=="on"):
    r1()
print("2.If one player picks scissors and the other paper, the player who showed scissors succeeds. Scissors cuts paper.")
if(a=="on"):
    r2()
print("3.If a player shows paper while the other shows rock, the player who picked paper succeeds. Paper covers rock.")
if(a=="on"):
    r3()
print("warnning! if your score get less than -3 you will auto exit") 
if(a=="on"):
    r4() 
if(a=="on"):
    start()   
while(command=="yes"):
    n=random.randint(1,3)
    if n==1:
        c='r'
    elif n==2:
        c='p'
    elif n==3:
        c='s'  
    print("computer turns over ")
    if(a=="on"): 
        turn()
    y=input("your turn rock (r) paper(p),scissors(s)? ")
    r=game(c,y)
    print(f"computer have choosen {c} ")
    print(f"you have choose {y} so")
    if r==None:
        print("both are same so tie! ")
        if(a=="on"): 
            tie()
    elif r==True:
        print("you won!")
        if(a=="on"): 
            won()
        score+=1
    elif r==False:
        print("computer won!")  
        if(a=="on"):    
            lose()
        score-=1   
    print("if you want continue it say yes or exit")
    if(a=="on"):
        game_exit()
    command=input()
    if(score<=-10):
        command="exit"    
with open("D:\\rock_paper_scissors\\scr.txt") as f:
    s=f.read()
s=int(s)
if(score>s):
    print("new record!")
    if(a=="on"):
        record()
    with open("D:\\rock_paper_scissors\\scr.txt",'w') as f:
        f.write(str(score))
with open("D:\\rock_paper_scissors\\scr.txt") as f:
    s=f.read()
print(f"Hi-score is {s}")    
            