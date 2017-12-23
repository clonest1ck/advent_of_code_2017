
def add(pos, direct):
    return [pos[0] + direct[0], pos[1] + direct[1]]


f = open("in19.txt", 'r')
themap = []

for line in f.readlines():
    line = line.split("\n")
    themap.append([char for char in line[0]])

start = themap[0].index("|")
direction = [1, 0]
position = [0, start]
movesPossible = True
letters = []
steps = 0;

while(movesPossible):
    position = add(position, direction)
    steps += 1
    directive = themap[position[0]][position[1]]

    if(directive == "+"):
        left = None
        right = None
        up = None
        down = None
        if(position[1] > 0 and direction[1] != 1):
            left = themap[position[0]][position[1] - 1]
        if(position[1] < len(themap[0]) - 1 and direction[1] != -1):
            right = themap[position[0]][position[1] + 1]
        if(position[0] > 0 and direction[0] != 1):
            up = themap[position[0] - 1][position[1]]
        if(position[0] < len(themap) - 1 and direction[0] != -1):
            down = themap[position[0] + 1][position[1]]

        if(left == "-"):
            direction = [0, -1]
        elif(right == "-"):
            direction = [0, 1]
        elif(up == "|"):
            direction = [-1, 0]
        elif(down == "|"):
            direction = [1, 0]

    elif (directive == "|" or directive == "-"):
        continue
    elif (directive == " "):
        movesPossible = False
    else:
        letters.append(directive)

print "Task 1: " + str("".join(letters))
print "Task 2: " + str(steps);
