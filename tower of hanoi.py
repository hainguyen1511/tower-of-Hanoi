#Name: Hai T. Nguyen
def pop(towers, location, sp):
    if sp[location] == -1:
        return -1
    temp = towers[location][sp[location]]
    towers[location][sp[location]] = -1
    sp[location] = sp[location] - 1
    return temp

def push(towers, location, stk, sp):
    sp[location] = sp[location] + 1
    towers[location][sp[location]] = stk

def mover(n, origin, destination, towers, sp):
    if n > 0:
        temp = pop(towers, origin, sp)
        if temp != -1:
            push(towers, destination, temp, sp)
def solver(n, towers, sp, start, end):
    if n == 0:
        display_towers(towers)
        return
    elif n == 1:
        mover(n, start, end, towers, sp)
        display_towers(towers)
        input("Press Enter to continue...")
    else:
        other = 3 - (start + end)
        solver(n - 1, towers, sp, start, other)
        mover(n, start, end, towers, sp)
        display_towers(towers)
        input("Press Enter to continue...")
        solver(n - 1, towers, sp, other, end)
def display_towers(towers):
    print()
    k = len(towers[0]) - 1
    while k >= 0:
        if towers[0][k] != -1:
            print(towers[0][k] + 1, end="  ")
        else:
            print("+", end="  ")
        if towers[1][k] != -1:
            print(towers[1][k] + 1, end="  ")
        else:
            print("+", end="  ")
        if towers[2][k] != -1:
            print(towers[2][k] + 1, end="  ")
        else:
            print("+", end="  ")
        print()
        k -= 1
    print("_______")
######### main ############
# Example using a 5-ring tower
n = int(input("Enter number of disc: "))
tower0 = []
tower1 = []
tower2 = []
i = n-1
while(i >= 0) :
    tower0.append(i)
    tower1.append(-1)
    tower2.append(-1)
    i -= 1
towers = [tower0,tower1,tower2]
#towers[0] = [4,3,2,1,0]  # tower 0
#towers[1] = [-1,-1,-1,-1,-1]  # tower 1
#towers[2] = [-1,-1,-1,-1,-1]  # tower 2
sp = [n-1,-1,-1]# stack pointers for each tower
display_towers(towers)
solver(n, towers, sp, 0, 2)