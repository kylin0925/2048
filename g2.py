import random
def move(arr):
    #arr = [2,2,2,2,0]
    idx = 0
    #print '------' 
    merged = 0
    for i in range(3):
        r = [x for x in arr if x > 0]
        if len(r) !=4:
            merged = 1
            r +=[0 for x in range(4-len(r))]
        #print r

        if r[i] == r[i+1]:
            r[i] +=r[i+1]
            r[i+1] = 0
            merged = 1
        for i in range(4):
            arr[i]=r[i]

    return merged
    #print ":",arr
'''
            j = i
            for j in range(i-1,-1,-1):
                if arr[j] > 0:
                    break
            #print i,j,arr[i],arr[j]
            if j >=0 and i!=j:
                if arr[j] ==arr[i] or arr[j] ==0:
                    arr[j]+=arr[i]
                    arr[i] = 0
                    #print "1",arr
                else:
                    arr[j+1] = arr[i]
                    if j + 1 != i:
                        arr[i] = 0
                    #print "2",arr
'''                 
    
def move_left(arr):
    r = 0
    for row in arr:
       r |= move(row)
 
    return r
def move_right(arr):
    idx = 0 
    r = 0
    for row in arr:
        row = row[::-1]
        r |=move(row)
        row = row[::-1]
        arr[idx] = [row[x] for x in range(4)]
        idx +=1 
    return r

def move_up(arr):
    idx = 0
    r = 0 
    for i in range(4):
        row = [arr[x][i] for x in range(4)]
        r |=move(row)
        #print row
        for y in range(4):
            arr[y][idx] = row[y] 
        idx +=1
    return r

def move_down(arr):
    idx=0
    r = 0
    for i in range(4):
        row = [arr[x][i] for x in range(4)]
        row = row[::-1]
        r |=move(row)
        #print row
        row = row[::-1]
        for y in range(4):
            arr[y][idx] = row[y]
        idx+=1
    return r

def dump(arr):
    for r in arr:
        print r

def gen_num(arr):
    while True:
        r = random.randint(0,1)
        num = 2**(r+1)
        x = random.randint(0,3)
        y = random.randint(0,3) 
        if arr[y][x] == 0:
            #print x,y,num
            return x,y,num

def check_zero(arr):
    zero_cnt = 0
    for a in arr:
        zero_cnt +=a.count(0)
    if zero_cnt > 0:
        return 1
    else: 
        return 0

def check(arr):
    for i in range(0,3):
        for j in range(0,4):
            if j != 3 and arr[i][j] == arr[i][j+1]:
                return 1
            elif arr[i][j] == arr[i+1][j]:
                return 1
    print 'gg'
    return 0
arr =[
     [0,0,0,0],
     [0,0,0,0],
     [0,0,0,0],
     [0,0,0,0]
    ]
#move_left1(arr)
#dump(arr)
x,y,num = gen_num(arr)
arr[y][x] = num

x,y,num = gen_num(arr)
arr[y][x] = num


dump( arr)
while True:
    r = raw_input(' :')
    rc = 0
    if r == 'u':
        rc = move_up(arr)
    elif r == 'd':
        rc = move_down(arr)
    elif r == 'l':
        rc = move_left(arr)
    elif r == 'r':
        rc = move_right(arr)
    elif r == 'q':
        break
    if rc >0:
        if check_zero(arr) > 0:
            x,y,num = gen_num(arr)
            arr[y][x] = num
    dump(arr)
    if check_zero(arr) == 0 and check(arr) == 0:
        print "game over"
        break

