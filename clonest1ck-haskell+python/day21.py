
class Rule(object):
    def __init__(self, rulestring):
        rulestring = rulestring.split(" => ")
        self.patterns = Pattern(rulestring[0]).combinations()
        self.out = [Pattern(rulestring[1])]
        self.size = self.patterns[0].size

    def match(self, pattern):
        for p in self.patterns:
            if pattern.__eq__(p):
                return self.out
        return None

class Pattern(object):
    def __init__(self, patternstr):
        patternstr = patternstr.split("/")
        self.size = len(patternstr)
        self.pattern = []
        for row in patternstr:
            pattern = []
            for char in row:
                pattern.append(char)
            self.pattern.append(pattern)

    def __eq__(self, p2):
        if self.size != p2.size:
            return False
        for i in range(self.size):
            for j in range(self.size):
                if self.pattern[i][j] != p2.pattern[i][j]:
                    return False
        return True

    def split(self, patternstr):
        patternstr = patternstr.split("\n")
        patterns = []
        size = len(patternstr[0])
        if(size % 2 == 0):
            for y in range(0, size, 2):
                for x in range(0, size, 2):
                    patterns.append(Pattern(patternstr[y][x:x+2] + "/" + patternstr[y+1][x:x+2]))
        else:
            for y in range(0, size, 3):
                for x in range(0, size, 3):
                    patterns.append(Pattern(patternstr[y][x:x+3] + "/" + patternstr[y+1][x:x+3] + "/" + patternstr[y+2][x:x+3]))
        return patterns

    def combinations(self):
        comb = [self, self.flipX(), self.flipY()]
        res = []
        for start in comb:
            res.append(start)
            for i in range(3):
                start = start.rotate()
                if start not in res:
                    res.append(start)
        return res

    def flipX(self):
        pattern = reversed(self.pattern[:])
        pattern = "/".join(["".join(p) for p in pattern])
        return Pattern(pattern)

    def flipY(self):
        pattern = self.pattern[:]
        pattern = [reversed(p) for p in pattern]
        pattern = "/".join(["".join(p) for p in pattern])
        return Pattern(pattern)

    def rotate(self):
        pattern = self.pattern[:]
        if(self.size == 2):
            pattern = [
                [pattern[1][0], pattern[0][0]],
                [pattern[1][1], pattern[0][1]]
            ]
        else:
            pattern = [
                [pattern[2][0], pattern[1][0], pattern[0][0]],
                [pattern[2][1], pattern[1][1], pattern[0][1]],
                [pattern[2][2], pattern[1][2], pattern[0][2]]
            ]
        pattern = "/".join(["".join(p) for p in pattern])
        return Pattern(pattern)

    def filled(self):
        filled = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.pattern[i][j] == "#":
                    filled += 1

        return filled

    def __str__(self):
        return "\n".join(["".join(x) for x in self.pattern])

    def x(self):
        return "".join(self.pattern[0])

    def y(self):
        return "".join(self.pattern[1])

    def z(self):
        if(self.size > 2):
            return "".join(self.pattern[2])
        else:
            return None

    def g(self):
        if(self.size > 3):
            return "".join(self.pattern[3])
        else:
            return None

    def asString(self, patterns):
        length = int(len(patterns) ** 0.5)
        out = ""
        y = 0
        for y in range(length):
            for j in range(patterns[0].size):
                for i in range(length):
                    if(j == 0):
                        out += patterns[y * length + i].x()
                    elif(j == 1):
                        out += patterns[y * length + i].y()
                    elif(j == 2):
                        out += patterns[y * length + i].z()
                    elif(j == 3):
                        out += patterns[y * length + i].g()
                out += "\n"
        return out


def iteratePatterns(times):
    f = open("in21.txt", 'r')
    rules = []
    patterns = [Pattern(".#./..#/###")]

    for line in f.readlines():
        rules.append(Rule(line.split("\n")[0]))

    for i in range(times):
        nextPatterns = []
        for pattern in patterns:
            for rule in rules:
                match = rule.match(pattern)
                if match is not None:
                    for m in match:
                        nextPatterns.append(m)
                    break
        patterns = patterns[0].split(patterns[0].asString(nextPatterns))
    return patterns


pat = iteratePatterns(5)
print "Task 1: " + str(sum([p.filled() for p in pat]))
pat = iteratePatterns(18)
print "Task 2: " + str(sum([p.filled() for p in pat]))
