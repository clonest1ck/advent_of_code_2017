f = open("in25.txt", 'r')
begin = f.readline().split(" ")[-1][0]
checksum_at = int(f.readline().split(" ")[-2])
states = {}

lines = f.readlines()
i = 0

while i < len(lines) - 7:
    i += 1 #skip one separatin line
    state = lines[i].split(" ")[-1][0]
    i += 2
    if_0 = {}
    if_0["w"] = int(lines[i].split(" ")[-1][0])
    i += 1
    if(lines[i].split(" ")[-1] == "left.\n"):
        if_0["m"] = -1
    else:
        if_0["m"] = 1
    i += 1
    if_0["n"] = lines[i].split(" ")[-1][0]

    i += 2
    if_1 = {}
    if_1["w"] = int(lines[i].split(" ")[-1][0])
    i += 1
    if(lines[i].split(" ")[-1] == "left.\n"):
        if_1["m"] = -1
    else:
        if_1["m"] = 1
    i += 1
    if_1["n"] = lines[i].split(" ")[-1][0]
    i += 1
    states[state] = [if_0, if_1]

currentState = begin
steps = 0
memory = {}
pos = 0

while(steps < checksum_at):
    if(not memory.has_key(pos)):
        memory[pos] = 0

    val = memory[pos]
    memory[pos] = states[currentState][val]["w"]
    pos += states[currentState][val]["m"]
    currentState = states[currentState][val]["n"]
    steps += 1


checksum = 0
for value in memory.values():
    checksum += value

print checksum
