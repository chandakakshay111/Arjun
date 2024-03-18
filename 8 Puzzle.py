src = [1,2,3,4,5,6,0,7,8]
target = [1,2,3,4,5,6,7,8,0]

LEVEL = 1


def move(arr,pos,state):
    rh = 9999
    store_st = state.copy()
    for i in range(len(arr)):
        dup_st = state.copy()
        tmp = dup_st[pos]
        dup_st[pos] = dup_st[arr[i]]
        dup_st[arr[i]] = tmp
        trh = countH(dup_st)
        if trh < rh:
            rh = trh
            store_st = dup_st.copy()
    return store_st , rh

def countH(state):
    count = 0
    for i in range(len(state)):
        if state[i] != target[i]:
            count+=1
    return count
h = countH(src)
print("\n ------LEVEL "+str(LEVEL)+"------")
print(src)
print("\nHeuristic Value(Misplaced):"+str(h))
while(h > 0):
    pos = int(src.index(0))
    LEVEL+=1
    arr = list()
    if pos ==0:
        arr = [1,3]
    elif pos == 1:
        arr = [0,2,4]
    elif pos == 2:
        arr = [1,5]
    elif pos == 3:
        arr =[0,4,6]
    elif pos == 4:
        arr = [1,3,5,7]
    elif pos == 5:
        arr = [2,4,8]
    elif pos == 6:
        arr = [3,7]
    elif pos == 7:
        arr = [6,4,8]
    else:
        arr = [5,7]
    src , h = move(arr,pos,src)
    print("\n ------LEVEL "+str(LEVEL)+"------")
    print(src)
    print("\nHeuristic Value(Misplaced):"+str(h))
        
