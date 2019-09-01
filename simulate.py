# http://gipa.csie.io/demo/gold/

amount = [0,0,0]

# food,wood,gold
work = [1,1,1]

cap = [500,500,500]

level = [10,5,2]

cost = [[0,0,0],[0,0,0],[0,0,0]]
avail = [[0,0,0],[0,0,0],[0,0,0]]

upgrade = 0
time = 0


def update_cost():
    for i in range(3):
        cost[0][i] = work[i]*50
        cost[1][i] = cap[i]//2
        cost[2][i] = level[i]*100
    
def find_move():
    pair = []
    for i in range(3):
        for j in range(3):
            avail[i][j] = 0
            # storage is not important
            if i==1 or j==1:
                priority = 0
            else:
                priority = 1
            if cost[i][j]<=amount[i]:
                avail[i][j] = 1
                diff = speed_diff(i,j)
                pair.append((priority,diff,i,j))
    #print(cost,avail)
    
    if not pair:
        return -1
    # greedy choose: best speed.diff, food and gold first
    pair.sort(key = lambda x: (-x[0],-x[1],x[3]))
    print(pair)
    return pair[0]

def level_up(x,y):
    if x==0: # level up worker
        work[y] += 1
    elif x==1:
        cap[y] += 500
    elif x==2:
        level[y] += 1
        
    amount[x] -= cost[x][y]
    
def speed_diff(x,y):
    new_level = list(level)
    new_work = list(work)
    if x==1:
        return 1
    elif x==0:
        new_work[y] += 1
    elif x==2:
        new_level[y] += 1
        
    return (new_work[y]*new_level[y])/(work[y]*level[y])
      

# initial cost
update_cost()
while time<=500:

    # choose move (limit: 3 move per second)
    for k in range(1):
        mov = find_move()
        
        # level up
        if mov!=-1:
            print(time,mov)
            upgrade += 1
            if upgrade==100:
                break
            p,d,x,y = mov
            level_up(x,y)
            # update cost
            update_cost()
            #print(amount)
        else:
            break
    
    if upgrade==100:
        break
        
    # update speed and amount
    speed = [0,0,0]
    for i in range(3):
        speed[i] = level[i]*work[i]
    
    for i in range(3):
        amount[i] = min(cap[i],amount[i]+speed[i])
    print(time,amount,speed)
    time += 1

print(time)
