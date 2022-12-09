import numpy as np
import random
avail_pts = []
grd = []
c = 0
class game:
    c = 0
    def __init__(self,a,b,ch):
        global avail_pts
        global grd
        self.player = []
        self.ch = ch
        self.score = 1
        self.x = 0
        i_o = (int(a),int(b))
        self.player.append(i_o)
        avail_pts.remove(i_o)
        grd[i_o[0]-1][i_o[1]-1] = ch
        
    def score_sh(self):
        return self.score
        
    def ai_move(self):
        if(self.x == 1):
            return
        global grd
        global avail_pts
        global c
        K=self.player[len(self.player)-1]
        v = self.ch
        v = v.lower()
        grd[K[0]-1][K[1]-1] = v
        l = [(K[0],K[1]+1),(K[0],K[1]-1),(K[0]-1,K[1]),(K[0]+1,K[1])]
        p=[]
        for i in range(len(l)):
            if l[i] in avail_pts :
                p.append(l[i])
        if(len(p) == 0):
            c+=1
            self.x = 1
        else:
            m = -1
            ix = -1
            for i in p:
                q = [(i[0],i[1]+1),(i[0],i[1]-1),(i[0]-1,i[1]),(i[0]+1,i[1])]
                w = 0
                for j in q:
                    if j in avail_pts:
                        w+=1
                if w>m:
                    m = w
                    ix = p.index(i)
            k = p[ix]
            grd[k[0]-1][k[1]-1] = self.ch
            self.player.append(k)
            print("I choose : " , k , "\n")
            avail_pts.remove(k)
            self.score +=1
            print(np.array(grd))
            #print("AVAILABLE POINTS : " , avail_pts , "\n")
    
    def player_move(self):
        if(self.x == 1):
            return
        global avail_pts
        global grd
        global c
        K=self.player[len(self.player)-1]
        v = self.ch
        v = v.lower()
        grd[K[0]-1][K[1]-1] = v
        l = [(K[0],K[1]+1),(K[0],K[1]-1),(K[0]-1,K[1]),(K[0]+1,K[1])]
        p=[]
        for i in range(len(l)):
            if l[i] in avail_pts:
                p.append(l[i])
        if(len(p) == 0):
            c+=1
            self.x = 1
        else:
            print("avail _OPTIONS = " , p ,"\n")
            x,y = input("enter coordinate  (r,c) : ").split()
            i_o = (int(x),int(y))
            grd[i_o[0]-1][i_o[1]-1] = self.ch
            #self.player[:len(self.player)] = self.ch.lower()
            self.player.append(i_o)
            self.score +=1
            #print("OPP choose : " , k , "\n")
            avail_pts.remove(i_o)
            print(np.array(grd))
            #print("AVAILABLE POINTS : " , avail_pts , "\n")
        
m = int(input("enter order of square grid (min  = 3): "))
for i in range(1,m+1):
    p = []
    for j in range(1,m+1):
        k = (i,j)
        avail_pts.append(k)
        p.append("_")
    grd.append(p)
    
print(np.array(grd))
    



y = input('\nNo of bot player (max = 3 , min= 0)  : ')
y = int(y)
n = int(input('\nenter no of players (n) :  '))

ai_op = [(1,1),(1,m),(m,1),(m,m)]
ai_l = []
if y!=0:
    for i in range(y):
        k = random.choice(ai_op)
        ch = 'A' + str(i+1)
        ai_l.append(game(k[0],k[1],ch))
        ai_op.remove(k)

l = []
for i in range(n):
    print('\n\nPlayer_',i+1)
    print('\n Available coordinate - ')
    print(np.array(grd))
    x,z = input("\nenter coordinate (r,c) : ").split()
    ch = input("enter the symbol : ")
    l.append(game(x,z,ch))

print(np.array(grd))
print(avail_pts)

while len(avail_pts) > 0:
    if c==(n+y):
        break
    for i in range(len(ai_l)):
        print('\nAI_',i+1)
        ai_l[i].ai_move()
        if c==(n+y):
            break
    for i in range(len(l)):
        print('\n\nPlayer_',i+1)
        l[i].player_move()
        

print(np.array(grd),"\n\n")


ply =[]
ply_sc =[]

for i in range(len(l)):
    z = l[i].score_sh()
    p = 'Player_'+str(i+1)
    ply.append(p)
    ply_sc.append(z)
    print('Player_',i+1," : ",z)
for i in range(len(ai_l)):
    p = 'AI_'+str(i+1)
    ply.append(p)
    z = ai_l[i].score_sh()
    print('AI_',i+1," : ",z)
    ply_sc.append(z)


sc = dict(zip(ply,ply_sc))
k = list(sc.keys())
v = list(sc.values())
sorted_value = np.argsort(v)
scorecard = {k[i]: v[i] for i in sorted_value}
result =dict(reversed(list(scorecard.items())))
print("\n\n",result)
