def Task1():
    f = open("in22.txt", 'r')
    infected = {}
    pos = (0,0)
    d = (0,1)
    newly_infected = 0

    lines = [x.split("\n")[0] for x in f.readlines()]
    maxindex = len(lines) / 2

    for i in range(len(lines)):
        for j in range(len(lines)):
            if(lines[i][j] == "#"):
                index = (j-maxindex, maxindex-i)
                infected[index] = True

    for i in range(10000):
        if(not infected.has_key(pos) or infected[pos] == False):
            if d == (1, 0):
                d = (0, 1)
            elif d == (-1, 0):
                d = (0, -1)
            elif d == (0, 1):
                d = (-1, 0)
            elif d == (0, -1):
                d = (1, 0)
            infected[pos] = True
            newly_infected += 1
        else:
            if d == (1,0):
                d = (0, -1)
            elif d == (-1, 0):
                d = (0, 1)
            elif d == (0, 1):
                d = (1, 0)
            elif d == (0, -1):
                d = (-1, 0)
            infected[pos] = False

        pos = tuple(map(sum, zip(pos, d)))
    return newly_infected

def Task2():
    f = open("in22.txt", 'r')
    infected = {}
    pos = (0,0)
    d = (0,1)
    newly_infected = 0

    lines = [x.split("\n")[0] for x in f.readlines()]
    maxindex = len(lines) / 2

    for i in range(len(lines)):
        for j in range(len(lines)):
            if(lines[i][j] == "#"):
                index = (j-maxindex, maxindex-i)
                infected[index] = "I"

    i = 0
    while(i < 10000000):
        if(not infected.has_key(pos) or infected[pos] == "C"):
            if d == (1, 0):
                d = (0, 1)
            elif d == (-1, 0):
                d = (0, -1)
            elif d == (0, 1):
                d = (-1, 0)
            elif d == (0, -1):
                d = (1, 0)
            infected[pos] = "W"
        elif(infected[pos] == "W"):
            infected[pos] = "I"
            newly_infected += 1
        elif(infected[pos] == "F"):
            infected[pos] = "C"
            d = tuple(map(mul, zip(d, (-1,-1))))
        else:
            if d == (1,0):
                d = (0, -1)
            elif d == (-1, 0):
                d = (0, 1)
            elif d == (0, 1):
                d = (1, 0)
            elif d == (0, -1):
                d = (-1, 0)
            infected[pos] = "F"

        pos = tuple(map(sum, zip(pos, d)))
        i += 1
    return newly_infected

def mul(l):
    res = 1
    for ls in l:
        res *= ls
    return res

print "Task 1 " + str(Task1())
print "Task 2 " + str(Task2())
