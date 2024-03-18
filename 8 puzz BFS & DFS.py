def print_grid(lst):
    # Check if the list has 9 elements
    if len(lst) != 9:
        print("Invalid list length")
        return

    # Loop through the list and print each element in a 3x3 grid
    for i in range(9):
        print("|", lst[i], "|", end="")
        # Add a new line after every third element
        if (i + 1) % 3 == 0:
            print("\n", "_" * 9)


def bfs(src,target):
    queue = []
    queue.append(src)
    
    exp = []
    i = 1
    while len(queue) > 0:
        source = queue.pop(0)
        exp.append(source)
        
        print("iteration:",i)
        i = i+1
        print_grid(source)
        
        if source==target:
            print("success")
            return
        
        poss_moves_to_do = []
        poss_moves_to_do = possible_moves(source,exp)
        
        for move in poss_moves_to_do:
            
            if move not in exp and move not in queue:
                queue.append(move)
def possible_moves(state,visited_states): 
    b = state.index(0)
    d = []
    
    if b not in [0,1,2]: 
        d.append('u')
    if b not in [6,7,8]: 
        d.append('d')
    if b not in [0,3,6]: 
        d.append('l')
    if b not in [2,5,8]: 
        d.append('r')
        
    pos_moves_it_can = []
        
    for i in d:
        pos_moves_it_can.append(gen(state,i,b))
        
    return [move_it_can for move_it_can in pos_moves_it_can if move_it_can not in visited_states]
def gen(state, m, b):
    temp = state.copy()                              
    
    if m=='d':
        temp[b+3],temp[b] = temp[b],temp[b+3]
    
    if m=='u':
        temp[b-3],temp[b] = temp[b],temp[b-3]
    
    if m=='l':
        temp[b-1],temp[b] = temp[b],temp[b-1]
    
    if m=='r':
        temp[b+1],temp[b] = temp[b],temp[b+1]
        
    return temp
src = [1,2,3,4,5,0,6,7,8]
target = [1,2,3,4,5,6,7,8,0]         
bfs(src, target)