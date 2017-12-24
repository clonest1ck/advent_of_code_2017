
def getPossibilites(pins, components):
    possible = []
    for c in components:
        if c[0] == pins:
            clist = components[:]
            clist.remove(c)
            possible.append([c, clist])
        elif c[1] == pins:
            clist = components[:]
            clist.remove(c)
            c.reverse()
            possible.append([c, clist])

    return possible

f = open("in24.txt", 'r')
components = [map(int, x.split("\n")[0].split("/")) for x in f.readlines()]

finalBridges = []
current = []

current = getPossibilites(0, components)
while(len(current) > 0):
    nextCurrent = []
    for c in current:
        possible = getPossibilites(c[0][-1], c[1])
        if(len(possible) != 0):
            for p in possible:
                nextCurrent.append([c[0] + p[0], p[1]])
        else:
            finalBridges.append(c[0])
    current = nextCurrent

result = max([sum(x) for x in finalBridges])
print "Task 1: "  + str(result)

longest = 0
bridges = []
for bridge in finalBridges:
    if len(bridge) > longest:
        longest = len(bridge)
        bridges = [bridge]
    elif(len(bridge) == longest):
        bridges.append(bridge)

result = max([sum(x) for x in bridges])
print "Task 2: "  + str(result)
