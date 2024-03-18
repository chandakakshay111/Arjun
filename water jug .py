x = 0 # no. of gallons of water in 4 gallon jug 
y = 0 # no. of gallons of water in 3 gallon jug


def amountOf_Water_CanBe_Addedto_x(x):
    if (x < 4):       
        X = int(input("Enter gallons of water u want to add in 4 gallon jug:-")) 
        if (X <= 4):
            x = X
            print("This amount of water has been added!")
        else:
            print("U cannot add this amount of water")
    print(x)
    return x

def amountOf_Water_CanBe_Addedto_y(y):
    if (y < 3):
        Y = int(input("Enter gallons of water u want to add in 3 gallon jug:-"))        
        if (Y <= 3):
            y = Y
        else:
            print("U cannot add this amount of water")
    print(y)     
    return y

    # transfer water 
def transferWater_x_to_y(x, y):
    # from x to y 
        X = int(input("Enter transfer amount of water from 4 gallon jug to 3 gallon jug"))
        if (X <= x):
            if (X + y <= 3):
                y += X
                print("The amount", X, "has been transferred")
        else:
            print("The amount of water can't be transferred as the amount mentioned is not present")
        print("(", x, y, ")")
        return x, y

def transferWater_y_to_x(x, y):
    # from y to x 
        Y = int(input("Enter transfer amount of water from 4 gallon jug to 3 gallon jug"))
        if (Y <= y):
            if (Y + x <= 4):
                y += Y
                print("The amount", Y, "has been transferred")
        else:
            print("The amount of water can't be transferred as the amount mentioned is not present")
        print("(", x, y, ")")
        return x, y

def empty_x(x):   
     x = 0
     print("The first gallon has been emptied!", x)
     return x

def empty_y(y):
     y = 0
     print("The second gallon has been emptied!", y)
     return y

## main_5
n = 1
while(n == 1):
    print("Water Jug Problem:\n1.Amount to water to be added to 4 gallon jug\n2.Amount to water to be added to 3 gallon jug\n3.Transfer water from 4 to 3\n4.Transfer from 3 to 4\n5.Empty x\n6.Empty y\n")
    i = int(input("Enter the operation to be performed: "))
    if(i == 1):
         amountOf_Water_CanBe_Addedto_x(x)
    elif(i == 2):
         amountOf_Water_CanBe_Addedto_y(y)
    elif(i == 3):
         transferWater_x_to_y(x, y)
    elif(i == 4):
         transferWater_y_to_x(x, y)
    elif(i == 5):
         empty_x(x)
    elif(i == 6):
         empty_y(y)
    else:
         n = 0         